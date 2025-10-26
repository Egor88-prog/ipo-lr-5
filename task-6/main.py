#Egor
with open("task-6\\text.txt","r") as infile , open("task-6\\output.txt","w") as outfile:#открытие 
    for i, line in enumerate(infile,1):#цикл перебора строк и счет строки
        outfile.write(f"{i}. {line}")#запись номера строки и самой строки
        
