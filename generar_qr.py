import qrcode

# URL fija a la que debe apuntar el QR de asistencia general
# Si quieres cambiarla en el futuro, solo edita este string.
url = "https://web-production-0a494.up.railway.app"

img = qrcode.make(url)
img.save("qr_asistencia.png")
