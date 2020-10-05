s=0
for i in range(1000, 20001):
    if i % 3 == 0 and i % 5 == 0: #задаем условие - число должно одновременно быть кратным 3 и 5
        s+=i
print(s)
    
    
count = input('Введите число:')
if int(count)%3 == 0 and int(count)%5 == 0:
    print('FIZZBUZZ')
elif int(count)%3 == 0:
    print('FIZZ')
elif int(count)%5 == 0:
    print('BUZZ')
else:
    print('Это число не делится ни на 5, ни на 3')