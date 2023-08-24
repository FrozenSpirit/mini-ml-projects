import cv2

# task is to detect given color in image
import numpy as np

path = 'Resources/lambo.PNG'
img = cv2.imread(path)

# firstly convert this image into HSV space
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


# So now we need to define some color values, some ranges in
# which we want our color to be, so we will define the Hue,
# the saturation and value limits within that limit if the
# image value falls then we grab that, but we do not know it now
# so we introduce Trackbars which allows us to play with values
# in real time and get the values

# empty function for creation of trackbars, useless for now
def empty(a):
    pass


# making the trackbar window in which we but in trackbars
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 200)
# normally Hue has max val 360 but here we have 180
cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, empty)  # 0
cv2.createTrackbar("Hue Max", "Trackbars", 179, 179, empty)  # 19
# saturation
cv2.createTrackbar("Sat Min", "Trackbars", 0, 255, empty)  # 110
cv2.createTrackbar("Sat Max", "Trackbars", 255, 255, empty)  # 240
# values
cv2.createTrackbar("Val Min", "Trackbars", 0, 255, empty)  # 153
cv2.createTrackbar("Val Max", "Trackbars", 255, 255, empty)  # 255

# # now we need to grab the values from trackbar and apply that to our image
# h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
# h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")

# to get the value we need to put it into a loop cause we are getting
# the value again and again

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    sat_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    sat_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    val_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    val_max = cv2.getTrackbarPos("Sat Max", "Trackbars")

    print(h_min, h_max, sat_min, sat_max, val_min, val_max)

    # now we gotta take these values and use it
    # it will give us the filtered out image of that color
    # keep adjusting till all other are black except color you want
    # then change default values of trackbars to these values
    lower = np.array([h_min, sat_min, val_min])
    upper = np.array([h_max, sat_max, val_max])
    mask = cv2.inRange(imgHSV, lower, upper)

    # after getting the values now we make new image by filling the
    # white in masked image
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Original", img)
    cv2.imshow("HSV Image", imgHSV)
    # masked image
    cv2.imshow("Mask", mask)
    # after applying masked image to orignial image
    cv2.imshow("Result Image", imgResult)
    # 1 cause its while loop, if 0 then infinite

    # you can use the function in resource to stack images next to each other
    # imgStack = stackImages(0.6, ([img, imgHSV], [mask, imgResult]))

    cv2.waitKey(1)
