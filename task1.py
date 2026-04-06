import json #Импортируем модуль

def task() -> float: #Объявляем функцию
    filename = "input.json" #Задаём имя файла для чтения
    with open(filename) as f: #Открываем файл для чтения
        json_data = json.load(f) #Загружаем данные из файла в переменную

    sum_values = sum([item["score"] * item["weight"] for item in json_data]) #Вычисляем сумму произведений для всех элементов
    return round(sum_values, 3) #Округляем результат до 3 знаков после запятой и возвращаем его

print(task()) #Вызываем task и выводим результат на экран.

