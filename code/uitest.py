# -*- coding:utf-8 -*-
from Tkinter import *
from PIL import Image, ImageTk
import predict_2

#import image_prepare.py
global x
root = Tk()
root.geometry('500x300+500+200')
root.title('图片识别')
image_frame = Frame(root)

l1 = Label(root, text="图片名称")
l1.pack()  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
xls_text = StringVar()
answer = StringVar()
xls = Entry(root, textvariable = xls_text)
xls_text.set("blue_M.png")
ans = Entry(root,textvariable = answer)
answer.set("ANWSER")

xls.pack()
ans.pack()
def on_click():
    x = xls_text.get()
    print x
    return x
def get_url():
    print xls_text.get()
    return xls_text.get()

    #s = sheet_text.get()
    #l = loop_text.get()
    #sl = sleep_text.get()
    #string = str("xls名：%s sheet名：%s 循环次数：%s 休眠时间：%s " %(x, s, l, sl))
    #print("xls名：%s sheet名：%s 循环次数：%s 休眠时间：%s " %(x, s, l, sl))
    #messagebox.showinfo(title='aaa', message = string)
#def get_pim():
#    image_prepare.main(get_url)


#Button(root, text="press", command = on_click).pack()
#Button(root,text="预处理",command = get_pim).pack()
def callback():
    '''
    predict_2.main(get_url())
    print 1
    if  pNum == 5:
        answer.set("5")
        ans.pack()
#anslist = ['0','1','2','3','4','5','6','7','8','9']
    '''
    anw = predict_2.main(get_url())
    print anw
    anslist = ['0','1','2','3','4','5','6','7','8','9']
    pre_output = anw[0]
    output = str(pre_output)
    print output
    answer.set(output)
    ans.pack()


image_file1 = Image.open(get_url())
print image_file1
#image_file2 = Image.open("2M.png")
#image_file3 = Image.open("3M.png")
#image_file4 = Image.open("4M.png")
#image_file5 = Image.open("5M.png")
#image_file6 = Image.open("6M.png")

im1 = ImageTk.PhotoImage(image_file1)
#im2 = ImageTk.PhotoImage(image_file2)
#im3 = ImageTk.PhotoImage(image_file3)
#im4 = ImageTk.PhotoImage(image_file4)
#im5 = ImageTk.PhotoImage(image_file5)
#im6 = ImageTk.PhotoImage(image_file6)

image_label = Label(image_frame,image = im1).pack(side = LEFT,padx = 0, pady = 50)
#image_label = Label(image_frame,image = im2).pack(side = LEFT,padx = 0, pady = 50)
#image_label = Label(image_frame,image = im3).pack(side = LEFT,padx = 0, pady = 50)
#image_label = Label(image_frame,image = im4).pack(side = LEFT,padx = 0, pady = 50)
#image_label = Label(image_frame,image = im5).pack(side = LEFT,padx = 0, pady = 50)
#image_label = Label(image_frame,image = im6).pack(side = LEFT,padx = 0, pady = 0)
Button(root, text="识别图片", fg="blue",bd=3,width=28,command=callback).pack()




image_frame.pack()

root.mainloop()
