#include <time.h>
#include <stdio.h>
#include <windows.h>

int main(int argc, char* argv[]) {
    STARTUPINFO si = { sizeof(STARTUPINFO) };
    PROCESS_INFORMATION pi = {};
    char ProcessName[] = "Lotto.exe";

    srand(_time64(NULL));
	printf("Here is the numbers:\n");
    for (int i = 0; i < 6; ++i) {
        printf("%d ", rand() % 100);
    }
    printf("\n");
    
    CreateProcess(ProcessName, ProcessName, NULL, NULL, FALSE, NULL, NULL, NULL, &si, &pi);
    WaitForSingleObject(pi.hProcess, INFINITE);
    CloseHandle(pi.hThread);
    CloseHandle(pi.hProcess);
    return 0;
}
