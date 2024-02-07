x = None
n= {}

for number in map(int, input("Введите числа : ").split()):
    y = sum(map(int, str(number)))
 
    if (x is None) or (y > x):
        x= y
        result = [number]
    elif y == x:
        result.append(number)

print(f"Ответ: {result}")