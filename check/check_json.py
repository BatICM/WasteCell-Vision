import os
import json
from collections import Counter


json_dir = r"D:\battery_ai\raw_data\battery"


class_count = Counter()
object_count = Counter()

total_json = 0


for file in os.listdir(json_dir):

    if file.endswith(".json"):

        total_json += 1

        path = os.path.join(json_dir,file)

        with open(path,"r",encoding="utf-8") as f:
            data=json.load(f)


        shapes=data.get("shapes",[])


        object_count[len(shapes)] += 1


        for shape in shapes:
            class_count[shape["label"]] += 1



print("JSON数量:")
print(total_json)


print("\n类别统计:")
for k,v in class_count.items():
    print(k,":",v)


print("\n每张图片目标数量:")
for k,v in object_count.items():
    print(k,"个目标:",v,"张")
