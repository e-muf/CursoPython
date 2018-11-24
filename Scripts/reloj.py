import datetime
import time, os

while True:
	os.system('clear')
	dt = datetime.datetime.now()
	print(dt.strftime('%H:%M:%S'))
	time.sleep(1)
	