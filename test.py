import pyfirmata
import time

board=pyfirmata.Arduino('COM7')
iter8 = pyfirmata.util.Iterator(board)
iter8.start()
succ=170
arm=board.get_pin('d:3:s')
succ=board.get_pin('d:11:s')
print("connected")
astate=0
sstate=0
#arm down is 180, arm up is 120
#
print(arm.read())
while True:
	inp=input()
	if inp=='a':
		astate+=1
		if astate%2==0:
			arm.write(130)
		else:
			arm.write(45)
	if inp=='s':
		sstate+=1
		if sstate%2==0:
			succ.write(170)
		else:
			succ.write(20)