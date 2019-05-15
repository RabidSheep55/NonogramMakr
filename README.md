![NonogramMakr Logo](https://github.com/RabidSheep55/NonogramMakr/blob/master/FinalLogo.jpg)

# NonogramMakr
This little script generates a Nonogram puzzle when given a black and white image that would correspond to its solution.
bit useless tbh - except for the 5 people in the world who do them I guess

[What's a Nonogram you ask?](https://en.wikipedia.org/wiki/Nonogram)

# Requirements
 - Numpy and PIL packages (These are installed by default if you are using Spyder with Anaconda)
 - The OpenSans-Regular.ttf font file in the same directory as the script file (If you want another font, you'll need to change the global variable at the top of the code)
 - For now, you'll need a monochromatic BMP file (each pixel is only given one value between 0 and 255), the script will accomodate for any size image too!
 
 # How to use
  - cd to the directory in which you have the script and font file
  - Run it and follow the instructions! (python NonogramMakr.py)

Note: you can pass in the three parameters as command line arguments in this form:
    
    python NonogramMakr.py <inputImage.bmp> <outputImage.jpg> <resolution>
