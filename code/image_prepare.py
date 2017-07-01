# coding=utf-8
'''

input image (Image.open)
get gray image(
    *_*gray.py need to reconstruction)
let 3pass image to 1pass image(
    *_*set_threshold.py and get_one_pass.py need to resconstruction)
output image

'''
import sys
import cv2
import numpy as np
from PIL import Image
def get_prepare_image(argv):
    url = argv
    print url
    path = argv
    path1 = 'Users/mali/Documents/MNIST/mnist_demo/CNN_mnsit/7.png'
    path3 = str(path)
#    print path

    print path
    image = cv2.imread(path3)
#    image = Image.open(path)
    print image
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    cv2.threshold(image, 140, 255, 0, image)

    res3 = cv2.resize(image, (28,28), interpolation = cv2.INTER_AREA)
    cv2.imwrite("TEM_RGK.bmp", res3, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
    im  =  Image.open('TEM_RGK.bmp')
    #  convert to grey level image
    Lim  =  im.convert('L')
    #Lim.save('sample_6.png')

    #  setup a converting table with constant threshold
    threshold  =  200
    table  =  []
    for  i  in  range( 256 ):
        if  i  >  threshold:
            table.append(0)
        else :
            table.append(1)
    #print len(table)
    #for i in range(len(table)):
        #print table[i]
    #  convert to binary image by the table
    bim  =  Lim.point(table,'1')
    #print (list(bim.getdata()))
    bim.save('TEM_BRGK.png')
    img = cv2.imread('TEM_BRGK.png')
    r,g,b = cv2.split(img)

    for i in range(28):
        for j in range(28):
            if r[i,j] > 0:
                r[i,j] = 255
    #cv2.imshow('Blue',r)
    cv2.imwrite("blue_M.png", r, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
    #cv2.waitKey(0)

def main(argv):

#    length = len(argv)
#    print length
 #   for i in range(length):
    get_prepare_image(argv)

#if  __name__ == "__main__":
#    main(sys.argv[1])

