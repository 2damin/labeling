import cv2
import os
import os.path
import csv
import pathlib
import random
import copy

imageDir = "C:/Users/Damin/Desktop/saeronDeeplearning/data/addedData/08258bb18"
#patchImageDir = "./croppedImage/1_3"

def saveCroppedImage(imagePath, y1, y2, x1, x2, i):
    image = cv2.imread(imagePath)
    crop = image[y1:y2, x1:x2]
    """
    cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("image", crop)
    cv2.waitKey()
    """
    name = "C:\\Users\\Damin\\Desktop\\saeronDeeplearning\\data\\addedData\\tmp" + "/" + "08258BB18_{}".format(i) + ".png"
    cv2.imwrite(name, crop)

def drawRectangle(image, background, x1, y1, x2, y2):

    height = y2 - y1
    width = x2 - x1

    image[y1 : y2+1, x1 : x2+1] = background[0:height+1, 0:width+1]
    """
    cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("image", image)
    cv2.waitKey()
    """

def insertPatch(imagePath, patchImagePath, patch_w, patch_h, x1, y1, index):

    image = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
    patchImage = cv2.imread(patchImagePath, cv2.IMREAD_GRAYSCALE)

    image[y1 : y1+patch_h, x1 : x1 + patch_w] = patchImage[0: patch_h, 0 : patch_w]

    """
    cv2.namedWindow("insertedImage", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("insertedImage", image)
    cv2.waitKey()
    """
    name = './croppedImage/1_09058D' + "/" + "1_09058D_{}".format(index) + ".png"
    cv2.imwrite(name, image)

image_path_list = []
patchImage_path_list = []
valid_image_extensions = [".png"]
valid_image_extensions = [item.lower() for item in valid_image_extensions]
for file in os.listdir(imageDir):
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_image_extensions:
        continue
    image_path_list.append(os.path.join(imageDir, file))

"""
for file in os.listdir(patchImageDir):
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_image_extensions:
        continue
    patchImage_path_list.append(os.path.join(patchImageDir, file))
"""

print(len(image_path_list))
print(image_path_list)
print(len(patchImage_path_list))
print(patchImage_path_list)
os.system("pause")
ii = 0

for imagePath in image_path_list:
    print(imagePath)

    saveCroppedImage(imagePath, 492,639,660,983, ii)

    #insertPatch(imagePath,patchImage_path_list[ii],39, 49, 900,572, ii)


    #image = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
    #background = image[100:161,3:64]

    #drawRectangle(image, background, 91,21,107,65)
    #drawRectangle(image, background, 31,21,48,65)
    #drawRectangle(image, background, 72,20,86,65)
    #drawRectangle(image, background, 140, 52, 164, 85)

    """
    cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("image", image)
    cv2.waitKey()
    """

    #name = "C:\\Users\\Damin\\Desktop\\saeron_deeplearning\\data\\tmp2" + "/" + "1_09058D_{}".format(ii) + ".png"
    #cv2.imwrite(imagePath, image)
    ii = ii + 1


