from PIL import Image, ImageFilter
#Read image
im = Image.open( './img.jpg' )
im2 = Image.open('./img2.jpg')
#Display image
#im.show()

print(im.getpixel((0, 0)))
print(list(im.getdata()))
out = Image.blend(im, im2, 0.5)

out.save('fusion.jpg','JPEG')

#Applying a filter to the image
#im_sharp = im.filter( ImageFilter.SHARPEN )
#Saving the filtered image to a new file
#im_sharp.save( 'image_sharpened.jpg', 'JPEG' )

#Splitting the image into its respective bands, i.e. Red, Green,
#and Blue for RGB
#r,g,b = im_sharp.split()

#Viewing EXIF data embedded in image
exif_data = im._getexif()
exif_data