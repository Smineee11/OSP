#!usr/bin/python

n = int(input("fibonacci number?: "))

a = [1,1]
for i in range(2,n):
	a.append(a[i-2]+a[i-1])

for i in range(len(a)):
	print(a[i], end = '', flush = True)
	if(i!=len(a)-1):
		print(',', end = '', flush = True)
print()
print("F%d = %d" %(n, a[n-1]))
