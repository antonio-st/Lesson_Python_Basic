# Задача №1 - вычисляем расстояние
print('# Задача №1 - вычисляем расстояние')
print('Дано:')
speed = 7
print('Скорость:', speed, "км/ч")
time = 1.5
print('Время:', time, 'часа')
dist = speed * time
print('Расстояние', dist, 'км')
print('*********************************************')


# Задача №2 - вычисляем скорость
print('# Задача №2 - вычисляем скорость')
print('Дано:')
rastoyanie = 8
print('Расстояние:', rastoyanie, "км")
time = 1.5
print('Время:', time, 'часа')
V = rastoyanie / time
print('Скорость',V, 'км/ч')
print('*********************************************')
# Задача №3- вычисляем U
print('# Задача №3- вычисляем U')
print('Дано:')
I = 102341132412344234
print('Напряжение', I , 'А')
R = 9876387639476324727
print('Сопротивление', R , 'Ом')
U = I*R
print('U =', I ,'*', R)
print('Напряжение U=', U, 'Вольт')
print('*********************************************')
# Задача №4 про белочек
print('# Задача №4 про белочек')
bel=60
oreh=38746298762973632324233242
result1=oreh//bel
print(result1, 'орешков на белочку')
print('*********************************************')
# Часы показывали полночь. Прошло 38746298762973632324233242 минут. Сколько полных часов прошло? В качестве ответа необходимо сдать целое число.
print('Задача №5 # Часы показывали полночь. Прошло 38746298762973632324233242 минут. Сколько полных часов прошло? В качестве ответа необходимо сдать целое число.')
min = 38746298762973632324233242
hour = min//60
print(hour, 'полных часов прошло')
print('*********************************************')
# 60 белочек делили поровну 38746298762973632324233242 орехов. Каждая белочка забрала свои орехи. Сколько орехов осталось?
print('Задача №6 60 белочек делили поровну 38746298762973632324233242 орехов. Каждая белочка забрала свои орехи. Сколько орехов осталось?')
oreh=38746298762973632324233242
res1=oreh % 60
print(res1, 'осталось орешков')
print('*********************************************')
# Минутная стрелка показывала на 0 минут. Прошло 38746298762973632324233242 минут. Куда показывает минутная стрелка?
print('# Минутная стрелка показывала на 0 минут. Прошло 38746298762973632324233242 минут. Куда показывает минутная стрелка?')
proshlo = 38746298762973632324233242
result  = proshlo % 60
print(result , ' мин')


