import os 
import cv2

path = "./Images"

image = []
listOfFiles = os.listdir(path)

for file in listOfFiles:
    name, ext = os.path.splitext(file)
    #print(file)
    if ext in [".gif", ".png", ".jpg", ".jpeg"]:
        file_name = path+"/"+file
        #print(file_name)
        image.append(file_name)
 
print(image)
count = len(image)
frame = cv2.imread(image[0])
width,height,channels = frame.shape
size = (width,height) 

out = cv2.VideoWriter("project.avi",cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

for i in range(0, count-1):
    frame = cv2.imread(image[i])
    out.write(frame)
    
out.release()
print("Concluido")
