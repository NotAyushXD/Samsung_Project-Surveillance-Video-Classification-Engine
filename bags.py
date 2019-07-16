import cv2
import os
import shutil

path = '/home/ayush/Desktop/Multiple Instance learning/video_data'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file:
            files.append(os.path.join(r, file))
i = 0
pa = '/home/ayush/Desktop/Multiple Instance learning/'
a = None
for f in files:
    if i % 30 == 0:
        a = pa+str(i)
        print(a)
        os.chdir(pa)
        os.mkdir(pa+str(i))
        os.chdir(pa+str(i))
    cwd = os.getcwd()
    # print(cwd)
    print(pa+"video_data/"+f)
    i+=1
    shutil.move(str(f), a)
