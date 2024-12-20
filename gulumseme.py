import cv2

cascade_smile = cv2.CascadeClassifier('haarcascade_smile.xml')

def detect(gray_image,image):
    smile = cascade_smile.detectMultiScale(gray_image,1.7,50)
    for(x,y,w,h) in smile:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    return image


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(grayImage, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


