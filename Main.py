from CardDetector import CardDetector
import cv2

cardDetector = CardDetector()

img = cv2.imread("./Test_Imgs/test1.jpg")
cardDetector.detectImage(img)