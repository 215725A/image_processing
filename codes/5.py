import cv2

movie = cv2.VideoCapture('images/testmovie1.avi')

fps = int(movie.get(cv2.CAP_PROP_FPS))                         
w = int(movie.get(cv2.CAP_PROP_FRAME_WIDTH))                   
h = int(movie.get(cv2.CAP_PROP_FRAME_HEIGHT))                  
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')            
video = cv2.VideoWriter('images/video_out.mp4', fourcc, fps, (w, h), False)  

fgbg = cv2.createBackgroundSubtractorMOG2()            

while True:
    ret, frame = movie.read()                                  
    fgmask = fgbg.apply(frame)                                 
    video.write(fgmask)                                        

    if not ret:
        break

movie.release()