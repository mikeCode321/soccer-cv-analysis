from ultralytics import YOLO

model = YOLO('models/best.pt')  # Load a pretrained YOLOv8 model
model.info()

results = model.predict('input_videos/08fd33_4.mp4', save=True)
print(results[0]) # first frame 

print("==========================================")
for box in results[0].boxes:
    print(box)

