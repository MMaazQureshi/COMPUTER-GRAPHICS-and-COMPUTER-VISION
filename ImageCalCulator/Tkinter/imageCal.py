# import tkinter as tk
import Tkinter as tk  # for Python 2.x version
# from Tkinter import filedialog
# from Tkinter import ttk
# from tkinter import filedialog
# from tkinter import ttk
# from PIL import ImageTk, Image
import numpy as np
import cv2

root = tk.Tk()

variable1 = 1
variable2 = 3
img1 = cv2.imread('hitman.jpg', 1)
img2 = cv2.imread('ubuntu.jpg', 1)


def addCallback():
    final = img1 + img2
    print("Image added", final)
    cv2.namedWindow("added", cv2.WINDOW_NORMAL)
    imS = cv2.resize(final, (960, 540))
    cv2.imshow('image', imS)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def subCallback():
    final = img1 - img2
    print("Image subtracted", final)
    cv2.namedWindow("subtracted", cv2.WINDOW_NORMAL)
    imS = cv2.resize(final, (960, 540))
    cv2.imshow('image', imS)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def mulCallback():
    final = img1 * img2
    print("Image multiplied", final)
    cv2.namedWindow("multiplied", cv2.WINDOW_NORMAL)
    imS = cv2.resize(final, (960, 540))
    cv2.imshow('image', imS)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def divCallback():
    final = img1 / img2
    print("Image divided", final)
    cv2.namedWindow("divided", cv2.WINDOW_NORMAL)
    imS = cv2.resize(final, (960, 540))
    cv2.imshow('image', imS)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


label1 = tk.Label(root, text="Image Calculator")
label2 = tk.Label(
    root, text="Your images are imported, just use the operators")
label1.pack(padx=20)
label2.pack(padx=20)
Badd = tk.Button(root, text="+", command=addCallback)
Badd.pack()
Bsub = tk.Button(root, text="-", command=subCallback)
Bsub.pack()
Bmul = tk.Button(root, text="*", command=mulCallback)
Bmul.pack()
Bdiv = tk.Button(root, text="/", command=divCallback)
Bdiv.pack()

label3 = tk.Label(root, text="Muzammil Sarwar EP1850097")
label3.pack(padx=20)  #
root.mainloop()
