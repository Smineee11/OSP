#!/usr/bin/python
import sys

N= int(input("How many numbers? : "))
sum=0
for i in range (1,N+1):
	n = int(input("%d번째 숫자: " %(i)))
	sum += n

print(sum/N)



