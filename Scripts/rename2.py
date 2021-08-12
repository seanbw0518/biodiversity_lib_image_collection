import os

imageDir = "D:\OneDrive\Documents\Programming\Python\imageDL\Cropped & Cleaned\Plants"

prev_id = "none"
i = 0

# rename files like "{number} - crop{number}.jpg"

for img in os.listdir(imageDir):
    imgId = img.split(" - ")[0]

    print(img)
    print(imgId)
    if prev_id in img:
        i += 1
        os.rename(imageDir + "\\" + img, imageDir + "\\" + imgId + "_" + str(i) + ".jpg")
    else:
        i = 0
        os.rename(imageDir + "\\" + img, imageDir + "\\" + imgId + "_" + str(i) + ".jpg")

    prev_id = imgId
	

# rename files like "{number}_{number}.jpg"
"""
for img in os.listdir(imageDir):
    imgId = img.split("_")[0]

    print(img)
    print(imgId)
    if prev_id in img:
        i += 1
        os.rename(imageDir + "\\" + img, imageDir + "\\" + imgId + "_" + str(i) + ".jpg")
    else:
        i = 0
        os.rename(imageDir + "\\" + img, imageDir + "\\" + imgId + "_" + str(i) + ".jpg")

    prev_id = imgId

"""
# fixing bad dupe finds
"""
for img in os.listdir(imageDir):
    try:
        imgId = img.split(".jpg_")[1]

        print(img)
        print(imgId)
        os.rename(imageDir + "\\" + img, imageDir + "\\" + imgId)
    except IndexError:
        continue
"""