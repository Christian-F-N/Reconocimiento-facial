import cv2
import imutils
import numpy as np
print("Librerias leidas")

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Rojo
    rojo_os = np.array([0, 0, 255])
    rojo_cl = np.array([102, 102, 255])
# Naranja
    naraj_os = np.array([0, 153, 255])
    naraj_cl = np.array([102, 178, 255])
# Amarillo
    amarill_os = np.array([0, 255, 255])
    amarill_cl = np.array([153, 255, 255])
# Verde
    verd_os = np.array([0, 255, 0])
    verd_cl = np.array([102, 255, 102])

# Azul
    azul_os = np.array([255, 0, 0])
    azul_cl = np.array([255, 102, 102])
# Morado
    mora_os = np.array([102, 0, 102])
    mora_cl = np.array([153, 0, 153])
# Rosa
    rosa_os = np.array([255, 0, 255])
    rosa_cl = np.array([204, 153, 255])
# Marron
    marron_os = np.array([0, 51, 102])
    marron_cl = np.array([0, 102, 178])
# Gris
    gris_os = np.array([128, 128, 128])
    gris_cl = np.array([192, 192, 192])
# Blanco
    blanco_os = np.array([255, 255, 255])
    blanco_cl = np.array([255, 255, 255])
# Negro
    negro_os = np.array([0, 0, 0])
    negro_cl = np.array([0, 0, 0])
# Cyan
    cyan_os = np.array([255, 255, 0])
    cyan_cl = np.array([255, 255, 102])
# Magenta
    mange_os = np.array([255, 0, 255])
    mange_cl = np.array([255, 102, 255])
# AmarilloClaro
    amarill2_os = np.array([153, 255, 255])
    amarill2_cl = np.array([204, 255, 255])

    cara1 = cv2.inRange(hsv, rojo_os, rojo_cl)
    cara2 = cv2.inRange(hsv, naraj_os, naraj_cl)
    cara3 = cv2.inRange(hsv, amarill_os, amarill_cl)
    cara4 = cv2.inRange(hsv, verd_os, verd_cl)
    cara5 = cv2.inRange(hsv, azul_os, azul_cl)
    cara6 = cv2.inRange(hsv, mora_os, mora_cl)
    cara7 = cv2.inRange(hsv, rosa_os, rosa_cl)
    cara8 = cv2.inRange(hsv, marron_os, marron_cl)
    cara9 = cv2.inRange(hsv, gris_os, gris_cl)
    cara10 = cv2.inRange(hsv, blanco_os, blanco_cl)
    cara11 = cv2.inRange(hsv, negro_os, negro_cl)
    cara12 = cv2.inRange(hsv, cyan_os, cyan_cl)
    cara13 = cv2.inRange(hsv, mange_os, mange_cl)
    cara14 = cv2.inRange(hsv, amarill2_os, amarill2_cl)

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

    cnt6 = cv2.findContours(cara6, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt6 = imutils.grab_contours(cnt6)

    cnt7 = cv2.findContours(cara7, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt7 = imutils.grab_contours(cnt7)

    cnt8 = cv2.findContours(cara8, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt8 = imutils.grab_contours(cnt8)

    cnt9 = cv2.findContours(cara9, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt9 = imutils.grab_contours(cnt9)

    cnt10 = cv2.findContours(cara10, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt10 = imutils.grab_contours(cnt10)

    cnt11 = cv2.findContours(cara11, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt11 = imutils.grab_contours(cnt11)

    cnt12 = cv2.findContours(cara12, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt12 = imutils.grab_contours(cnt12)

    cnt13 = cv2.findContours(cara13, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt13 = imutils.grab_contours(cnt13)

    cnt14 = cv2.findContours(cara14, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt14 = imutils.grab_contours(cnt14)
    MIN_AREA = 500

    for c in cnt1:
        print(c, "", cnt1)
        area = cv2.contourArea(c)
        if area > MIN_AREA:

            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Rojo", (cx-20, cy-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)
    print('paso')
    for c in cnt2:
        area = cv2.contourArea(c)
        if area > MIN_AREA:

            cv2.drawContours(frame, [c], -1, (30, 255, 255), 3)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Naranja", (cx-20, cy-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

    for c in cnt3:
        area = cv2.contourArea(c)
        if area > MIN_AREA:

            cv2.drawContours(frame, [c], -1, (30, 255, 255), 3)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Amarillo", (cx-20, cy-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

    for c in cnt4:
        area = cv2.contourArea(c)
        if area > MIN_AREA:

            cv2.drawContours(frame, [c], -1, (30, 255, 255), 3)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Verde", (cx-20, cy-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

    for c in cnt5:
        area = cv2.contourArea(c)
        if area > MIN_AREA:

            cv2.drawContours(frame, [c], -1, (30, 255, 255), 3)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Azul", (cx-20, cy-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

    for c in cnt6:

        area = cv2.contourArea(c)
        if area > MIN_AREA:

            # ----------------------------------B     G    R-------------------
            cv2.drawContours(frame, [c], -1, (255, 30, 136), 3)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Morado", (cx-20, cy-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

    for c in cnt7:

        area = cv2.contourArea(c)
        if area > MIN_AREA:

            cv2.drawContours(frame, [c], -1, (30, 255, 255), 3)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Rosa", (cx-20, cy-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)
    for c in cnt8:

        area = cv2.contourArea(c)
        if area > MIN_AREA:

            cv2.drawContours(frame, [c], -1, (30, 255, 255), 3)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Marrón", (cx-20, cy-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

    for c in cnt9:

        area = cv2.contourArea(c)
        if area > MIN_AREA:

            cv2.drawContours(frame, [c], -1, (30, 255, 255), 3)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Gris", (cx-20, cy-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

    for c in cnt10:

        area = cv2.contourArea(c)
        if area > MIN_AREA:

            cv2.drawContours(frame, [c], -1, (30, 255, 255), 3)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Blanco", (cx-20, cy-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

    for c in cnt11:

        area = cv2.contourArea(c)
        if area > MIN_AREA:

            cv2.drawContours(frame, [c], -1, (30, 255, 255), 3)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Negro", (cx-20, cy-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

    for c in cnt12:

        area = cv2.contourArea(c)
        if area > MIN_AREA:

            cv2.drawContours(frame, [c], -1, (30, 255, 255), 3)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Cyan", (cx-20, cy-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

    for c in cnt13:

        area = cv2.contourArea(c)
        if area > MIN_AREA:

            cv2.drawContours(frame, [c], -1, (30, 255, 255), 3)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Magenta", (cx-20, cy-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

    for c in cnt14:
        area = cv2.contourArea(c)
        if area > MIN_AREA:

            cv2.drawContours(frame, [c], -1, (30, 255, 255), 3)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Amarillo claro", (cx-20, cy-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
