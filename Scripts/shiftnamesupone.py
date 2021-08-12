import os

imageDir = "D:\OneDrive\Documents\Programming\Python\imageDL\Images"

urlFile = open("D:\OneDrive\Documents\Programming\Python\imageDL"+"/imageUrls.txt","r")
rows = urlFile.read().split("\n")

for filename in os.listdir(imageDir):
    print(filename)
    if "img" in filename:
        num = filename[3:]
        num = num[:-4]
        newNum = int(num)+1
        print(num,newNum)
        os.rename(imageDir + "\\" + filename, imageDir + "\\" + "i"+str(newNum) + ".jpg")