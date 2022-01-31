import handtrackmodule as ht
import cv2 as cv
import time as t
import os

wCam, hCam = 640, 480
capture = cv.VideoCapture(0)
capture.set(3, wCam)
capture.set(4, hCam)

# to list the image in the image folder
folderpath = "./rps images"
mylist = os.listdir(folderpath)
print(mylist)

# to store image path to a list and access it
overlaylist = []
for impath in mylist:
    actualpath = cv.imread(f'{folderpath}/{impath}')
    overlaylist.append(actualpath)

# print(len(overlaylist))
# print(overlaylist[2].shape)

# initializing required variables to calculate frame rate.
ctime = 0
ptime = 0

# initializing a detector variable
detector = ht.handDetector(mode=False, maxHands=1,
                           detectionCon=0.5, trackCon=0.4)


while True:
    ret, frame = capture.read()

    # to use findhands method to detect hands and show it in the frame
    frame = detector.findHands(frame)

    # to find position of different coordinates and print its info list for each coordinate.
    cordlist = detector.findPosition(frame, draw=False)
    print(cordlist)

    # to display the info array of coordinates if and only if the array is non-empy!
    if len(cordlist) != 0:
        if(cordlist[8][2] > )

    # to get the pic dimensions and adjust the screen and fit in the pic to the screen according to its dimensions.
    h, w, c = overlaylist[0].shape
    frame[0:h, 0:w] = overlaylist[0]

    # to calculate frame rate
    ctime = t.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv.putText(frame, f'fps:{int(fps)}', (400, 70),
               cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv.imshow('frame', frame)
    if(cv.waitKey(1) & 0xFF == ord('d')):
        break

# capture.release()
# cv.destroyAllWindows()
