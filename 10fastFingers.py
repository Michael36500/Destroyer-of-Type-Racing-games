from urllib.parse import _ResultMixinBytes
from pynput.keyboard import Key, Controller
import time
from numpy import double
from pytesseract import*
import numpy as np
import cv2
import pyautogui

time.sleep(2)

pytesseract.tesseract_cmd = r'C:\\Users\\ambro\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

min_conf = 40

keyboard = Controller()

for a in range(13):
    image = pyautogui.screenshot()
    # image = cv2.imread("image1.png")
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    # image = image[679:978, 556:1345]
    # image = image[189:284, 436:1300] 
    image = image[453:540, 37:946] 

    cv2.imwrite("image3.png", image)


    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pytesseract.image_to_data(image, output_type=Output.DICT)

    for i in range(0, len(results["text"])):
        
        # We can then extract the bounding box coordinates
        # of the text region from the current result
        x = results["left"][i]
        y = results["top"][i]
        w = results["width"][i]
        h = results["height"][i]
        
        # We will also extract the OCR text itself along
        # with the confidence of the text localization
        text = results["text"][i]
        conf = float(results["conf"][i])
        
        # filter out weak confidence text localizations
        if conf > min_conf:
            print(text, "[{}]".format(conf), end=" ")
            for a in text:
                if a == "|":
                    keyboard.type("I")
                    break
                keyboard.type(a)
                time.sleep(0.00002)
            keyboard.type(" ")
    time.sleep(0.0002)



