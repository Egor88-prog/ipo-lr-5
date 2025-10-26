#Egor
string=str(input("Введите строку: "))#Ввод строки пользователем
glt=0
slt=0
i=0
len_string=len(string) #Нахождение длины сторки
g_letter=("аоуэюияеёы")#гласные буквы
s_letter=("бвгджзйклмнпрстфхцчшщ")#сщгласные буквы

while i<len_string:#цикл подсчёта гласных и согласных букв
    if string[i]in g_letter or string[i].lower() in g_letter:
        glt+=1
    elif string[i]in s_letter or string[i].lower() in s_letter:
        slt+=1
    i+=1

print (f"длина строки= {len_string}")
print (f"количество гласных= {glt}")
print (f"количество согласных= {slt}")