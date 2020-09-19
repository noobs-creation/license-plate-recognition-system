import pytesseract
import cv2
import imutils
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'

image = cv2.imread("1.png", cv2.IMREAD_COLOR)
image = cv2.resize(image, (600, 400))

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image = cv2.bilateralFilter(gray_image, 13, 15, 15)

edged = cv2.Canny(gray_image, 30, 200)
contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
screenCnt = None

for c in contours:

    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)

    if len(approx) == 4:
        screenCnt = approx
        break

if screenCnt is None:
    detected = 0
    print("No contour detected")
else:
    detected = 1

if detected == 1:
    cv2.drawContours(image, [screenCnt], -1, (0, 0, 255), 3)

mask = np.zeros(gray_image.shape, np.uint8)
new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
new_image = cv2.bitwise_and(image, image, mask=mask)

(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
cropped_image = gray_image[topx:bottomx + 1, topy:bottomy + 1]

detected_text = pytesseract.image_to_string(cropped_image, config='--psm 11')
print("Detected license plate Number is: ", detected_text)
image = cv2.resize(image, (500, 300))
cropped_image = cv2.resize(cropped_image, (400, 200))
cv2.imshow("image",image)
cv2.imshow("cropped_image",cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
