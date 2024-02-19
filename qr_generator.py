import qrcode
from PIL import  Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data('https://www.instagram.com/mdjr_0_09/?hl=en')
qr.make(fit=True)
img=qr.make_image(fill_color='orange',back_color="white")
img.save('insta_qr2.png')
