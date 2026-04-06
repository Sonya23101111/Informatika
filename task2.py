import csv #Импортируем модуль
import json #Импортируем модуль

INPUT_FILENAME = "input.csv" #Задаём имя входного файла
OUTPUT_FILENAME = "output.json" #Задаём имя выходного файла

def task() -> None: #Объявляем функцию, которая ничего не возвращает
    with open(INPUT_FILENAME) as f: #Открываем CSV‑файл для чтения
        lines = [line for line in csv.DictReader(f)] #Каждая строка в словарь, все словари в список

    with open(OUTPUT_FILENAME, "w") as f: #Открываем файл для записи
       json.dump(lines, f, indent=4) #Записываем список lines в файл с отступами 4 пробела


if __name__ == '__main__':
    # Нужно для проверки
    task() #

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
