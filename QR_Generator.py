import qrcode

user_data = input("Enter the URL or text you want to turn into a QR code: ")

img = qrcode.make(user_data)

img.save("my_new_qrcode.png")

print("All done! Your QR code is saved.")