import cv2
import numpy as np

# Define los límites de color (en BGR) para cada color que se desea detectar
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([140, 255, 255])
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
lower_green = np.array([50, 100, 100])
upper_green = np.array([70, 255, 255])

colors = {
    "blue": (lower_blue, upper_blue),
    "red": (lower_red, upper_red),
    "green": (lower_green, upper_green)
}

# Inicializa la cámara
cap = cv2.VideoCapture(1)

while True:
    # Captura una imagen desde la cámara
    ret, frame = cap.read()

    # Convierte la imagen a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Inicializa una lista para almacenar las máscaras y contornos
    masks = []
    contours_list = []

    # Crea una máscara para cada color
    for color, bounds in colors.items():
        lower, upper = bounds
        mask = cv2.inRange(hsv, lower, upper)
        masks.append(mask)

        # Encuentra los contornos de los objetos detectados
        contours, _ = cv2.findContours(
            mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours_list.append(contours)

    # Dibuja los contornos y nombres de los colores detectados en la imagen original
    for color, contours in zip(colors.keys(), contours_list):
        for contour in contours:
            # Solo muestra el nombre del color si el área del objeto es mayor a 5000
            if cv2.contourArea(contour) > 5000:
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, color, (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Muestra la imagen resultante en una ventana
    cv2.imshow("Detected Colors", frame)
    # Sale del bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la cámara y destruye las ventanas
cap.release()
cv2.destroyAllWindows()
