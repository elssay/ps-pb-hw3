user_list = [{'name': 'Иван', 'gender': 'male'},
             {'name': 'Юлия', 'gender': 'female'},]

male_count = 0
female_count = 0

for user in user_list:
    if user['gender'] == 'male':
        male_count += 1
    elif user['gender'] == 'female':
        female_count += 1

print(f'Девочек: {female_count}')
print(f'Мальчиков: {male_count}')

#КОНСТАНТЫ:
GENDER_MALE = 'm'
GENDER_FEMALE = 'f'


user_list = [{'name': 'Иван', 'gender': GENDER_MALE},
             {'name': 'Петр', 'gender': GENDER_MALE},
             {'name': 'Марья', 'gender': GENDER_FEMALE},
             {'name': 'Дарья', 'gender': GENDER_FEMALE},
             {'name': 'Юлия', 'gender': GENDER_FEMALE},]

male_count = 0
female_count = 0

for user in user_list:
    if user['gender'] == GENDER_MALE:
        male_count += 1
    elif user['gender'] == GENDER_FEMALE:
        female_count += 1

print(f'Девочек: {female_count}')
print(f'Мальчиков: {male_count}')