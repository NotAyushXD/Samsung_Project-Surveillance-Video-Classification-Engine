import cv2

cap= cv2.VideoCapture('/home/ayush/Desktop/Multiple Instance learning/test_video.mp4')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    st = '/home/ayush/Desktop/Multiple Instance learning/video_data/'
    cv2.imwrite(st + 'test'+str(i)+'.jpg',frame)
    i+=1

cap.release()
cv2.destroyAllWindows()
