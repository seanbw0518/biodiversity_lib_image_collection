import os

imageDir = "D:\OneDrive\Documents\Programming\Python\imageDL\Images"

urlFile = open("D:\OneDrive\Documents\Programming\Python\imageDL"+"/imageUrls.txt","r")
rows = urlFile.read().split("\n")

for filename in os.listdir(imageDir):
    if "i" in filename:
        print(filename)
        num = filename[1:]
        num = num[:-4]
        print(num)

        idNum = rows[int(num)-1][46:]

        print(idNum)
        try:
            os.rename(imageDir + "\\" + filename, imageDir + "\\" + idNum + ".jpg")
        except:
            print("already there?")