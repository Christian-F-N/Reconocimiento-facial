import pyheif
from PIL import Image

# Ruta de la imagen .heic
ruta_imagen_heic = 'ruta/a/tu/imagen.heic'

# Abrir el archivo .heic
archivo_heic = pyheif.read(ruta_imagen_heic)

# Obtener los datos de píxeles de la imagen
datos_pixeles = archivo_heic.image

# Crear una imagen PIL desde los datos de píxeles
imagen_pil = Image.frombytes(
    size=archivo_heic.size,
    mode=archivo_heic.mode,
    data=datos_pixeles
)

# Mostrar la imagen
imagen_pil.show()
