import xml.etree.ElementTree as ET

blackList = ["literature", "books", "medicine", "modern", "physics", "geology", "chemistry", "architecture",
           "bibliography", "manual", "newspaper",
           "psychology", "human", "paleontology", "fossil", "photography", "mathematics", "music", ]

NAMESPACE = {"xmlns": "xlink=""http://www.w3.org/1999/xlink"""}

print("parsing tree")
tree = ET.parse('bhlintitem.mods.xml')
root = tree.getroot()

numOfChildren = sum(1 for _ in root.iter("*"))
print(numOfChildren)

imagesFile = open("imagesUrls-ALL.txt", "r+")

imageCodes = []

print("making list")
for line in imagesFile:
    imageCodes.append(line.split(" : ")[0])

c = 0
for child in root:
    for url in child.find("{http://www.loc.gov/mods/v3}location"):
        if url.attrib == {'access': 'raw object', 'usage': 'primary'}:
            print(url.text[41:])
            # if already saved item
            if "88345" in imageCodes:
                print("in")
                try:
                    for subject in child.find("{http://www.loc.gov/mods/v3}subject"):
                        # if any from blacklist in subject
                        for i in blackList:
                            print(subject.text)
                            if i in subject.text:
                                print("no!")
                            else:
                                print("yes!")
                except Exception:
                    print("no subjects")
            else:
                print("not used")


    print("PROGRESS: " + str(round((c / numOfChildren) * 100, 2)) + "%")
    c += 1
