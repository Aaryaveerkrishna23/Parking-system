import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2


font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,50)
fontScale              = 1
fontColor              = (205,92,5)
lineType               = 2
webcam = cv2.VideoCapture(1)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()
    
while webcam.isOpened():

    
    status, frame = webcam.read()

    # if not status:
    #     print("Could not read frame")
    #     exit()

    
    bbox, label, conf = cv.detect_common_objects(frame)

    print(bbox, label, conf)

    # 
    out = draw_bbox(frame, bbox, label, conf)
    out = cv2.putText(frame,'No. of spaces in Parking Lot: '+ str(10-label.count('car')), 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    lineType)
    
    

    
    cv2.imshow("Real-time object detection", out)
    print('No. of spaces in Parking Lot: '+ str(10-label.count('car')))
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

webcam.release()
cv2.destroyAllWindows()   