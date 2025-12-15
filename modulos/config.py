import json
import os
# Ruta al archivo JSON
BASE_DIR = os.path.dirname(__file__)  # carpeta actual (pygame_interface)
CATEGORIAS_PATH = os.path.abspath(os.path.join(BASE_DIR, "../json/categorias.json"))

with open(CATEGORIAS_PATH, "r", encoding="utf-8") as f:
    OPCIONES_JUGADAS = json.load(f)