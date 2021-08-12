import os
import requests
import threading

DATA_DIR = "D:/OneDrive/Documents/Programming/Python/imageDL"
URL_TO_IMAGE = "https://www.biodiversitylibrary.org/pageimage/"

low_res_image_dir = "D:\\OneDrive\\Documents\\Programming\\Python\\imageDL\\Images - Categorized\\p2"
high_res_image_dir = "D:\\OneDrive\\Documents\\Programming\\Python\\imageDL\\High-Res Images (Categorized)\\Plants\\"


class dlThread(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID

    def run(self):
        print("Starting thread " + str(self.threadID))
        dlImages(self.threadID)


def dlImages(startPoint):
    num_of_images = len(os.listdir(low_res_image_dir))
    count = 0
    print("Number of images: " + str(num_of_images))

    # loop the URLs

    for filename in os.listdir(low_res_image_dir):

        image_id = filename[:-4]
        count += 1
        perct_prog = round((count / num_of_images) * 100, 3)

        try:
            print("Downloading: " + image_id)

            # try to download the image
            response = requests.get(URL_TO_IMAGE + image_id, timeout=50)
            # outFile name
            file = open(high_res_image_dir + image_id + ".jpg", "wb")
            # print(response)
            file.write(response.content)
            file.close()

            # completion % updates
            print("PROGRESS: " + str(perct_prog) + "%, REMAINING: " + str(num_of_images - count))

        # handle if any exceptions are thrown during the download process
        except Exception as e:
            print(e)
            print("STATUS - Unable to download!")


thread0 = dlThread(0)
"""thread1 = dlThread(1)
thread2 = dlThread(2)
thread3 = dlThread(3)
thread4 = dlThread(4)
thread5 = dlThread(5)
thread6 = dlThread(6)
thread7 = dlThread(7)
thread8 = dlThread(8)
thread9 = dlThread(9)
thread10 = dlThread(10)
thread11 = dlThread(11)
thread12 = dlThread(12)
thread13 = dlThread(13)
thread14 = dlThread(14)
thread15 = dlThread(15)
"""

thread0.start()
"""thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()
thread11.start()
thread12.start()
thread13.start()
thread14.start()
thread15.start()
"""
