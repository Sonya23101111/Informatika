numb_of_sumb = 25 #Количество символов в строке
numb_of_srt = 50 #Число строк на странице
numb_of_page = 100 #Количество страниц в книге
info_vol_mb = 1.44 #Информационный объем дискеты, Мб
symb_weight = 4 #вес одного символа

book_weight = symb_weight * numb_of_page * numb_of_srt * numb_of_sumb  #вес одной книги
weight = info_vol_mb * 1024 * 1024 #Информационный объем дискеты
numb_of_books = int(weight // book_weight)

print("Количество книг, помещающихся на дискету:", numb_of_books)






