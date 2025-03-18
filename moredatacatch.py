import os
from ultralytics import YOLO

# 加载训练好的模型
model = YOLO('D:\\yolov8.2\\runs\\detect\\train7\\weights\\best.pt')

# 图片文件夹路径
image_folder = r"C:\Users\CAODONGHAO\Desktop\newdata\cdh_tea0001-0150"

# 获取文件夹中的所有图片
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png'))]

# 逐一处理每一张图片
for image_file in image_files:
    # 生成图片路径
    image_path = os.path.join(image_folder, image_file)
    
    # 读取图片进行预测
    results = model(image_path)
    
    # 获取检测框（boxes）数据
    boxes = results[0].boxes  # 获取第一个图片的检测框数据

    # 生成对应的 txt 文件
    txt_filename = os.path.splitext(image_file)[0] + ".txt"
    txt_filepath = os.path.join(image_folder, txt_filename)
    
    with open(txt_filepath, "w") as file:
        for box in boxes:
            # 提取坐标和类别
            xmin, ymin, xmax, ymax = box.xywh[0]  # 获取框的坐标（xywh 格式）
            class_id = int(box.cls[0])  # 获取类别 ID
            
            # 根据类别ID来设置对应的标签（0-3）
            if class_id == 0:
                label = "1to2day"
            elif class_id == 1:
                label = "2to4day"
            elif class_id == 2:
                label = "4to7day"
            elif class_id == 3:
                label = "7plusday"
            else:
                continue  # 如果类标签不在 0-3 之间，则跳过

            # 写入 txt 文件，格式：类标签 xmin ymin xmax ymax
            file.write(f"{class_id} {xmin} {ymin} {xmax} {ymax}\n")

    print(f"Processed {image_file}, results saved in {txt_filename}")
