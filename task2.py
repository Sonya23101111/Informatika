salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

necessary_capital = 0.0

for _ in range(months):
    deficit = spend - salary #дефицит на текущий месяц
    necessary_capital += deficit #сумма, которую надо взять из подушки
    spend *= (1 + increase) #расход следующего месяца

if necessary_capital == int(necessary_capital):
    necessary_capital = int(necessary_capital)
else:
    necessary_capital = int(necessary_capital) #округление до целого числа
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", necessary_capital)

