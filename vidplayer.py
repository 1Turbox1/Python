import cv2
from PIL import Image
import argparse
import numpy as np
import time
import os

def printTheImageInCMD(array,args):
  text = ""
  for x in range(0, len(array)):
      for y in range(0, len(array[x])):
          if array[x][y] >= 0 and array[x][y] <= 15:
              text = text + " "
          elif array[x][y] > 15 and array[x][y] <= 30:
              text = text + "¸"
          elif array[x][y] > 30 and array[x][y] <= 45:
              text = text + "."
          elif array[x][y] > 45 and array[x][y] <= 60:
              text = text + "'"
          elif array[x][y] > 60 and array[x][y] <= 75:
              text = text + "\""
          elif array[x][y] > 75 and array[x][y] <= 90:
              text = text + "‹"
          elif array[x][y] > 90 and array[x][y] <= 105:
              text = text + "⌂"
          elif array[x][y] > 105 and array[x][y] <= 120:
              text = text + ":"
          elif array[x][y] > 120 and array[x][y] <= 135:  
              text = text + "÷"
          elif array[x][y] > 135 and array[x][y] <= 150:  
              text = text + "+"
          elif array[x][y] > 150 and array[x][y] <= 165:  
              text = text + ":"
          elif array[x][y] > 165 and array[x][y] <= 180:  
              text = text + "†"
          elif array[x][y] > 180 and array[x][y] <= 195:  
              text = text + "‡"
          elif array[x][y] > 195 and array[x][y] <= 210:  
              text = text + "?"
          elif array[x][y] > 210 and array[x][y] <= 225:  
              text = text + "&"
          elif array[x][y] > 225 and array[x][y] <= 240:
              text = text + "#"
          elif array[x][y] > 240 and array[x][y] <= 255:
              text = text + "@"
  print(text, end="", flush=True)

def main(args):
  vidcap = cv2.VideoCapture(args.video) 
  success,image = vidcap.read() # otworz wideo i zczytaj dane
  count = 0
  frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT)) # zczytaj ilosc klatek
  while success:
    image = cv2.resize(image,(args.width,args.height)) # zmien rozdzielczosc na 120x30
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # filter czarnobialy
    cv2.imwrite(args.framefolder + "frame"+str(count)+".png", image) # zapisz klatke
    success,image = vidcap.read() # zczytaj ponownie klatke
    count = count + 1 # zwieksz licznik
    if count % 500 == 0:
        print("Stworzono " + str(count) + " z " + str(frames) + " klatek")
  os.system('cls' if os.name == 'nt' else 'clear')
  width = args.width
  height = args.height
  emptyArray = np.zeros((height, width))
  for i in range(0, height):
      for j in range(0, width):
        emptyArray[i][j] = 0 # wypelnij tablice zerami
  for k in range(0, frames):
    imag = Image.open(args.framefolder + "frame"+str(k)+".png")
    imag = imag.convert('RGB')
    for y in range(0, imag.size[1]):
      for x in range(0, imag.size[0]):
        pixelRGB = imag.getpixel((x, y))
        R,G,B = pixelRGB
        brightness = sum([R, G, B])/3
        emptyArray[y][x] = brightness # otworz plik, zdobadz int kolorow i magja matematyki zmien na int jasnosci, potem dodaj do tabeli
    printTheImageInCMD(emptyArray,args)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--video', type=str, default='', help='Nazwa wideo')
  parser.add_argument('--framefolder', type=str, default='frames/', help='Nazwa folderu frame\'ow')
  parser.add_argument('--width', type=int, default=120, help='Szerokosc wideo')
  parser.add_argument('--height', type=int, default=30, help='Wysokosc wideo')
  args = parser.parse_args()
  if os.path.exists(args.framefolder):
    pass
  else:
    os.mkdir(args.framefolder)
  main(args)


