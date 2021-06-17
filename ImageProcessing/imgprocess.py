# Invokation: python3 imgprocess.py

from PIL import Image, ImageFilter

img = Image.open('./pokedox/pokemon1.jpg')

# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)

# Blurring mage
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", "png")

# Smooth Image
filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save("smooth.png", "png")

# Sharpen Image
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("sharp.png", "png")

# GrayScale Image
filtered_img = img.convert("L")
filtered_img.save("grey.png", "png")

# See Image
filtered_img.show()

# Rotate Image
rotated = filtered_img.rotate(90)
rotated.save("rotated.png", "png")

# Resize Image
resize = filtered_img.resize((100, 100))
resize.save("resized.png", "png")

# Crop Image
box = (100, 100, 600, 600)
region = filtered_img.crop(box)
region.save("cropped.png", "png")


# Thumbnail: maintains Aspect Ratio
filtered_img.thumbnail((400, 200))
filtered_img.save("thumbnail.jpg")
