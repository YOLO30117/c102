import os
import shutil

from_dir = "assets"
to_dir = "Krish_Images"

listOfFiles = os.listdir(from_dir)
#print(listOfFiles)
for i in listOfFiles:
    name,ext = os.path.splitext(i)
    #print(name)
    #print(ext)

    if ext == '':
        continue
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        p1 = from_dir + "/" + i
        p2 = to_dir + "/" + "my pics"
        p3 = to_dir + "/" + "my pics" + "/" + i
        #print(p1)
        ##print(p2)
        print(p3)
        if os.path.exists(p2):
            print("Moving " + i + ".....")
            shutil.copy(p1,p3)
        else:
            os.makedirs(p2)  
            print("Moving " + i + ".....")
            shutil.copy(p1,p3)  

        

