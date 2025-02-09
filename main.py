from fractions import Fraction

def int_to_hex(n):
    return format(n, 'x')

def fraction_operations(frac1, frac2):
    f1 = Fraction(frac1)
    f2 = Fraction(frac2)
    return f1 + f2, f1 * f2

if __name__ == "__main__":
    num_hex = int(input("Введите целое число для перевода в шестнадцатеричный формат: "))
    print(f"Шестнадцатеричное представление: {int_to_hex(num_hex)} (проверка: {hex(num_hex)})")

    frac1 = input("Введите первую дробь (в формате a/b): ")
    frac2 = input("Введите вторую дробь (в формате a/b): ")
    sum_frac, prod_frac = fraction_operations(frac1, frac2)
    print(f"Сумма дробей: {sum_frac}")
    print(f"Произведение дробей: {prod_frac}")
