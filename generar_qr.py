import os
import qrcode

# Lee la URL base de la app desde variables de entorno
# Ejemplos:
# - Local: http://127.0.0.1:8000/
# - Railway: https://<tu-subdominio>.up.railway.app/
BASE_URL = os.getenv("APP_URL", "https://web-production-0a494.up.railway.app/")

# Ruta de destino del formulario de asistencia (por defecto QR general)
# Nota: /auto/abrir/ es un "launcher" que abre el flujo en una pestaña creada por JS.
DEST_PATH = os.getenv("APP_ENTRY_PATH", "/auto/abrir/")

url = f"{BASE_URL.rstrip('/')}{DEST_PATH}"

img = qrcode.make(url)
img.save("qr_asistencia.png")
