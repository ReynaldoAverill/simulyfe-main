from subprocess import Popen, PIPE, STDOUT
import time

create_exe  = ['gcc','-o','coba','number_gen.c']
perintah    = [".\coba"]
# perintah = "./coba"
proc1 = Popen(create_exe)
proc1.wait()
print("exe file created")
proc = Popen(perintah, stdout = PIPE, stderr = PIPE,text=True,universal_newlines=True)
print("open exe file")
while (True):
    print(proc.stdout.readline())
    time.sleep(1)
hasil, err = proc.communicate()

# resp = hasil.decode("utf-8")

print(hasil)