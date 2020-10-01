mylist=[1,2,3]
for i in range(2,100):
    j=i-1
    s=mylist[i]+mylist[j]
    mylist.append(s)
    if s>10000000:
        break
#print(mylist)
print('Количество элементов в последовательности:', len(mylist)-1)

summ = 0
print('Все четные элементы:')
for element in mylist[:-1]:
    if element%2 == 0:
        print(element,';',end = ' ')
        summ+= element

print('\n'+'Сумма всех четных элементов:', summ)
print('Предпоследнее число последовательности:', mylist[-3])