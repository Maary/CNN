# -*- coding:utf-8 -*-
from Tkinter import *
import tkFileDialog
from PIL import Image, ImageTk
import image_prepare
global filePath
root = Tk()
root.geometry('600x500+500+200')
root.title('图片预处理')
image_frame = Frame(root)

image_file = im = image_label = None
def create_image_label():
    global image_file, im, image_label,im_path
    #image_file = Image.open("F:\\Pie.jpg")
    im_path = tkFileDialog.askopenfilename(title='打开文件', filetypes=[('Python', '*.py *.pyw *.png *.jpg *.bmp'), ('All Files', '*')])
    print im_path
    image_file = Image.open(im_path)
    im = ImageTk.PhotoImage(image_file)
    image_label = Label(image_frame,image = im)
    image_label.grid(row = 3, column = 0, sticky = NW, pady = 30, padx = 20)


def get_pim():
    #    image_prepare.get_prepare_image(get_url())
    path = str(im_path)
    print path
    image_prepare.main(path)


#button = Button(image_frame,text='选择图片',anchor = 'center',command = create_image_label)
Button(root, text="选择图片", fg="blue",bd=3,width=28,command= create_image_label).pack()
#button.grid(row = 5, column = 0, sticky = NW, pady = 8, padx = 20)
Button(root,text="预处理",fg = "red", bd = 20,width = 26,command = get_pim).pack()

image_frame.pack()

root.mainloop()
