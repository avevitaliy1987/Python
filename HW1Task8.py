#  Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите количество долек в длину: '))
m = int(input('Введите количество долек в ширину: '))
k = int(input('Введите количество долек, которое хотите отломить: '))

a = k/m
b = k/m
c = m*n

if k<c:

    if k == m or k == n :
        print('Дольки можно отломить')
    elif int(a) == a or int(b) == b:
        print('Дольки можно отломить')
    else:
        print('Такое количество долек не мозможно отломить одним надломом!')
else:
    print('Количество долек превышает существующее либо не требует надлома!')
