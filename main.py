text = open('text.txt', encoding="utf-8") # Открываем нужный файл
print("Kol-vo slov : ", len(text.read().split())) # Вывод на экран текстa, кол-во слов 
text.close() # Закрываем файл
