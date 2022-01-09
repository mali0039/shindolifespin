import cv2 as cv
import numpy as np
import pyautogui as pag
import time
import os


def findImg(needle) :
    method = cv.TM_CCOEFF_NORMED
    needle_img = cv.imread(needle, 0)
    # h, w = needle_img.shape
    haystack_img = cv.imread('screen.png', 0)
    # img2 = haystack_img.copy()

    result = cv.matchTemplate(haystack_img, needle_img, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    # print(max_val)
    # location = max_loc
    # bottom_right = (location[0] + 90, location[1] + 90)
    # cv.rectangle(img2, location, bottom_right, 255, 5)
    # cv.imshow('Match', img2)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    # get the best match position
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print('Best match top left position: %s' % str(max_loc))
    print('Best match confidence: %s' % max_val)
     
    return max_val

def getAllBloodlines():
    listOfFile = os.listdir('bloodlines')
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        if (not entry.startswith(".")):
            # Create full path
            fullPath = os.path.join('bloodlines', entry)
            # If entry is a directory then get the list of files in this directory 
            allFiles.append(fullPath)
    
    return allFiles
                
def spin():
    allFiles = getAllBloodlines()
    foundBloodline = False
    while (not foundBloodline):
        # pag.moveTo(173,449)
        # pag.sleep(0.5)
        # pag.click(173,449)
        # time.sleep(1)
        # pag.moveTo(800, 0)
        # pag.sleep(1)
        # pag.click(800, 0)
        pag.moveTo(1758,448)
        pag.click(1758,448)
        time.sleep(1)
        pag.click(1758,448)
        time.sleep(1)
        pag.moveTo(173,449)
        pag.sleep(0.5)
        pag.click(173,449)
        time.sleep(10)
       
        # pag.click(173,449)
        # pag.moveTo(800, 0)
        # pag.sleep(1)
        # pag.click(800, 0)
        # time.sleep(10)
        screenshot = pag.screenshot('screen.png')
        for bloodline in allFiles:
            if(bloodline == "bloodlines/S+") or bloodline =="bloodlines/Rnadom":
                continue
            else:
                print(bloodline)
                if (findImg(bloodline) > 0.98):
                    foundBloodline = True
    print("Found")  

spin()
