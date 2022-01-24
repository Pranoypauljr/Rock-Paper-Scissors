import cv2 as cv
import mediapipe as mp
import time as t
capture = cv.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands(False, 1, 1, 0.5, 0.4)
mpDraw = mp.solutions.drawing_utils

# initializing time variables to calculate fps
ctime = 0
ptime = 0

while True:
    ret, frame = capture.read()

    rgbimg = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    result = hands.process(rgbimg)

    # drawing markers and lines over hand coordinates
    # print(result.multi_hand_landmarks)
    if(result.multi_hand_landmarks):
        for cords in result.multi_hand_landmarks:
            for id, marks in enumerate(cords.landmark):
                print(id, marks)

            mpDraw.draw_landmarks(frame, cords, mphands.HAND_CONNECTIONS)

    # to find fps(frames per second)
    ctime = t.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    # to display the fps on the screen
    cv.putText(frame, str(int(fps)), (10, 70),
               cv.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 4)

    cv.imshow('livestream', frame)
    if(cv.waitKey(1) & 0xFF == ord('d')):
        break
capture.release()
cv.destroyAllWindows()
