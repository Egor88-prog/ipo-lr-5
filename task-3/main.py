#Egor
with open("text.txt","r") as file:#открытие файла
    lines=file.readlines()#нахождение количества строк в файле
print(f"В файле {len(lines)} строки")