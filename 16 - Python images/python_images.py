# pip install pillow
from PIL import Image

tent = Image.open('../example.jpg')
print(type(tent))

# opening the image
# tent.show()

# check image size
print(tent.size)
# check image name
print(tent.filename)

print(tent.format_description)

