from subprocess import Popen, PIPE

perintah    = [".\coba"]
# perintah = "./coba"

proc = Popen(perintah, stdout = PIPE, stderr = PIPE,text=True)

hasil, err = proc.communicate()

# resp = hasil.decode("utf-8")

print(hasil)