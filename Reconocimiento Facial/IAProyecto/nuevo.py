import cv2
import imutils
import numpy as np
print("Librerias leidas")
# URL del servidor de transmisión de video
url = "http://192.168.1.4:4747/video"

# Conectarse al servidor de transmisión de video
cap = cv2.VideoCapture(1)
# cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# amarillo
    amarillo_osc = np.array([25, 70, 120])
    amarillo_cl = np.array([30, 255, 255])
# Rojo
    rojo_osc = np.array([0, 50, 120])
    rojo_cl = np.array([10, 255, 255])
# verde
    verde_osc = np.array([40, 70, 80])
    verde_cl = np.array([70, 255, 255])
# azul
    azul_cl = np.array([121, 255, 255])
    azul_osc = np.array([90, 60, 0])
# Negro
    negro_osc = np.array([0, 0, 0])
    negro_cl = np.array([68, 71, 68])

    cara1 = cv2.inRange(hsv, amarillo_osc, amarillo_cl)
    cara2 = cv2.inRange(hsv, rojo_osc, rojo_cl)
    cara3 = cv2.inRange(hsv, verde_osc, verde_cl)
    cara4 = cv2.inRange(hsv, azul_osc, azul_cl)
    cara5 = cv2.inRange(hsv, negro_osc, negro_cl)

    cnt1 = cv2.findContours(cara1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt1 = imutils.grab_contours(cnt1)

    cnt2 = cv2.findContours(cara2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt2 = imutils.grab_contours(cnt2)

    cnt3 = cv2.findContours(cara3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt3 = imutils.grab_contours(cnt3)

    cnt4 = cv2.findContours(cara4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt4 = imutils.grab_contours(cnt4)

    cnt5 = cv2.findContours(cara5, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt5 = imutils.grab_contours(cnt5)

    for c in cnt1:
        area = cv2.contourArea(c)
        if area > 5000:
            cv2.drawContours(frame, [c], -1, (30, 255, 255), 3)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Amarillo", (cx-20, cy-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

    for c in cnt2:
        area = cv2.contourArea(c)
        if area > 5000:
            cv2.drawContours(frame, [c], -1, (0, 0, 255), 3)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Rojo", (cx-20, cy-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)
    for c in cnt3:
        area = cv2.contourArea(c)
        if area > 5000:
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Verde", (cx-20, cy-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

    for c in cnt5:
        area = cv2.contourArea(c)
        if area > 5000:
            cv2.drawContours(frame, [c], -1, (68, 74, 68), 3)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Negro", (cx-20, cy-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)
    for c in cnt4:
        area = cv2.contourArea(c)
        if area > 5000:
            cv2.drawContours(frame, [c], -1, (255, 0, 0), 3)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Azul", (cx-20, cy-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
