from PIL import Image, ImageDraw, ImageFont
import os

def text_on_image(filename='./image-01.png', text='Hello', size=12, color=(255,255,0), bg='red'):
    "Draw a text on an Image, saves it, show it"
    fnt= ImageFont.truetype('fonts/anonymous-pro-v13-latin-700.ttf', size)
    # create image
    image = Image.new(mode = "RGB", size = (int(1.2*size/2)*len(text),size+30), color = 0)
    draw = ImageDraw.Draw(image)
    # draw text
    draw.text((10,10), text, font=fnt, fill=(255,255,0))
    # save file
    image.save(filename)
    #show file
    # os.system(filename)


text_on_image(text="Welcome To Smy-Whitty Video Productions - Python Generated Text", size=36, bg='red')
