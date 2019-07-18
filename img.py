from PIL import Image
from logs import file_on

def img_on(img):
    image = Image.open('1.png')

    file_on("读取了图片 %s" % img)
    image.format, image.size, image.mode('JPEG', (500, 750),  'RGB')
    image.show()
    file_on("图片成功展示" )