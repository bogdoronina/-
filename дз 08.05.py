


def count_zeros_in_ternary(expression):
    zeros_count = 0
    for char in expression:
        if char == '0':
            zeros_count += 1
    return zeros_count

result = 4**3 * 3**19
result_in_ternary = ""

while result > 0:
    remainder = result % 3
    result //= 3
    result_in_ternary = str(remainder) + result_in_ternary

print(f"Значение выражения 4^3 * 3^19 в троичной системе: {result_in_ternary}")
print(f"Количество нулей в данной записи: {count_zeros_in_ternary(result_in_ternary)}")