import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while True:
    ret, frame =cap.read()
    if ret:
        cv2.imshow("frame",frame)
        # cv2.waitkey(10)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()