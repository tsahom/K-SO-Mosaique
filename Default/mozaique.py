from PIL import Image, ImageFilter
import os, random

def genererMosa(database="http://51.68.86.16/img/IMAGE/", image="http://51.68.86.16/img/imageNuitInfo.jpg", sizePixel=55):
    listImage = generateImagesFromDataBase(database,sizePixel)
    listColor = getColorlistImage(image, sizePixel)
    blendedlist = blendcolorimg(listImage,listColor)
    imageFinal = generateFinalImage(blendedlist, image)
    imageFinal.save('Mosaique.jpg','JPEG')

def generateImagesFromDataBase(database, size):
    listImage = []
    for root, dirs, files in os.walk(database):
        for filename in files:
            im = Image.open(root+filename)
            im = setImageSize(im, size)
            im = im.rotate(-90)
            listImage += [im]
    return listImage

def setImageSize(im, size=50):
    return im.resize((size,size))

def getColorlistImage(image, size):
    im = Image.open(image)
    width = im.size[0]
    height = im.size[1]
    listC = []
    for y in range(height):
        for x in range(width):
            img = Image.new("RGB", (size, size), im.getpixel((x, y)))
            listC += [img]
    return listC


def blendcolorimg(listImage, listColor):
    blendedlist = []
    for img in listColor:
        im = Image.blend(img,random.choice(listImage),0.3)
        blendedlist += [im]
    return blendedlist

def generateFinalImage(blendedlist,img):
    sizeimg = Image.open(img).size
    finalimage = Image.new("RGB",(sizeimg[0]*blendedlist[0].size[0],sizeimg[1]*blendedlist[0].size[1]))

    x_offset = 0
    y_offset = 0
    compt = 0
    for y in range(sizeimg[1]):
        for x in range(sizeimg[0]):
            finalimage.paste(blendedlist[compt], (x_offset, y_offset))
            x_offset += blendedlist[x].size[0]
            compt += 1
        x_offset = 0
        y_offset += blendedlist[y].size[1]
    return finalimage


genererMosa("G:\SciTE\IMAGE\\","C:\\Users\\Thomas\\Downloads\\imageNuitInfo.jpg")