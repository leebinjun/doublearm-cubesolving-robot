import os
import cv2

path = "./data"
files = os.listdir(path) 
# print(files)
cnt = 0
for f in files: 
    print(f)
    data_file_path = path+'/'+f 
    # img = cv2.imread(data_file_path)
    # img_resize = cv2.resize(img, (300, 300))
    # cv2.imwrite(path+'/'+f+'/'+"{:04d}.jpg".format(cnt), img_resize)
    newname = path+'/'+"{:04d}.jpg".format(cnt)
    os.rename(data_file_path, newname)
    cnt += 1
    #     if cnt == 2:
    #         break
    # break