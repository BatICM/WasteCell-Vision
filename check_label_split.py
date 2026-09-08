import os


label_root = r"D:\battery_ai\dataset\labels"


for split in ["train", "val", "test"]:

    path = os.path.join(
        label_root,
        split
    )


    txts = [
        f for f in os.listdir(path)
        if f.endswith(".txt")
    ]


    print("================")
    print(split)
    print("================")

    print("txt数量:", len(txts))