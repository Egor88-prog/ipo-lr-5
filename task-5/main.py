#Egor
string=str(input("Введите строку: "))#Ввод строки пользователем
i=0
while i< len(string):#цикл поиска всех индексов е
    if string[i] == "е":
        print(i)
    i+=1