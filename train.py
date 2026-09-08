from ultralytics import YOLO


def main():

    model = YOLO("yolo26n-seg.pt")


    model.train(
        data=r"D:\battery_ai\dataset\battery.yaml",
        epochs=100,
        imgsz=800,
        batch=8,
        device=0,
        hsv_h = 0.015,
        hsv_s = 0.7,
        hsv_v = 0.4
    )


if __name__ == "__main__":
    main()