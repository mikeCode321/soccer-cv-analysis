# Advanced Soccer Computer Vision Analysis

Computer vision: is able to draw a bounding box around an object and identify it frame by frame (image). YOLO state of the art right now via ultralytics


MODEL: YOLOv8x


750 frames in our input video (30 seconds)


x, y , w, h -> bounding box

x1, y1, x2, y2 -> bounding box (what we are using)

YOLO class names:
names: {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'}


We are focused on class names: [0 and 32]

We need to refine the detection to not get people in the stands or outside the pitch. 

We also need to refine the detection for the soccer ball


reference 30:48 in video maybe showing how to download and use the model he already trained


download the best.pt and place at the root models/best.pt 

use best model YOLO('models/best.pt')


Preperation for the data such as cutting matches into bite size pieces, labeling and annotating each frame (weeks long process)
Then training a object detection algo on each annotated frame (CNN Algo)
Then each frame is put together to make a video with object detection and bounding boxes on each frame
Then by using frame to frame calculations we can figure out certain statistics and metrics 

<!-- 
5. Possible Enhancements for Accuracy
Camera Calibration: If the camera's focal length and field of view are known, you can use camera calibration techniques to more accurately convert pixel distances to real-world distances, especially for videos with complex perspectives.

Use of GPS Data: If the video includes GPS data (e.g., from a car's camera system), you can directly calculate speed using the GPS coordinates of the vehicle between frames.

Multiple Frames Averaging: To reduce errors and noise, you can average the speeds calculated from several frames, rather than relying on a single frame-to-frame calculation.

6. Considerations
Perspective Distortion: If the object is moving toward or away from the camera, the perceived speed can be distorted due to perspective. It's important to account for this, and techniques like perspective correction or knowing the depth of the scene (using stereo cameras or depth sensors) can help.

Frame Resolution: The higher the resolution of the video, the more accurate your pixel-to-meter scaling will be, as it reduces the error introduced by low-resolution images.

Occlusion: If the object gets partially or fully occluded (blocked by other objects), the tracking can fail, and you might need to implement recovery strategies like re-identification. -->

