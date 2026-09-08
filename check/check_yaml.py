import yaml


yaml_path = r"D:\battery_ai\dataset\battery.yaml"


with open(yaml_path,"r",encoding="utf-8") as f:

    data = yaml.safe_load(f)


print(data)
