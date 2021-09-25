from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

df = pd.read_csv('list.csv')
font = ImageFont.truetype("fonts/poppinsSB.ttf", 55)
font2 = ImageFont.truetype("fonts/poppinsRegular.ttf",18)
for index, j in df.iterrows():
  img = Image.open('certi.png')
  draw = ImageDraw.Draw(img)
  draw.text(xy=(73,353), text='{}'.format(j['name']), fill=(108,203,219),font=font)
  draw.text(xy=(254,469), text='{}'.format(j['topic']), fill=(102,102,102),font=font2)
  img.save('pictures/{}.png'.format(j['name']))