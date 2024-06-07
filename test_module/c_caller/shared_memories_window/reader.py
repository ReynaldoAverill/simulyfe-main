import time
import ctypes
from ctypes import wintypes

# Define constants
SHM_SIZE = 1024

# Define the shared memory name
shm_name = "Local\\MySharedMemory"

# Load Windows libraries
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

# Define required Windows structures and functions
OpenFileMapping = kernel32.OpenFileMappingW
OpenFileMapping.restype = wintypes.HANDLE
OpenFileMapping.argtypes = (wintypes.DWORD, wintypes.BOOL, wintypes.LPCWSTR)

MapViewOfFile = kernel32.MapViewOfFile
MapViewOfFile.restype = wintypes.LPVOID
MapViewOfFile.argtypes = (wintypes.HANDLE, wintypes.DWORD, wintypes.DWORD, wintypes.DWORD, ctypes.c_size_t)

UnmapViewOfFile = kernel32.UnmapViewOfFile
UnmapViewOfFile.restype = wintypes.BOOL
UnmapViewOfFile.argtypes = (wintypes.LPCVOID,)

CloseHandle = kernel32.CloseHandle
CloseHandle.restype = wintypes.BOOL
CloseHandle.argtypes = (wintypes.HANDLE,)

# Open the shared memory segment
hMapFile = OpenFileMapping(0x0004, False, shm_name)
if not hMapFile:
    raise ctypes.WinError(ctypes.get_last_error())

# Map the shared memory segment into the address space
pBuf = MapViewOfFile(hMapFile, 0x0004, 0, 0, SHM_SIZE)
if not pBuf:
    CloseHandle(hMapFile)
    raise ctypes.WinError(ctypes.get_last_error())

# Define a ctypes string buffer to read the data
buffer = ctypes.create_string_buffer(SHM_SIZE)

try:
    while True:
        # Read the data from the shared memory
        ctypes.memmove(buffer, pBuf, SHM_SIZE)
        message = buffer.value.decode('utf-8')
        if message:
            print(f"Received: {message}")
        time.sleep(1)
except KeyboardInterrupt:
    pass

# Unmap the shared memory segment and close the handle
UnmapViewOfFile(pBuf)
CloseHandle(hMapFile)
