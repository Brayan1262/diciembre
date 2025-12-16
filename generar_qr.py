import os
import qrcode

def normalize_base_url(url: str) -> str:
    url = (url or "").strip()
    return url.rstrip("/")


# Lee la URL base pública de la app desde variables de entorno
# IMPORTANTE: Debe incluir esquema para que el celular abra el link al escanear.
# Ejemplos:
# - Local: http://127.0.0.1:8000
# - Railway: https://<tu-subdominio>.up.railway.app
BASE_URL = normalize_base_url(
    os.getenv("PUBLIC_BASE_URL")
    or os.getenv("APP_URL")  # compatibilidad
    or "http://127.0.0.1:8000"
)

# Ruta de destino al escanear (por defecto QR general)
DEST_PATH = (os.getenv("APP_ENTRY_PATH", "/auto/") or "/auto/").strip()
if not DEST_PATH.startswith("/"):
    DEST_PATH = "/" + DEST_PATH

url = f"{BASE_URL}{DEST_PATH}"

img = qrcode.make(url)
img.save("qr_asistencia.png")
