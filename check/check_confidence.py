from ultralytics import YOLO
import csv
import os


model = YOLO(
    "D:/battery_ai/runs/segment/train-3/weights/best.pt"
)


results = model.predict(
    source="D:/battery_ai/dataset/images/test",
    save=False
)


with open("confidence.csv", "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow(
        ["image", "num_objects", "max_conf", "min_conf"]
    )

    for r in results:

        name = os.path.basename(r.path)

        if r.boxes is not None and len(r.boxes):

            confs = r.boxes.conf.cpu().numpy()

            writer.writerow(
                [
                    name,
                    len(confs),
                    max(confs),
                    min(confs)
                ]
            )

        else:

            writer.writerow(
                [
                    name,
                    0,
                    None,
                    None
                ]
            )
