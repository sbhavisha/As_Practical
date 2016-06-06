#!/usr/bin/python
import sys
def compare():
	try:
		a = raw_input("Enter an age:")
		b = int(a)
		print "Age is:",b
		if b <= 0:
			print "UNBORN"
		elif b > 0 and b <= 150:
			print "ALIVE"
		elif b > 150:
			print "VAMPIRE"
		else:
			print "NONE"
	except ValueError:
		print "Enter valid no"
def main():
	compare()
if __name__ == '__main__':
	main()