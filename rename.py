import os

# 图片文件夹路径
folder_path = r'C:\Users\CAODONGHAO\Desktop\newdata\txt_new'

# 获取文件夹内所有文件
files = os.listdir(folder_path)

# 过滤出图片文件（假设是 .jpg 或 .png 后缀）
image_files = [f for f in files if f.lower().endswith(('.txt', '.png'))]

# 从01616开始命名
start_number = 1616

for i, filename in enumerate(image_files):
    # 获取文件扩展名
    file_extension = os.path.splitext(filename)[1]
    
    # 新文件名：01616、01617、01618等，保持5位数格式
    new_filename = f"{start_number + i:05d}{file_extension}"
    
    # 构建完整路径
    old_file_path = os.path.join(folder_path, filename)
    new_file_path = os.path.join(folder_path, new_filename)
    
    # 重命名文件
    os.rename(old_file_path, new_file_path)

    print(f"Renamed: {filename} -> {new_filename}")
