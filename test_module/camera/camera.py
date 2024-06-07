import cv2 as cv
import os
from datetime import datetime

cam = cv.VideoCapture(0)
cam.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
output_dir = '/media/simulyfe/DataVideo'
os.chdir('/media/simulyfe/DataVideo')

if not os.path.exists(output_dir):
    os.mkdir(output_dir)
os.chdir('hasil')
cc = cv.VideoWriter_fourcc(*'mp4v')
date = datetime.now().strftime("%d-%m-%Y_%H.%M.%S")
filename = f"video_{date}.mp4"
file = cv.VideoWriter(filename, cc, 30.0, (640, 480))

if not cam.isOpened():
    print("Error opening camera")
    exit()

while True:
    ret, frame = cam.read()

    if not ret:
        print("Error in retrieving frame")
        break
    cv.imshow('frame', frame)
    file.write(frame)

    if cv.waitKey(1) == ord('q'):
        break
    
cam.release()
file.release()
cv.destroyAllWindows()