from PIL import Image

image = Image.open('./res/guido.jpg')
image.format, image.size, image.mode('JPEG', (500, 750),  'RGB')
image.show()