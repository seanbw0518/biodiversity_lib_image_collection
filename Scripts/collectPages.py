from urllib.request import urlopen
import json

AUTH_KEY = "73c01f7d-e4b1-46bf-93e3-fca1e56e51ee"

inFile = open("itemUrls-ALL.txt", "r+")
outFile = open("imageUrls-ALL.txt", "a+")

inFileLineNum = sum(1 for line in open("itemUrls-ALL.txt", "r"))

c = 0

for line in inFile:

    try:
        itemId = line[41:-1]
        print("Getting page data...")
        urlData = urlopen(
            "https://www.biodiversitylibrary.org/api3?op=GetItemMetadata&id=" + itemId + "&pages=t&ocr=f&parts=f&apikey=" + AUTH_KEY + "&format=json")
        jsonText = json.loads(urlData.read())
        pages = jsonText["Result"][0]["Pages"]
        pageTypes = []

        print("checking pages...")
        for page in range(len(pages)):
            for pageType in range(len(pages[page]["PageTypes"])):
                pageTypes.append(pages[page]["PageTypes"][pageType]["PageTypeName"])
            if " Illustration" in pageTypes or "Illustration" in pageTypes or "Drawing" in pageTypes or " Drawing" in pageTypes or "Foldout" in pageTypes or " Foldout" in pageTypes:
                print("Relevant Page Found!")
                outFile.writelines(itemId + " : " + pages[page]["FullSizeImageUrl"] + "\n")

            pageTypes.clear()

        print("PROGRESS: " + str(round((c / inFileLineNum) * 100, 3)) + "%")
        c += 1
    except:
        print("oopsy poopsy")

outFile.close()
