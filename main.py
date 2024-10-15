 
with open('text.txt', 'r', encoding='utf-8') as file:
    spis = f.read()
words=0
for line in file:
  words+=len(line.split())
  print("кол-во слов в файле : ", words)
