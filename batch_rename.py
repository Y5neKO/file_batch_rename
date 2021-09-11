import os

file_ext = ".png"                         # 要重命名的文件后缀
file_dir = "./"                           # 文件路径，推荐为当前目录，其他目录会报错
num = 8                                   # 编号的总位数，少则往前补零

for files in os.listdir(file_dir):
    if os.path.splitext(files)[1] == file_ext:
        filename = files[:-4]             # 去除后缀的文件名,注意后缀长度包括"."
        filename_new = filename
        filename_len = len(filename)
        s = num - filename_len            # 需要往前补零的个数
        for re in range(0, s + 1):
            filename_new = "0" + filename_new
        os.rename(filename + file_ext, filename_new + file_ext)
