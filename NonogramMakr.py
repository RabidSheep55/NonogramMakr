#  -*- coding: utf-8 -*-
"""
Created on Sat May  4 23:33:24 2019

LINKS:
    https://randomgeekery.org/2017/11/24/drawing-grids-with-python-and-pillow/
    https://www.geeksforgeeks.org/working-images-python/
    https://fonts.google.com/?query=sans&selection.family=Open+Sans

list(filter(None, list))

@author: tharr
"""
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import sys


def pr(A):
    for line in A:
        print(line)


def getImage(path):
    try:    
        # Get Image
        img = Image.open(path)
#        print(img.mode)
        
        # Get Image data
        width, height = img.size 
        imgArr = np.reshape(img.getdata(), (height, width))
        
        return imgArr
    
    except IOError:
        pass
    

def genHints(image):
    h = len(image)
    w = len(image[0]) 
    
#    print(w, h)
    
    hintCol = []
    for i in range(h):
        currCol = []
        j = 0
        while j < w:
            currHint = 0
            while image[i][j] == 0:        # Could change this to a threshold value when the image is not completely black and white
                currHint += 1
                j += 1   
                if j >= w:
                    break
            if currHint != 0:
                currCol += [currHint]
            j += 1
        hintCol += [currCol]
        
    hintRow = []
    for j in range(w):
        currRow = []
        i = 0
        while i < h:
            currHint = 0
            while image[i][j] == 0:        # Could change this to a threshold value when the image is not completely black and white
                currHint += 1 
                i += 1
                if i >= h:
                    break
            if currHint != 0:
                currRow += [currHint]
            
            i += 1
        hintRow += [currRow]
    
    return hintCol, hintRow


def sortKey(a):
    return len(a)


def findMax(A):
    return len(sorted(A, key=sortKey, reverse=True)[0])


def genPuzzle(hintCol, hintRow, res, output):   
    # res is a bit like the resolution
    
    h = len(hintCol)
    w = len(hintRow)
    
    # Find out the maximum amount of hints a row and column have
    maxh = findMax(hintRow)
    maxw = findMax(hintCol)
    
    height = h * res
    hoff = maxh  * res
    width = w * res 
    woff = maxw * res
    
    # Generate base canvas
    image = Image.new(mode='L', size = (width + woff + int(res/30) + 1, height + hoff + int(res/30) + 1), color = 255)
    
    # Make the grid boi
    draw = ImageDraw.Draw(image)
    yStart = hoff
    yEnd = image.height
    xStart = woff
    xEnd = image.width
    stepSize = res
    
        # Vertical Lines
    for x in range(woff, image.width, stepSize):
        line = ((x, yStart), (x, yEnd))
        draw.line(line, fill=50, width=int(res/15))

        # Horizontal Lines
    for y in range(hoff, image.height, stepSize):
        line = ((xStart, y), (xEnd, y))
        draw.line(line, fill=50, width=int(res/15))
        
    # Add the numbers
    font = ImageFont.truetype("OpenSans-Regular.ttf", int(res/1.7))
    
        #Hint Column
    for i in range(h):
        hints = hintCol[i]
        if hints:
#            print("Trying to lay out hints", hints)
            yPos = hoff + res*i
            for j in range(len(hints)-1, -1, -1):
                d = len(str(hints[j]))
                xPos = woff - (j+1)*res + res/(2.6)               
#                print("Trying to draw", hints[j], "at position", (xPos, yPos) )
                draw.text((xPos, yPos), str(hints[j]), 0, font=font)
                
        #Hint Row
    for i in range(w):
        hints = hintRow[i]
        if hints:
#            print("Trying to lay out hints", hints)
            
            for j in range(len(hints)-1, -1, -1):
                d = len(str(hints[j]))
                xPos = woff + res*i + res/1.8 - (res/6)*d # The d stuff makes sure the number is centered on a grid, I would need to learn more about fonts and typeface to determine this value exactly based on res
                print("corrected based on d=", d)
                yPos = hoff - (j+1)*res                
#                print("Trying to draw", hints[j], "at position", (xPos, yPos) )
                draw.text((xPos, yPos), str(hints[j]), 0, font=font)

    #Save image!
#    image.show()
    image.save(output)  
    del draw


def main(path, output, res):   
    print("Converting Image...")
    image = getImage(path)
#    pr(image)
    print("Image Converted")
    
    print("Generating Hints...")
    hintCol, hintRow = genHints(image)
#    print(hintCol)
#    print(hintRow)
    print("Hints Generated")
    
    print("Making Final puzzle...")
    genPuzzle(hintCol, hintRow, res, output)
    print("All done!")
    
    
if __name__ == "__main__": 
    
    if len(sys.argv) == 1:
        print('')
        print("Welcome to the first and ever Image to Nonogram Converter!")
        print("To use this script, you'll first need a monochromatic BMP image...")
        path = str(input("BW Image path: "))
        output = str(input("Output Puzzle path: "))
        res = int(input("Desired 'resolution': "))
        print("")
        
        main(path, output, res)
        
    elif len(sys.argv) == 4:
        path = str(sys.argv[1])
        output = str(sys.argv[2])
        res = int(sys.argv[3])
        
        main(path, output, res) 
        
    else:
        print("Invalid number of arguments -_-")