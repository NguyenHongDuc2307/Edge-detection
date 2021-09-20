import argparse
import cv2
import numpy
import sys
numpy.set_printoptions(threshold=sys.maxsize)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


gray_g = (image[:,:,0]+ gray)/2
gray_g=cv2.convertScaleAbs(gray_g)


cv2.imshow("Original", image)
cv2.imshow("Gray scale", gray_g)
wide = cv2.Canny(gray_g, 100, 180)
mid = cv2.Canny(gray_g, 30, 150)
tight = cv2.Canny(gray_g, 340, 350)

print(tight)
# show the output Canny edge maps
cv2.imshow("Wide Edge Map", wide)
cv2.imshow("Mid Edge Map", mid)
cv2.imshow("Tight Edge Map", tight)
cv2.waitKey(0)