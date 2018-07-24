import time
#this script demonstrates how to use try:except structure
def loop():
	while True:
		print "Hello World!"
		time.sleep(1)

if __name__ == '__main__':
	try:
		loop()
	except KeyboardInterrupt:
		print '''Good Grief! I'm out of here.'''
