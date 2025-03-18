import cv2
from ultralytics import YOLO

# 读取视频
#input_video_path = r"D:\yolov8.2\tea_detect_using_video\teatest.mp4"
input_video_path =r"D:\yolov8.2\tea_detect_using_video\teatest.mp4"
output_video_path = "output.mp4"
cap = cv2.VideoCapture(input_video_path)

# 获取视频属性
fps = max(1, int(cap.get(cv2.CAP_PROP_FPS)))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 兼容性更好的编码格式
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

if not cap.isOpened():
    print("Error: Cannot open video file.")
    exit()

if not out.isOpened():
    print("Error: VideoWriter failed to open.")
    exit()

# 加载 YOLOv8 模型
model = YOLO('D:\\yolov8.2\\runs\\detect\\train7\\weights\\best.pt')

# 逐帧处理
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = f"{model.names[cls]} {conf:.2f}"

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    out.write(frame)
    cv2.imshow("YOLOv8 Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

