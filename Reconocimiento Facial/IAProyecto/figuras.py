import cv2
import numpy as np

# Define los colores que se van a detectar
colors = {'rojo': (0, 0, 255), 'verde': (0, 255, 0), 'azul': (255, 0, 0),
          'amarillo': (0, 255, 255), 'morado': (255, 0, 255), 'blanco': (255, 255, 255),
          'negro': (0, 0, 0), 'gris': (125, 125, 125)}

# Inicializa la cámara
captura = cv2.VideoCapture(1)

while True:
    # Toma una imagen de la cámara
    ret, frame = captura.read()

    # Convierte la imagen a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Recorre los colores
    figuras = []
    for color_name, color_value in colors.items():
        # Crea una máscara para el color actual
        lower = np.array([50, 50, 50])
        upper = np.array([255, 255, 255])
        mask = cv2.inRange(hsv, lower, upper)

        # Encuentra los contornos de la máscara
        contours, _ = cv2.findContours(
            mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Dibuja los contornos en la imagen
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                figuras.append((x, y, w, h, color_name))

    # Ordena las figuras por tamaño
    figuras = sorted(figuras, key=lambda x: x[2]*x[3], reverse=True)

    # Muestra solo las 5 figuras más grandes
    for x, y, w, h, color_name in figuras[:5]:
        cv2.rectangle(frame, (x, y), (x+w, y+h), colors[color_name], 2)
        cv2.putText(frame, color_name, (x, y-5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors[color_name], 2)

    # Muestra la imagen
    cv2.imshow('Deteccion de colores', frame)

    # Sale del ciclo si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la cámara
captura.release()

# Cierra las ventanas
cv2.destroyAllWindows()
