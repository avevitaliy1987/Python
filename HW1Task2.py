# Найдите сумму цифр трехзначного числа.
n = int (input('Введите ерехзначное число: '))
a = n % 10
i = n//10
b = i % 10
c = i//10
d = int (1000)
if n < d:
    
    print(a + b + c)
    print(a)
    print(b)
    print(c)
else:
    print('Вы ввели не трехзначное число!')