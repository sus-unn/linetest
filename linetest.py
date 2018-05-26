import cv2

print("lintest for 2d animtaion")
print("press s to save")
print("press ctrl c to exit")

prefix = input("Enter prefix: ")
cap = cv2.VideoCapture(0)
count = 1

while(True):
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    
    cv2.imshow('preview', rgb)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        out = cv2.imwrite(prefix + str(count) + ".jpg", frame)
        count += 1
        print("saved: " + prefix + str(count) + ".jpg")

cap.release()
cv2.destroyAllWindows()