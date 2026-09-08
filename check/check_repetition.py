import os


battery_dir = r"D:\battery_ai\raw_data\battery"
no_battery_dir = r"D:\battery_ai\raw_data\no_battery"


battery_names = set()
no_battery_names = set()


for file in os.listdir(battery_dir):

    if file.lower().endswith(".jpg"):
        battery_names.add(file)


for file in os.listdir(no_battery_dir):

    if file.lower().endswith(".jpg"):
        no_battery_names.add(file)



same = battery_names & no_battery_names


print("重复文件名数量:",len(same))

print(same)
