#!/usr/bin/env python
import cv2 as cv
import tkinter as tk

#-----------------------------------------------------------------------
#		resize v0.1
# 		loads image and resizes
#		started: 07/01/2020
#		Comp tested: 07/01/2020
#		Author: AH
#-----------------------------------------------------------------------
def ResizeImage(strPath, strSave, arryOutSize):
	image = cv.imread(strPath)
	image = cv.resize(image, arryOutSize)
	cv.imwrite(strSave, image)

#-----------------------------------------------------------------------
#		Main v0.1
# 		main file loop
#		started: 07/01/2020
#		Comp tested: 07/01/2020
#		Author: AH
#-----------------------------------------------------------------------
def main(args):
	strPath = "C:\\Users\\P10499583\\Downloads\\parking1.png"
	strSave = "C:\\Users\\P10499583\\Downloads\\parkingSmaller2.png"
	arryOutSize = 1080, 1920

	ResizeImage(strPath, strSave, arryOutSize)
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

