import os


# 数据集路径
dataset_dir = r"D:\battery_ai\dataset\images"


# 三个数据集
splits = ["train", "val", "test"]



# 统计函数

def count_files(folder, suffix):

    count = 0

    for file in os.listdir(folder):

        if file.lower().endswith(suffix):

            count += 1

    return count



# 开始检查

for split in splits:


    image_dir = os.path.join(
        dataset_dir,
        "images",
        split
    )


    label_dir = os.path.join(
        dataset_dir,
        "labels",
        split
    )


    print("====================")
    print(split)
    print("====================")


    # 图片数量

    if os.path.exists(image_dir):

        image_count = count_files(
            image_dir,
            (".jpg",".jpeg",".png")
        )

    else:

        image_count = 0



    # 标签数量

    if os.path.exists(label_dir):

        label_count = count_files(
            label_dir,
            (".txt",)
        )

    else:

        label_count = 0



    print("图片数量:",image_count)

    print("标签数量:",label_count)



    if image_count == label_count:

        print("状态: 图片和标签数量一致")

    else:

        print("状态: 数量不一致，请检查")


print("====================")
print("检查完成")
