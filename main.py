import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=50,
                   border=2)

qr.add_data("www.paudelnabin.com.np")
qr.make(fit=True)

img = qr.make_image(fill_color="black",  back_color="white")
img.save("QR.svg")