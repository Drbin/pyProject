from PIL import Image
from logs import file_on

def img_on():
    image = Image.open('1.png')
    image.format, image.size, image.mode('JPEG', (500, 750),  'RGB')
    image.show()