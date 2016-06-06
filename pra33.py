#!/usr/bin/python

####### Code written by Shah Bhavisha ##########
####### This code is for comparing that the no is divisible by 2 and 3 ###### 

import sys
import math
def compare():
	try:
		a = raw_input("Enter an number:") ####Taking An input####
		n = int(a)
		print "Number:",n
		while n >=0:
			if n%2 == 0 and n%3 == 0:
				print "BOTH"
				break
			elif (n%2 == 0 and n%3 != 0) or (n%2 != 0 and n%3 == 0):
				print "ONE"
				break
			elif n%2 != 0 and n%3 !=0:
				print "NEITHER"
				break
			else:
				print "NONE"
				break
			print "Please enter positive number"
	except ValueError:
		print "Enter valid no"
def main():
	compare()
if __name__ == '__main__':
	main()