import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data("https://www.youtube.com/")
qr.make(fit=True)

# IMPORTANT: convert("RGB") use kar
img = qr.make_image(fill_color="blue", back_color="yellow").convert("RGB")

img.save("ganu_color.png")