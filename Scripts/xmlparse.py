import xml.etree.ElementTree as ET
import json

NAMESPACE = {"xmlns": "xlink=""http://www.w3.org/1999/xlink"""}

print("parsing tree")
tree = ET.parse('bhlintitem.mods.xml')
root = tree.getroot()

numOfChildren = sum(1 for _ in root.iter("*"))
print(numOfChildren)

file = open("itemUrls-ALL.txt", "w")

c = 0
for child in root:
    type = child.find("{http://www.loc.gov/mods/v3}typeOfResource")
    if "software" not in type.text:
        itemType = type.text
        uri = ""

        for url in child.find("{http://www.loc.gov/mods/v3}location"):
            if url.attrib == {'access': 'raw object', 'usage': 'primary'}:
                uri = url.text
                file.write(uri + "\n")

    print("PROGRESS: " + str(round((c / numOfChildren) * 100, 2)) + "%")
    c += 1

print("Done! - Saving...")
file.close()
