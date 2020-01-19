import time
import pyfirmata
import numpy as np

board = pyfirmata.Arduino('COM7')
iter8 = pyfirmata.util.Iterator(board)
iter8.start()
succ=170
vert=board.get_pin('d:3:s')
arm=board.get_pin('d:10:s')
succ=board.get_pin('d:11:s')
print("connected")
astate=0
sstate=0

arm.write(0)
vert.write(45)
succ.write(20)
time.sleep(5)

def pos2pwm(pos):
    d = {0: 144, 1: 108, 2: 72, 3: 36, 4: 0}
    #degree is arc from left side
    deg=180-45*pos
    return deg

def move_card(from_ind, to_ind,arm,vert,succ):
    #arm, vert, succ correspond to the servos
    #move arm to position
    t = 1
    up_pos = 45
    down_pos = 130
    half_down_pos = 60
    arm.write(pos2pwm(from_ind))
    time.sleep(t)
    #lower the boy
    vert.write(down_pos)
    time.sleep(t)
    #succ
    succ.write(170)
    time.sleep(t)
    #raise the boy
    vert.write(up_pos)
    time.sleep(t)
    #move arm to position
    arm.write(pos2pwm(to_ind))
    time.sleep(t)
    #drop again
    vert.write(half_down_pos)
    time.sleep(t)
    #de-succ
    succ.write(20)
    time.sleep(t)
    #move arm back up
    vert.write(up_pos)
    time.sleep(t)

def get_swap_sequence(card_ranks):
    swap_sequence = []
    sorted = np.sort(card_ranks)

    for i in range(len(card_ranks)):
        if card_ranks[i] != sorted[i]:
            correct_index = np.where(sorted == card_ranks[i])[0][0]
            swap_sequence.append((i, correct_index))
            temp = card_ranks[i]
            card_ranks[i] = card_ranks[correct_index]
            card_ranks[correct_index] = temp
    return swap_sequence

def execute_swap_sequence(swap_sequence,arm,vert,succ):
    TMP_CARD=2
    for (pos1, pos2) in swap_sequence:
        move_card(pos1,TMP_CARD,arm,vert,succ)
        move_card(pos2,pos1,arm,vert,succ)
        move_card(TMP_CARD,pos1,arm,vert,succ)

move_card(4, 2, arm, vert, succ)
move_card(0, 4, arm, vert, succ)
move_card(2, 0, arm, vert, succ)

