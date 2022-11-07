from PIL import Image
import tkinter.filedialog
import numpy as np

AA_NAME = input("What is the name of the ASCII art?:")

Filepass = tkinter.filedialog.askdirectory(title="Which file do you want to put it in?") + '/'
img= Image.open(tkinter.filedialog.askopenfilename(filetypes = [("Image file", ".bmp .png .jpg .tif"), ("Bitmap", ".bmp"), ("PNG", ".png"), ("JPEG", ".jpg"), ("Tiff", ".tif") ]))

size=img.size

width = img.width

ratio = 1

img_gray = Image.new('L',size)

def change_256tone(r,g,b):
    grey = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
    if grey > 255:
        return 255
    else:
        return grey

def change_2tone(r,g,b):
    tone = 128
    grey = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
    grey = round(grey/tone)
    grey = grey*tone-1
    if grey > 255:
        return 255
    else:
        return grey

def change_4tone(r,g,b):
    tone = 64
    grey = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
    grey = round(grey/tone)
    grey = max(0,grey*tone-16)
    if grey > 255:
        return 255
    else:
        return grey

def change_8tone(r,g,b):
    tone = 32
    grey = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
    grey = round(grey/tone)
    grey = max(0,grey*tone-16)
    if grey > 255:
        return 255
    else:
        return grey

def change_16tone(r,g,b):
    tone = 16
    grey = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
    grey = round(grey/tone)
    grey = grey*tone-1
    if grey > 255:
        return 255
    else:
        return grey
'''
for x in range(size[0]):
    for y in range(size[1]):
        if img.mode != 'L':
            r,g,b=img.getpixel((x,y))[:3]
            img_gray.putpixel((x,y),change_2tone(r,g,b))
        else:
            img_gray.putpixel((x,y),img.getpixel((x,y)))

img_gray.save(Filepass + str(AA_NAME) + '2tone.png')
'''
'''
for x in range(size[0]):
    for y in range(size[1]):
        if img.mode != 'L':
            r,g,b=img.getpixel((x,y))[:3]
            img_gray.putpixel((x,y),change_4tone(r,g,b))
        else:
            img_gray.putpixel((x,y),img.getpixel((x,y)))

img_gray.save(Filepass + str(AA_NAME) + '4tone.png')
'''
'''
for x in range(size[0]):
    for y in range(size[1]):
        if img.mode != 'L':
            r,g,b=img.getpixel((x,y))[:3]
            img_gray.putpixel((x,y),change_8tone(r,g,b))
        else:
            img_gray.putpixel((x,y),img.getpixel((x,y)))

img_gray.save(Filepass + str(AA_NAME) + '8tone.png')
'''
'''
for x in range(size[0]):
    for y in range(size[1]):
        if img.mode != 'L':
            r,g,b=img.getpixel((x,y))[:3]
            img_gray.putpixel((x,y),change_16tone(r,g,b))
        else:
            img_gray.putpixel((x,y),img.getpixel((x,y)))

img_gray.save(Filepass + str(AA_NAME) + '16tone.png')
'''
'''
for x in range(size[0]):
    for y in range(size[1]):
        if img.mode != 'L':
            r,g,b=img.getpixel((x,y))[:3]
            img_gray.putpixel((x,y),change_256tone(r,g,b))
        else:
            img_gray.putpixel((x,y),img.getpixel((x,y)))

img_gray.save(Filepass + str(AA_NAME) + '256tone.png')
'''
