#Egor
string_1=str(input("Введите 1 строку: "))#Ввод 1 строки пользователем
string_2=str(input("Введите 2 строку: "))#Ввод 2 строки пользователем
if sorted(string_1.lower())==sorted(string_2.lower()):
    print ("Строки анаграммы")
else:
    print ("Строки неанаграммы")