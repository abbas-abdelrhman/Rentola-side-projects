import numpy as np

import cv2
import pytesseract
import urllib
from io import BytesIO
import urllib.request



def read_images(image_link):
    response = urllib.request.urlopen(image_link)
    image = BytesIO(response.read())

    image = np.asarray(bytearray(image.read()))

    # read the image using cv2
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # image = cv2.imdecode(np.asarray(bytearray(image.read()), dtype=np.uint8), cv2.IMREAD_COLOR)

    # extract the text from the image
    text = pytesseract.image_to_string(image)
    print(text)


img = "https://www.michielstolker.nl/wp-content/uploads/WPL/579/thimg_thimg_1_1600x750-6_1600x750.jpg?timestamp=1672718186800"

test = read_images(img)

