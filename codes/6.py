import numpy as np
import cv2

def contours(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                  
    ret, img_binary = cv2.threshold(img_gray,                         
                                    60, 255,                          
                                    cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(img_binary,                
                                           cv2.RETR_EXTERNAL,         
                                           cv2.CHAIN_APPROX_SIMPLE)
    
    contours = np.concatenate(contours)
    x = np.mean(contours[0].T[0, 0])                                  
    y = np.mean(contours[0].T[1, 0])                                  
    return x, y

movie = cv2.VideoCapture('images/testmovie1.avi', 0)                  

fps = int(movie.get(cv2.CAP_PROP_FPS))                                
w = int(movie.get(cv2.CAP_PROP_FRAME_WIDTH))                          
h = int(movie.get(cv2.CAP_PROP_FRAME_HEIGHT))                         
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')                   
video = cv2.VideoWriter('images/video_out-avi.mp4', fourcc, fps, (w, h), True)

x_list = []
y_list = []
while True:
    ret, frame = movie.read()                                         
    
    if not ret:
        break

    x, y = contours(frame)                                            

    frame = cv2.circle(frame, (int(x), int(y)), 30, (0, 255, 0), 3)  

    video.write(frame) 
    x_list.append(x)
    y_list.append(y)

movie.release()