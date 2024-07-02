import cv2
import time


cap  = cv2.VideoCapture(0)

widh = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*"DIVX")

writer = cv2.VideoWriter("video.mp4",fourcc,30,(widh,height))

while True:

    ret , frame = cap.read()
    cv2.imshow("video",frame)

    writer.write(frame)

    if cv2.waitKey(1) & 0xFF == ord("q"): break


cap.release()
writer.release()
cv2.destroyAllWindows()