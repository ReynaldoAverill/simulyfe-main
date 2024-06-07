#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Run code using this syntax
// gcc writer.c -o writer -luser32 -lkernel32

#define SHM_SIZE 1024  // Size of the shared memory segment

int main() {
    HANDLE hMapFile;
    LPCTSTR pBuf;

    // Create a named shared memory segment
    hMapFile = CreateFileMapping(
                 INVALID_HANDLE_VALUE,    // Use paging file
                 NULL,                    // Default security
                 PAGE_READWRITE,          // Read/write access
                 0,                       // Maximum object size (high-order DWORD)
                 SHM_SIZE,                // Maximum object size (low-order DWORD)
                 "Local\\MySharedMemory"); // Name of mapping object

    if (hMapFile == NULL) {
        printf("Could not create file mapping object (%d).\n", GetLastError());
        return 1;
    }

    pBuf = (LPTSTR) MapViewOfFile(hMapFile,   // Handle to map object
                                  FILE_MAP_ALL_ACCESS, // Read/write permission
                                  0,
                                  0,
                                  SHM_SIZE);

    if (pBuf == NULL) {
        printf("Could not map view of file (%d).\n", GetLastError());
        CloseHandle(hMapFile);
        return 1;
    }

    // Write data to the shared memory segment
    for (int i = 0; i < 10; i++) {
        char buffer[SHM_SIZE];
        sprintf(buffer, "Message %d from C program", i);
        CopyMemory((PVOID)pBuf, buffer, (strlen(buffer) + 1) * sizeof(char));
        Sleep(1000);  // Sleep for a second
    }

    // Unmap the shared memory segment and close the handle
    UnmapViewOfFile(pBuf);
    CloseHandle(hMapFile);

    return 0;
}
