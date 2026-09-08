import os
from PIL import Image
from collections import Counter


image_dirs = {
    "有电池": r"D:\battery_ai\battery",
    "无电池": r"D:\battery_ai\no_battery"
}


for name, image_dir in image_dirs.items():

    size_count = Counter()
    total_image = 0


    for file in os.listdir(image_dir):

        if file.lower().endswith((".jpg", ".jpeg", ".png")):

            total_image += 1

            image_path = os.path.join(image_dir, file)

            img = Image.open(image_path)

            size_count[img.size] += 1


    print("\n===================")
    print(name)
    print("===================")

    print("图片数量:")
    print(total_image)

    print("\n尺寸统计:")

    for size, count in size_count.items():
        print(size, ":", count)
