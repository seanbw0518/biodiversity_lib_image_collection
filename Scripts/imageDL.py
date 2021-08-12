import requests
import cv2
import os
import threading

DATA_DIR = "D:/OneDrive/Documents/Programming/Python/imageDL"

urlFile = open(DATA_DIR + "/imageUrls-ALL.txt", "r+")
rows = urlFile.read().split("\n")
numOfRows = len(rows)

c = 0

# loop the URLs
for line in rows:

    url = line.split(" : ")[1]

    try:
        imagePath = DATA_DIR + "/test/" + url[46:] + ".jpg"

        # try to download the image
        response = requests.get("https://www.biodiversitylibrary.org/pagethumb/"+url[46:], timeout=50)
        # outFile name
        file = open(imagePath, "wb")
        print(response)
        file.write(response.content)
        file.close()

        # try to load the image with cv2
        # if unsuccessful, delete image
        try:
            image = cv2.imread(imagePath)
            if image is None:
                print("STATUS - FAILURE! Image error! Deleting.")
                os.remove(imagePath)
                c+=1
            else:

                """# resize images
                img = cv2.imread(imagePath, cv2.IMREAD_UNCHANGED)
                newWidth = ((img.shape[1] - 0) / (10000 - 0)) * 2000
                newHeight = ((img.shape[0] - 0) / (10000 - 0)) * 2000

                cv2.imwrite(imagePath, cv2.resize(img, (int(newWidth), int(newHeight))))"""
                c += 1

        except Exception as e:
            print("STATUS - FAILURE! Image error! Deleting.")
            os.remove(imagePath)
            c+=1

        # completion % updates
        file.close()
        print("PROGRESS: " + str(round((c / (numOfRows)) * 100, 3)) + "%")

    # handle if any exceptions are thrown during the download process
    except Exception as e:
        print(e)
        print("STATUS - Unable to download!")