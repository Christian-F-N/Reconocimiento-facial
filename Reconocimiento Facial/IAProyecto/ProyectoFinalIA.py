import cv2
import numpy as np

# Diccionario con los colores y sus rangos en HSV
colors = {
    "Negro": (np.array([0, 0, 0]), np.array([180, 255, 30])),
    "Azul": (np.array([100, 50, 50]), np.array([140, 255, 255])),
    "Marrón": (np.array([10, 100, 20]), np.array([20, 255, 255])),
    "Verde": (np.array([35, 50, 50]), np.array([90, 255, 255])),
    "Rojo": (np.array([0, 50, 50]), np.array([10, 255, 255])),
    "Amarillo": (np.array([20, 100, 100]), np.array([30, 255, 255])),
    "Blanco": (np.array([0, 0, 200]), np.array([180, 30, 255])),
    "Gris": (np.array([0, 0, 70]), np.array([180, 30, 220]))
}

# Inicializa la cámara
cap = cv2.VideoCapture(1)

while True:
    # Captura un frame de la cámara
    ret, frame = cap.read()

    # Convierte la imagen a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Itera sobre los colores
    for color_name, (lower, upper) in colors.items():

        # Crea una máscara para el color actual
        mask = cv2.inRange(hsv, lower, upper)

        # Encuentra los contornos de los objetos en la máscara
        contours, hierarchy = cv2.findContours(
            mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Itera sobre los contornos encontrados
        for contour in contours:

            # Calcula el área del contorno
            area = cv2.contourArea(contour)

            # Si el área es mayor a 10000, dibuja el contorno y muestra el nombre del color
            if area > 10000:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 108, 255), 2)
                cv2.putText(frame, color_name, (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 108, 255), 2)

    # Muestra la imagen con los contornos y los nombres de los colores
    cv2.imshow("Detector de Colores", frame)

    # Si se presiona la tecla "q", sale del bucle
    if cv2.waitKey(1) == 27:
        break

# Libera la cámara y destruye las ventanas
cap.release
