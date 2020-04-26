#!/usr/bin/python

import re
from my_pkg.BinaryConv import *
from my_pkg.IntersectUnion import *

if __name__ == '__main__':
	n=0

	while n == 0:
		menu = input("Select menu: 1) conversion  2)union/intersection  3) exit ?  ")
		if(menu == "1"):
			num = input("input binary number: ")
			print("=> OCT> %s" %octa(num))
			print("=> DEC> %s" %deci(num))
			print("=> HEX> %s" %hexadec(num))
			
		elif(menu == "2"):
			input1 = input("1st list: ")
			re1 = re.sub('[^0-9]+', ' ', input1)
			list1 = re1.split()
			
			input2 = input("2nd list: ")
			re2 = re.sub('[^0-9]+', ' ', input2)
			list2 = re2.split()
			
			print("=>union ", end= '')
			print(uni(list1,list2))
			print("=>intersection ", end= '')
			print(ins(list1,list2))
			

		elif(menu == "3"):
			print("exit the program...")
			n=1


