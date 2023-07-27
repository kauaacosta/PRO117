import os
import cv2

Images = []
path = "Images"


for file in os.listdir(path):
    name, extension = os.path.splitext(file)

    if extension.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
        file_name = os.path.join(path, file)
        print(file_name)
        Images.append(file_name)

count = len(Images)

frame = cv2.imread(Images[0])
height, width, channels = frame.shape
size = (width, height)
print(size)

video_name = "Project.avi"
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
fps = 0.8
out = cv2.VideoWriter(video_name, fourcc, fps, size)

for i in range(count):
    frame = cv2.imread(Images[i])
    out.write(frame)

out.release()

print("Concluído")