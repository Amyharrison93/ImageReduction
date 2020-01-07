#!/usr/bin/env python
import cv2 as cv
import tkinter as tk
import os

#-----------------------------------------------------------------------
#		GUI v0.1
# 		provides a GUI for interaction
#		started: 07/01/2020
#		Comp tested: 07/01/2020
#		Author: AH
#-----------------------------------------------------------------------
def GUI():
	#get the directory
	strPath = os.path.dirname(os.path.abspath(__file__))
	
	root = tk.Tk()
	#path textbox
	tbPath = tk.Text(root, height=1, width=60)
	tbPath.pack()
	tbPath.insert(tk.END, strPath)

	#save path textbox
	tbSave = tk.Text(root, height=1, width=60)
	tbSave.pack()


	#image height textbox, image width textbox
	tbHeight = tk.Text(root, height=2, width=20)
	tbHeight.pack()
	tbHeight.insert(tk.END, "1080")
	tbWidth = tk.Text(root, height=2, width=20)
	tbWidth.pack()
	tbWidth.insert(tk.END, "1920")

	#get file data
	strPath = tbPath.get('1.0', 'end-1c')
	strSave = tbSave.get('1.0', 'end-1c')
	arryOutSize = (int(tbHeight.get('1.0', 'end-1c')), int(tbWidth.get('1.0', 'end-1c')))

	print((arryOutSize[0]))

	tk.mainloop()

	return strPath, strSave, arryOutSize

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
	strPath, strSave, arryOutSize = GUI()
	print(strPath, strSave, arryOutSize)

	root = tk.Tk()
	#save button
	bttnSave = tk.Button(root, text="Save", command = ResizeImage(strPath, strSave, arryOutSize))
	bttnSave.pack()

	strPath = "C:\\Users\\P10499583\\Downloads\\parking1.png"
	strSave = "C:\\Users\\P10499583\\Downloads\\parkingSmaller2.png"
	arryOutSize = 1080, 1920

	ResizeImage(strPath, strSave, arryOutSize)
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

