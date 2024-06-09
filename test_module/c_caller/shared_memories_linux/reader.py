import os
import time
import ctypes

# Shared memory key
key = os.ftok('shmfile', 65)

# Get the shared memory segment
shm_id = ctypes.CDLL('libc.so.6').shmget(key, 1024, 0o666)

# Attach the shared memory segment
shm_ptr = ctypes.CDLL('libc.so.6').shmat(shm_id, None, 0)

# Cast the pointer to a string pointer
shared_memory = ctypes.cast(shm_ptr, ctypes.POINTER(ctypes.c_char * 1024))

try:
    while True:
        message = shared_memory.contents.value.decode('utf-8')
        if message:
            print(f"Received: {message}")
        time.sleep(1)
except KeyboardInterrupt:
    pass

# Detach the shared memory
ctypes.CDLL('libc.so.6').shmdt(shm_ptr)
