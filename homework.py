import math

print('Now we are going to learn a Math.')
a = input(print('Choice what you want learn + * / - :'))
if a == '+':
    print('Formula is a + b = x')
    print('Yoy can do a + b or b + a')
    b = input(print('Choice the first number :'))
    a = input(print('Choice the second number :'))
    x = int(a) + float(b)
    print('Answer is ' + str(x) )


elif a == '*':
    print('Formula is a * b = ab')
    print('You can do a*b or b*a')
    a = input(print('Choice the first number :'))
    b = input(print('Choice the second number :'))
    x = int(a) * float(b)
    print('Answer is :' + str(x))

elif a =='/':
    print ('Formula is a / b = a/b)
    print('You can`t do b / a')
    a = input(print('Type the first number : '))
    b = input(print'Type the second number : '))
    x = int(a) / float(b)
    print('Answer is ' + str(x))