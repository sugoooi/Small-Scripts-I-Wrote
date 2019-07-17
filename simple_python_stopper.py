import time
import re
import subprocess as sp

def validate_legal(num):
	if num >= 60 or num < 0:
		return False
	return True

sp.call('cls',shell=True)
timer_format = raw_input('Enter countdown time in dd:dd:dd format: ')
vals = map(int, re.findall('(\d+):(\d+):(\d+)', timer_format)[0])

legal = True
for val in vals:
	if not validate_legal(val):
		legal = False
		break

if vals and legal:
	h = vals[0]; m = vals[1]; s = vals[2]
	while h >= 0:
		sp.call('cls',shell=True)
		print("{}:{}:{}".format(h, m, s))
		time.sleep(1)
		s -= 1
		if s < 0:
			s = 60 + s
			m -= 1
		if m < 0:
			m = 60 + m
			h -= 1