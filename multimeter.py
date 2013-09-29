import serial


ser = serial.Serial('/dev/tty.usbmodem1421',9600)

i = 0
v = 0
pre_v = 0.0
tol = 0.01

while True:
	try:
		v = float(ser.readline())
	except:
		v = 0
	if v <= pre_v - tol and v >= pre_v - tol:
		i += 1
	else:
		i = 0
	pre_v = v
	if i > 100:
		# open site to appropriate place
		if v > 0.045:
			tomato = True
			potato = False
		else:
			tomato = False
			potato = True
		break

import webbrowser

if(potato):
		webbrowser.open_new('http://127.0.0.1:8000/result/potato/')
	else:
		webbrowser.open_new('http://127.0.0.1:8000/result/tomato/')


