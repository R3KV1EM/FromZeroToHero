mylist = [13, 25, 31, 44, 55] # При цикле возвращается каждое число по очереди. Сколько переменных столько циклов
n = len(mylist) # автоподставка в range по длинне листа
for i in range(n):
    print(i,mylist[i]) # Принтим этап цикла + index значения
    mylist[i] += 5 # Подставляем в каждый цикл + 5
    print(mylist)
print(mylist)





# ОБход по значениям
#for i in mylist:
#    print(i, mylist.index(i))