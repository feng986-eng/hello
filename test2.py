import os

folder_path = "./photos"  # 目标文件夹路径（换成你的文件夹）

老子不信了

for filename in os.listdir(folder_path):
    old_path = os.path.join(folder_path, filename)
    if os.path.isfile(old_path):  # 只处理文件，不处理子文件夹
        new_filename = prefix + filename
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)  # 重命名文件
        print(f"已重命名：{filename} -> {new_filename}")
  print(f"已重命名：{filename} -> 无所谓{new_filename}")
