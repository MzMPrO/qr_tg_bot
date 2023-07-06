import qrcode
# pip install qrcode
for i in range(1, 1000):
    # Generate a QR code
    data = f"https://t.me/moderator_MzMPrObot?start={i}"  # Replace with your desired data (URL, text, etc.)
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image
    qr_filename = f'{i}.png'  # Replace with your desired filename
    qr_image.save(qr_filename)
