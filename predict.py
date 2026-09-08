from ultralytics import YOLO

# 加载训练好的模型
model = YOLO(
    r"D:\battery_ai\runs\segment\train\weights\best.pt"
)

# 测试集预测
results = model.predict(
    source="D:/battery_ai/dataset/images/test",
    save=True,
    conf=0.576
)