money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0

while money_capital + salary >= spend:
    #месяц без долгов
    money_capital = money_capital + salary - spend
    months += 1
    #увкличение расходов на след месяц
    spend *= (1 + increase)

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", months)

