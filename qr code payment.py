import qrcode
from PIL import Image

# Define the UPI payment link
upi_link = "upi://pay?pa=abc@upi&pn=Recipient%20Name&am=10.00&cu=INR&tn=Payment%20for%20goods"

# Generate the QR code image
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(upi_link)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Display the QR code image in a new window
img.show()
