text=open('text.txt', encoding="utf-8")   #открываем нужный файл
print("Kol-vo slov : ", len(text.read().split())) #Вывод на экран текстa, кол-во слов 
text.close()#закрываем файл
