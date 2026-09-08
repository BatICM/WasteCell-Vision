import cv2
import os


# 图片路径
image_path = r"D:\battery_ai\raw_data\battery\IMG_3641.JPG"

# YOLO标签路径
label_path = r"D:\battery_ai\IMG_3641.txt"



# 读取图片
img = cv2.imread(image_path)

if img is None:
    print("图片读取失败")
    exit()


# 获取图片尺寸
height, width = img.shape[:2]

print("图片尺寸:")
print(width, height)



# 打开YOLO标签

with open(label_path, "r") as f:

    lines = f.readlines()



for line in lines:


    data = line.strip().split()


    # 第一个是类别
    class_id = int(data[0])


    # 后面全部是坐标
    points = data[1:]


    polygon = []


    # 每两个数字组成一个点

    for i in range(0, len(points), 2):

        x = float(points[i])
        y = float(points[i+1])


        # YOLO坐标还原成像素坐标

        x_pixel = int(x * width)
        y_pixel = int(y * height)


        polygon.append(
            [x_pixel, y_pixel]
        )


    # 转numpy格式

    import numpy as np

    polygon = np.array(
        polygon,
        np.int32
    )


    polygon = polygon.reshape((-1,1,2))


    # 绘制polygon

    cv2.polylines(
        img,
        [polygon],
        True,
        (0,255,0),
        5
    )



# 缩小显示
scale = 0.25

show_img = cv2.resize(
    img,
    None,
    fx=scale,
    fy=scale
)


cv2.imshow(
    "YOLO Seg Check",
    show_img
)

cv2.waitKey(0)

cv2.destroyAllWindows()
