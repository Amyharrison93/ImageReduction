#!/usr/bin/env python
import cv2 as cv
import tkinter as tk
import os
import numpy as np

strPath = ""
strSave = ""
arryOutSize = np.zeros(2)

#-----------------------------------------------------------------------
#		gui functionality v0.1
# 		interacts with the GUI
#		started: 07/01/2020
#		Comp tested: 07/01/2020
#		Author: AH
#-----------------------------------------------------------------------
def GUIFunc():
	#get file data
	strPath = str(tbPath.get('1.0', 'end-1c'))
	print(strPath)
	strSave = str(tbSave.get('1.0', 'end-1c'))
	intHeight, intWidth = (int(tbHeight.get('1.0', 'end-1c')), int(tbWidth.get('1.0', 'end-1c')))
	arryOutSize = intHeight, intWidth

	print(strPath, strSave, arryOutSize)
	ResizeImage(strPath, strSave, arryOutSize)

	mbMessage = tk.messagebox.showinfo("Status", "Process complete")
	tk.mainloop()

	

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
#		GUI v0.1
# 		provides a GUI for interaction
#		started: 07/01/2020
#		Comp tested: 07/01/2020
#		Author: AH
#-----------------------------------------------------------------------

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

#save button
bttnSave = tk.Button(root, text="Save", command = GUIFunc)
bttnSave.pack()

tk.mainloop()

#-----------------------------------------------------------------------
#		Main v0.1
# 		main file loop
#		started: 07/01/2020
#		Comp tested: 07/01/2020
#		Author: AH
#-----------------------------------------------------------------------
def main(args):
	print(strPath, strSave, arryOutSize)

	strPath = "C:\\Users\\P10499583\\Downloads\\parking1.png"
	strSave = "C:\\Users\\P10499583\\Downloads\\parkingSmaller2.png"
	arryOutSize = 1080, 1920

	ResizeImage(strPath, strSave, arryOutSize)
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


