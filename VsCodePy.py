import math
what = input("+ or - * / zero :")

a = float(input('Type first number:'))
b = float(input('Type second number:'))

if what =='+':
	c = a + b
	print('Answer is :'  + str(c) )

elif what =='-':
	c = a - b
	print( 'Answer is :' + str(c) )

elif what == '*':
	c = a * b
	print('Answer is :' + str(c) )

elif what == '/':
	c = a / b
	print('Answer is:'  + str(c) )
elif what == 'zero':
	c = -c
	print( c )
else:
	print('Uncorrect ! ! !')


	input()