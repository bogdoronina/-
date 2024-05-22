


def count_H(expression):
    result = eval(expression)
    count = str(result).count('H')
    return count

expression = (105 + int('5F', 37) * int('1011', 3) ** int('BA', 15))
H_count = count_H(str(expression))
print(f"Количество букв 'H' в результате выражения: {H_count}")


