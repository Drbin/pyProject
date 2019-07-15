from PIL import Image
from logs import file_on

def img_on(img):
    file_on("读取了图片 %s" % img)
    image = Image.open('1.png')
    image.format, image.size, image.mode('JPEG', (500, 750),  'RGB')
    image.show()