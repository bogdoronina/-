x = int(input("Введите число:"))
n = 0
while(x > 0):
    d = x % 10
    n = n + d
    x = x//10
print("Сумма цифр равна:", n)

