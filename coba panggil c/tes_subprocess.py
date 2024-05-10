from subprocess import Popen, PIPE

perintah = "./coba"

proc = Popen(perintah, stdout = PIPE, stderr = PIPE)

hasil, err = proc.communicate()

resp = hasil.decode("utf-8")

print(resp)