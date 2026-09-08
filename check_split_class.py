import os


# YOLO数据集路径
dataset_dir = r"D:\battery_ai\dataset"


# 原始有电池文件夹
battery_dir = r"D:\battery_ai\raw_data\battery"


# 三个划分
splits = ["train", "val", "test"]



# 统计每个集合

for split in splits:


    image_dir = os.path.join(
        dataset_dir,
        "images",
        split
    )


    battery_count = 0
    no_battery_count = 0


    for image_name in os.listdir(image_dir):


        # 只处理图片
        if not image_name.lower().endswith(
                (".jpg",".jpeg",".png")):
            continue



        # 去掉后缀
        name = os.path.splitext(image_name)[0]


        # 找对应json

        json_path = os.path.join(
            battery_dir,
            name + ".json"
        )


        if os.path.exists(json_path):

            battery_count += 1

        else:

            no_battery_count += 1



    print("====================")
    print(split)
    print("====================")

    print("有电池:",battery_count)

    print("无电池:",no_battery_count)

    print("总数:",
          battery_count + no_battery_count)