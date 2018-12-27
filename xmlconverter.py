import xml.etree.ElementTree as ET
import os, glob


def xml_convert(path):
    for xml_file in glob.glob(path + "/*.xml"):
        for imageName in glob.glob(xml_file):
            imageName = imageName.replace(path+"\\","")
            imageName = imageName.replace(".xml", ".png")

        tree = ET.parse(xml_file)
        root = tree.getroot()
        value = [root.find('filename').text]
        root.find('filename').text = str(imageName)
        #print(root.find('filename').text)
        #ET.dump(root)
        tree.write(xml_file, encoding="utf-8", xml_declaration=True)


def main():
    path = os.path.join(os.getcwd(),'annotations')
    xml_convert(path)

main()
print("convert done")

