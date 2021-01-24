#Что то похожее на резюме.
print('Приветсвуем!Мы принимаем на работу!Оставь резюме ниже!')
#answer`ы ответы user`ов
import math

a = input('Ваш опыт работы 2 или 3:')
n = input('Ваш возраст:21 или 22:')
s = input('Желаемая зарплата:3 или 5 k:')
w = input('Язык программирования: 1(C#) 2(Python)  3(C++)  4(Js) 5(Java):')

if a == 2:
    A = 2

elif a == 3:
    AA = 3

elif n == 21:
    N = 21

elif n == 22:
   NN = 22
    
elif s == 3:
    s = 3

elif s == 5:
    SS = 5

elif w == '1':
    w = 17

elif w == '2':
     w = 17.5
    
elif w == 3:
    w = 14

elif w == 4:
    w == 15

elif w == 5:
    w = 16


points = (int(a)  + int(n) + float(w) + int(s))
print('Ваши баллы за собеседование ' + str(points))


input()