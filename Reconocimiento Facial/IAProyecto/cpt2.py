import cv2
import numpy as np

# Inicializar la cámara
cap = cv2.VideoCapture(0)

while True:
    # Capturar un frame
    ret, frame = cap.read()

    # Convertir el frame a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#

    # Definir el rango de color rojo en HSV
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])

    # Crear una máscara que incluya solo el color rojo
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Ajustar el tamaño de la máscara para que tenga las mismas dimensiones que el frame original
    mask = cv2.resize(
        mask, (frame.shape[1], frame.shape[0]), interpolation=cv2.INTER_NEAREST)

    # Aplicar la máscara al frame original
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Ajustar el tamaño de la imagen resultante para que tenga las mismas dimensiones que el frame original
    res = cv2.resize(
        res, (frame.shape[1], frame.shape[0]), interpolation=cv2.INTER_NEAREST)

    # Concatenar horizontalmente los frames
    # result = cv2.hconcat([frame, res, mask])

    # Mostrar el resultado
   # cv2.imshow('Detector de color', result)
    cv2.imshow('Original', frame)
    cv2.imshow('Máscara', mask)
    cv2.imshow('Resultado', res)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
