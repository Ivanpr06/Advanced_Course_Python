import sys

from PIL import Imagen

imagenes = []

for arg in sys.argv[1:]:
    imagen = Imagen.open(arg)
    imagenes.append(imagen)

imagenes[0].save(
    "disfraz.gif", save_all=True, append_images=imagenes[1:], duration=200, loop=0
)