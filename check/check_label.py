import os
import json
import random
from PIL import Image, ImageOps
import matplotlib.pyplot as plt


# 数据路径
data_dir = r"D:\battery_ai\battery"


# 保存检查结果
save_dir = r"/check_result"

os.makedirs(save_dir, exist_ok=True)


# 找所有图片
multi_images = []


for file in os.listdir(data_dir):

    if file.endswith(".json"):

        json_path = os.path.join(data_dir,file)

        with open(json_path,"r",encoding="utf-8") as f:
            data=json.load(f)


        if len(data["shapes"]) >= 3:

            image_name = file.replace(".json",".jpg")

            multi_images.append(image_name)


# 随机抽10张
sample_images=random.sample(multi_images,10)


for image_name in sample_images:

    print("正在检查:", image_name)


    # 图片路径
    image_path = os.path.join(data_dir, image_name)


    # json名字
    json_name = os.path.splitext(image_name)[0] + ".json"

    json_path = os.path.join(data_dir, json_name)


    # 如果没有json，跳过
    if not os.path.exists(json_path):
        print("没有JSON:", json_name)
        continue



    # 打开图片
    img = Image.open(image_path)

    # 处理手机EXIF旋转
    img = ImageOps.exif_transpose(img)



    # 打开json
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)



    plt.figure(figsize=(10,10))

    plt.imshow(img)



    # 画polygon
    for shape in data["shapes"]:

        points = shape["points"]

        x=[]
        y=[]

        for p in points:
            x.append(p[0])
            y.append(p[1])


        # 闭合
        x.append(x[0])
        y.append(y[0])


        plt.plot(x,y)


    plt.axis("off")


    # 保存
    save_path = os.path.join(save_dir,image_name)

    plt.savefig(
        save_path,
        bbox_inches="tight",
        dpi=200
    )


    plt.close()



print("检查完成")
