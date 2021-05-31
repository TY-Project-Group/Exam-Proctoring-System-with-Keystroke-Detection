import threading    
import time
import cv2
from keyStrokeDetection import key_start 
from gazeTracking import start_gazeTracking
from person_and_phone import start_phone_person

if __name__ == "__main__":

    video_capture = cv2.VideoCapture(0)

    t1 = threading.Thread(target=key_start, args=())
    t2 = threading.Thread(target=start_gazeTracking, args=(video_capture, ))
    t3 = threading.Thread(target=start_phone_person, args=(video_capture, ))
  
    t1.start()
    t3.start()
    t2.start()
  
    t1.join()
    t3.join()
    t2.join()