#### Basic License Plate Recognition System

This is just a very simple and basic python program using opencv and pytesseract to detect and recognise the license plate from a given image.
The program gives out a few false-positives, further we can train and use some models to detect license plates from images.

#### Requirements:

You need to have previously installed tesseract-ocr application for windows or linux, 
and also install a few libraries.

```
pip install pytesseract
pip install opencv-python
pip install numpy
pip install imutils
```

#### Runnning the program:

You need to enter the tesseract.exe file location in line number 6, according to where you installed it. <br>
And also you need to put the image file in same folder as the python program file and change the name of file in line number 8,
and run the program with,
```
python main.py
```