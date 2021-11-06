

from exif import Image
img_path = './IMG_2165.HEIC'
with open(img_path, 'rb') as src:
    img = Image(src)
    print (src.name, img)  
var = img.has_exif
print(var)