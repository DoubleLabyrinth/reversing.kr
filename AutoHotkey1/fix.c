#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <windows.h>

uint32_t table[256];

uint8_t keyword[16] = {
    0xA3, 0x48, 0x4B, 0xBE, 0x98, 0x6C, 0x4A, 0xA9, 
	0x99, 0x4C, 0x53, 0x0A, 0x86, 0xD6, 0x48, 0x7D 
};

void init_table() {
    for (int i = 0; i < 256; ++i) {
        int tmp = i << 24;
        for (int j = 0; j < 8; ++j) {
            if (tmp >= 0)
                tmp *= 2;
            else
                tmp = 2 * tmp ^ 0x4C11DB7;
        }
        table[i] = tmp;
    }
}

uint32_t calc_checksum(uint32_t init_value, PVOID lpContent, DWORD dwSize) {
    for (DWORD i = 0; i < dwSize; ++i)
        init_value = (init_value << 8) ^ table[((uint8_t*)lpContent)[i] ^ (init_value >> 24)];
    return init_value;
}

int main(int argc, char* argv[]) {
    init_table();

    HANDLE hFile = INVALID_HANDLE_VALUE;
    HANDLE hFileMap = NULL;
    DWORD dwFileSize = 0;
    PVOID lpContent = NULL;
	uint32_t relocated = 0;
    uint32_t checksum = 0;

    hFile = CreateFileA(argv[1], 
                        GENERIC_READ | GENERIC_WRITE, 
                        0, 
                        NULL, 
                        OPEN_EXISTING, 
                        FILE_ATTRIBUTE_NORMAL, 
                        NULL);
    if (hFile == INVALID_HANDLE_VALUE) {
        printf("CreateFileA: 0x%08X\n", GetLastError());
        goto ON_main_ERROR;
    }

    hFileMap = CreateFileMappingA(hFile, 
                                  NULL, 
                                  PAGE_READWRITE, 
                                  0, 
                                  0, 
                                  NULL);
    if (hFileMap == NULL) {
        printf("CreateFileMappingA: 0x%08X\n", GetLastError());
        goto ON_main_ERROR;
    }

    dwFileSize = GetFileSize(hFile, NULL);
    
    lpContent = MapViewOfFile(hFileMap, FILE_MAP_READ | FILE_MAP_WRITE, 0, 0, 0);
    if (lpContent == NULL) {
        printf("CreateFileMappingA: 0x%08X\n", GetLastError());
        goto ON_main_ERROR;
    }
	
	for (DWORD i = dwFileSize - sizeof(keyword); i > 0; --i) {
		if (memcmp((uint8_t*)lpContent + i, keyword, sizeof(keyword)) == 0) {
			*(uint32_t*)((uint8_t*)lpContent + dwFileSize - 8) = i;
			relocated = 1;
			break;
		}
	}
	
	if (relocated == 0) {
		printf("Cannot find keyword.\n");
		goto ON_main_ERROR;
	}

    checksum = calc_checksum(-1, lpContent, dwFileSize - 4);
	checksum ^= 0xAAAAAAAA;
    printf("checksum = 0x%X\n", checksum);
	
	*(uint32_t*)((uint8_t*)lpContent + dwFileSize - 4) = checksum;

ON_main_ERROR:
    if (lpContent)
        UnmapViewOfFile(lpContent);
    if (hFileMap)
        CloseHandle(hFileMap);
    if (hFile)
        CloseHandle(hFile);
    return 0;
}
