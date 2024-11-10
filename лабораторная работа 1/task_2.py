# TODO Найдите количество книг, которое можно разместить на дискете
size = 1.44
count_of_page = 100
count_of_line = 50
count_of_simbols = 25
bts = 4
total_symbols = count_of_page * count_of_line * count_of_simbols
total_bts = total_symbols * bts
disk_size = size * 1024 * 1024
count_of_book = round(disk_size / total_bts)
print("Количество книг, помещающихся на дискету:", count_of_book)
