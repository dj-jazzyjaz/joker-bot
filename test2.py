import pyfirmata

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
while True:
    inp=input()
    if inp =='a':
        astate+=1
        if astate % 2 == 0:
            vert.write(130)
        else:
            vert.write(45)
    elif inp == 's':
        sstate+= 1
        if sstate % 2 == 0:
            succ.write(170)
        else:
            succ.write(20)
    else:
        arm.write(int(inp))


