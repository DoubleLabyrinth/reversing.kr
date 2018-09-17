#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <windows.h>

int main(int argc, char* argv[]) {
    DWORD dwLastError = ERROR_SUCCESS;
    HANDLE hFile = INVALID_HANDLE_VALUE;
    HANDLE hFileMap = NULL;
    uint8_t* lpFileContent = NULL;
    uint8_t* lpfnMetMett = NULL;
    size_t fnMetMettSize = 0x622 - 0x538;

    hFile = CreateFileA(argv[1],
                        GENERIC_READ | GENERIC_WRITE,
                        0,
                        NULL,
                        OPEN_EXISTING,
                        FILE_ATTRIBUTE_NORMAL,
                        NULL);
    if (hFile == INVALID_HANDLE_VALUE) {
        dwLastError = GetLastError();
        printf("[LINE: %u] CreateFile failed. CODE: 0x%08X\n", __LINE__, dwLastError);
        goto ON_tmain_ERROR;
    }

    hFileMap = CreateFileMapping(hFile, 
                                 NULL, 
                                 PAGE_READWRITE, 
                                 0, 
                                 0, 
                                 NULL);
    if (hFileMap == NULL) {
        dwLastError = GetLastError();
        printf("[LINE: %u] CreateFileMapping failed. CODE: 0x%08X\n", __LINE__, dwLastError);
        goto ON_tmain_ERROR;
    }

    lpFileContent = (uint8_t*)MapViewOfFile(hFileMap,
                                            FILE_MAP_READ | FILE_MAP_WRITE,
                                            0,
                                            0,
                                            0);
    if (lpFileContent == NULL) {
        dwLastError = GetLastError();
        printf("[LINE: %u] MapViewOfFile failed. CODE: 0x%08X\n", __LINE__, dwLastError);
        goto ON_tmain_ERROR;
    }

    {
        uint8_t num = 0;
        lpfnMetMett = lpFileContent + 0x538;
        for (size_t i = 0; i < fnMetMettSize; ++i) 
            num += ++lpfnMetMett[i];
        lpfnMetMett[0x12] = num - 0x26;
        lpfnMetMett[0x23] = num - 0x3;
        lpfnMetMett[0x34] = num ^ 0x27;
        lpfnMetMett[0x45] = num - 0x15;
        lpfnMetMett[0x57] = 0x47 - num;
        lpfnMetMett[0x7c] = num ^ 0x72;
        lpfnMetMett[0x8d] = num ^ 0x50;
        lpfnMetMett[0x9f] = 0xeb - num;
        lpfnMetMett[0xb3] = num + 0x6a;
        lpfnMetMett[0xc8] = 0x24 - num;
        lpfnMetMett[0xdc] = num - 0x3;
    }

ON_tmain_ERROR:
    if (lpFileContent)
        UnmapViewOfFile(lpFileContent);
    if (hFileMap)
        CloseHandle(hFileMap);
    if (hFile)
        CloseHandle(hFile);
    return dwLastError;
}

