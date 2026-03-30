# TODO Напишите функцию для поиска индекса товара
def find_item_index(items_list, find_item): #проверим, есть ли товар в списке
    if find_item in items_list:
        return items_list.index(find_item) #если есть, вызываем его индекс
    else:
        return None #

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)
    if index_item is not None: #функция вызывается для каждого товара в списке
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

