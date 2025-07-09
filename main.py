import qrcode

data = input("Enter the text or URL to encode in a QR Code:")

qr = qrcode.QRCode(
    version = 1,
    box_size = 10, #15x15 pixels per box
    border = 5
)

# Add the input data to the QR image
qr.add_data(data)
qr.make(fit = True)

#create the QR image
img = qr.make_image(fill_color = "Black", back_color = "White") 
filename = "qr_code.png"
img.save(filename)      #save the QR image 

#confirm QR generation
print(f"QR Code generated and saved as {filename}")