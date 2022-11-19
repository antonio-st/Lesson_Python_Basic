"""
#оператор elif

x = int(input())
if x == 1:
    print('one')
elif x == 4:
    print('four')
elif x == 11:
    print('eleven')
else:
    print('other')


#Даны два целых числа. Программа должна вывести число 1, если первое число больше второго, число 2, если второе больше первого или число 0, если они равны.
#Эту задачу нужно решить с помощью конструкций if-elif

x = int(input())
y = int(input())
if x > y:
    print(1)
elif y > x:
    print(2)
elif x == y:
    print(0)

#В математике функция sign(x) (знак числа) определена так:
#sign(x) = 1, если x > 0,
#sign(x) = -1, если x < 0,
#sign(x) = 0, если x = 0.
#Для данного числа x выведите значение sign(x).

x = int(input())
if x > 0:
    print(1)
elif x < 0:
    print(-1)
elif x == 0:
    print(0)

#Даны три целых числа. Найдите наибольшее из них (программа должна вывести ровно одно целое число).
x = int(input())
y = int(input())
z = int(input())

if x > y and x > z:
    print(x)
elif y > x and y > z:
    print(y)
else:
    print(z)

#Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
#Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с
#григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.

x = int(input())
if  x % 4 == 0 and not x % 100 == 1:
    print('YES')
elif x % 400 == 0:
    print('YES')
else:
    print ('NO')
"""
#Даны три целых числа A, B, C. Выведите YES, есть ли среди них хотя бы одно четное и хотя бы одно нечетное, и NO в противном случае.

A = int(input())
B = int(input())
C = int(input())
if A % 2 == 0 and B % 2 == 1 and C % 2 == 1:
    print('YES')
elif A % 2 == 0 and B % 2 == 0 and C % 2 == 1:
    print('YES')
elif A % 2 == 0 and B % 2 == 1 and C % 2 == 0:
    print('YES')
elif A % 2 == 1 and B % 2 == 1 and C % 2 == 0:
    print('YES')
elif A % 2 == 1 and B % 2 == 0 and C % 2 == 0:
    print('YES')
elif A % 2 == 1 and B % 2 == 0 and C % 2 == 1:
    print('YES')
else:
    print('NO')

