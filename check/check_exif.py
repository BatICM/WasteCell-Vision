from PIL import Image


image_path = r"D:\battery_ai\battery\IMG_3641.JPG"


img = Image.open(image_path)


print("图片尺寸:")
print(img.size)


print("EXIF方向:")
print(img.getexif().get(274))
