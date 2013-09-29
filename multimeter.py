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
	if i > 500:
		# open site to appropriate place
		break



