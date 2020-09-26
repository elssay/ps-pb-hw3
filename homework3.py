account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

user_list = [user1, user2, user3, user4]

key1 = input('Введите ключ (name или account): ')
S=1
for i in user_list:
    print('значение ключа', key1.lower(), 'для юзера', S, '=', i[key1.lower()])
    S+=1

key2 = input('Введите порядковый номер: ')
user_n = user_list[int(key2)]
print(f"Данные по юзеру № {key2} \n{'имя'}: {user_n['name']} \n{'возраст'}: {user_n['age']}")
print(f"логин: {user_n['account']['login']} \n{'пароль'}: {user_n['account']['password']}")

print(user_list)
key3 = input('Введите номер пользователя, которого нужно переместить в конец: ')
user_list_n = user_list
end_user = user_list_n.pop(int(key3))
print(end_user['name'])
user_list_n.append(end_user)
print(user_list_n)
print(user_list)

s = 0
for j in user_list:
    s += j['age']
average_age = s/len(user_list)
print('Средний восзраст пользователей:', average_age)