from subprocess import Popen, PIPE, STDOUT
import time

create_exe  = ['gcc','-o','coba','number_gen.c']
perintah    = [".\coba"]
# perintah = "./coba"

# proc1 = Popen(create_exe)
# proc1.wait()
print("exe file created")
# proc = Popen(perintah, stdout = PIPE, stderr = PIPE,text=True,universal_newlines=True)
# print("open exe file")
# while (True):
#     print(proc.stdout.readline())
#     time.sleep(1)

# Start the C program as a subprocess
process = Popen(perintah, stdout=PIPE, stderr=PIPE, text=True)

# Read the output continuously
while True:
    output = process.stdout.readline()
    if output == '' and process.poll() is not None:
        break
    if output:
        print(f"Received from C program: {output.strip()}")

# Check for any error messages
error_output = process.stderr.read()
if error_output:
    print(f"Error: {error_output.strip()}")

# hasil, err = proc.communicate()

# resp = hasil.decode("utf-8")

# print(hasil)