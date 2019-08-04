from PIL import Image

image = Image.open('1.png')
image.format, image.size, image.mode('JPEG', (500, 750),  'RGB')
image.show()