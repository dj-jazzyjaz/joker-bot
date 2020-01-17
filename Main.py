from CardDetector import CardDetector
import cv2
import pyfirmata
import time
import VideoStream
import time
import CardSort

cardDetector = CardDetector()

#cap = cv2.VideoCapture(0)

#for i in(range(10)):
    # Capture frame-by-frame
#    ret, frame = cap.read()

IM_WIDTH = 1280
IM_HEIGHT = 720
FRAME_RATE = 10
# videostream = VideoStream.VideoStream((IM_WIDTH,IM_HEIGHT),FRAME_RATE,2,0).start()
time.sleep(1) # Give the camera time to warm up

cap = cv2.VideoCapture(0)
'''
board=pyfirmata.Arduino('COM3')#need to change to make work
arm=board.get_pin('d:3:s')
vert=board.get_pin('d:10:s')
succ=board.get_pin('d:11:s')
arm.write(0)
vert.write(0)
succ.write(20)#20 is resting
time.sleep(2)
'''
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cards = cardDetector.detectImage(frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        if len(cards) == 0:
            print("No cards detected")
            continue

        cards_sorted, ranks_sorted = CardSort.sort_cards_by_x(cards)
        swap_sequence = CardSort.get_swap_sequence(ranks_sorted)
        CardSort.execute_swap_sequence(swap_sequence, arm,vert,succ)



# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
