################################################
#
#  Created by jeon on 2017-06-02.
#  이미지 전처리 테스트 파일
#
################################################

from PIL import Image
import pytesseract
import cv2
import datetime
import numpy as np

src_path = "j:/img/"

def get_String(img_path):
    img = cv2.imread(img_path);
    print "start ==================="
    print  datetime.datetime.now()
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1,1),np.uint8)
    img = cv2.dilate(img,kernel,iterations=1)
    img = cv2.erode(img,kernel,iterations=1)
    cv2.imwrite(src_path+"removed_noise.png", img)
    print "end ==================="
    print  datetime.datetime.now()
    img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    cv2.imwrite(src_path+"thres.png",img)
    im = Image.open(src_path+'thres.png')
    result = pytesseract.image_to_string(im,lang="kor")

    return result

print "--------------- start =============="
print get_String(src_path+"1.png")
print "----------------done---------------"