tax = float(input('Введите бюджет страны: '))
new_tax = float(input('Новые поступления (налог): '))

result = tax + new_tax
if abs(tax - result) < 1e-15:
    print('Результат: Бюджет не изменится')
else:
    print('Результат: Бюджет увеличится')