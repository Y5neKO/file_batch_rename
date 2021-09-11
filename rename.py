import os

file_ext = ".png"
file_dir = "./"

for files in os.listdir(file_dir):
    if os.path.splitext(files)[1] == file_ext:  # 要重命名的文件后缀
        filename = files[:-4]  # 去除后缀的文件名,注意后缀长度包括"."
        filename_new = filename
        filename_len = len(filename)
        s = 8 - filename_len  # 编号的总长度，少则补零
        for re in range(0, s + 1):
            filename_new = "0" + filename_new
        os.rename(filename + file_ext, filename_new + file_ext)
