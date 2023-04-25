import sys
import cv2
import numpy as np
sys.path.append("../python-common")

import TIS


Tis = TIS.TIS()

if not Tis.selectDevice():
    quit(0)

try:
    Tis.Set_Property("TriggerMode","Off")
except Exception as error:
    print(error)


Tis.Start_pipeline() 

print('Press Esc to stop')
lastkey = 0

cv2.namedWindow('Window')  

kernel = np.ones((5, 5), np.uint8)  

while lastkey != 27:
    if Tis.Snap_image(1) is True:  
        image = Tis.Get_image()  
        numpy_array = np.asfarray(image)
        print(numpy_array)
        #image = cv2.erode(image, kernel, iterations=5)  
        cv2.imshow('Window', image)  

    lastkey = cv2.waitKey(10)

Tis.Stop_pipeline()
cv2.destroyAllWindows()
print('Program ends')
