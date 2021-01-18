#code challenge 17
import PIL         #import PIl library
from PIL import Image

#to convert it into greyscale

i = Image.open('sample.jpg').convert('LA')#.rotate(270)
i.save('greyscale.png')                 #save image as
i.show()

# to rotate it 90 degree clockwise

i = Image.open('sample.jpg').convert('LA').rotate(270)
i.save('rotate.png')                            #save image as rotate
i.show()

#to crop the image

i = Image.open('sample.jpg').convert('LA').rotate(270)# we can also use -90degree
width, height = i.size   
left = (width - 1500)/2
top = (height - 1500)/2
right = (width + 1000)/2
bottom = (height + 1000)/2
i2=i.crop((left, top, right, bottom))
i2.save('crop.png')
i2.show()

#to produce thumbnail

margin=20
background=Image.new('RGBA',(75,75))
img = Image.open('sample.jpg').convert('LA').rotate(270)
img=img.resize((150,150-margin*2),Image.ANTIALIAS)
background.paste(img,(0,margin),img)
background.save('thumbnail.png')
