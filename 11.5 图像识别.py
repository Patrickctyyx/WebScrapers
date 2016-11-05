from PIL import Image, ImageFilter

logo = Image.open('logo.jpg')
blurryLogo = logo.filter(ImageFilter.GaussianBlur)
blurryLogo.save('logo_blurred.jpg')
blurryLogo.show()
