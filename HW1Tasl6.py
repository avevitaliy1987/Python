#  Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

n = int (input('Введите номер билета из 6 цифр: '))
a = n % 1000
i = n//100
c = i//10
d = int (1000000)
if n < d:
    print(a)
    print(c)

    num1 = a % 10
    k = a//10
    num2 = k % 10
    num3 = k // 10
    Summ_First = num1+num2+num3
    print(Summ_First)

    num4 = c % 10
    z = c //10
    num5 = z % 10
    num6 = z // 10
   
    Summ_Sec = num4+num5+num6
    print(Summ_Sec)
    if Summ_First == Summ_Sec:
        print('Вам попался счастливый билет!')
    else:
        print('Вам попался не счастливый билет.')
else:
    print('Вы ввели не шестизначное число!')