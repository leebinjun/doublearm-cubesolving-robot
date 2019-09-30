from cv2 import cv2
import time

cap = cv2.VideoCapture(0)
ret, img = cap.read()

while ret:
    ret, img = cap.read()
    cv2.imshow("", img)
    key = cv2.waitKey(10)

    if key == ord('q'):
        break
    if key == ord('s'):
        file_name = str(time.time()) + '.jpg'
        cv2.imwrite(file_name, img)

    




