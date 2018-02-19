import time

def fib(nr):
	a = 0
	b = 1
	while nr > 0:
		b = a + b
		a = b - a
		nr = nr-1

	print(a)
	
def fib_even_or_odd(nr):
	if nr%3 == 0:
		print("gerade")
	else:
		print("ungerade")
	
	
	
	
print("ex: (nr,fib_nr), (0,0), (1,1), (2,1), (3,2), (4,3), (5,5), (6,8)")	
nr = int(input("nr? "))

fib_even_or_odd(nr)
fib(nr)

time.sleep(10)