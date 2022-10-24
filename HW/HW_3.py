"""
3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
"""
my_list = ['a', 'b', [1, 2, 3], 'd']
for i in my_list[2]:
    print(i)

print("===========1==========\n")

"""
3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
   - получите сумму всех чисел,
   - распечатайте все строки, где есть буква 'a'
"""
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
print(sum([i for i in list_1 if str(i).isdigit()]))
print(" ")
print("Using lambda and filter\n")
print(sum(filter(lambda x: isinstance(x, int), list_1)))

# все строки, где есть буква 'a'
index = 0  # выводит выбранные слова столбиком по одному
count = 0
for x in list_1:
    y = list_1[index]
    if type(y) == str and "a" in y:
        if count == 0:
            print("Все строки, где есть буква 'a': ")
            count += 1
        print(y)
        index += 1
    else:
        index += 1
print(" ")
print("Using list comprehension")
print([x for x in list_1 if isinstance(x, str) and 'a' in x])  # выводит список слов
print("===========2==========\n")
"""
3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
"""
list_words = ['cat', 'dog', 'horse', 'cow']
tuple1 = tuple(list_words)
print(tuple1)
print(tuple(list_words))
print("===========3==========\n")
"""
3.4. Напишите программу, которая определяет, какая семья больше. 
      1) Программа имеет два input() - например, family_1, family_2. 
      2) Членов семьи нужно перечислить через запятую. 
     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
"""
family_1 = tuple(input('Введите текст через запятую: ').split(',')) # метод split(',') - сканирует всю строку и разделяет ее в случае нахождения разделителя
family_2 = tuple(input('Введите текст через запятую: ').split(','))
if len(family_1) == len(family_2):
    print('Equal')
elif len(family_1) > len(family_2):
    print("family_1")
else:
    print("family_2")
print("==========4===========\n")
"""
3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
    о вашем любимом фильме. 
    - распечатайте только ключи
    - распечатайте только значения
    - распечатайте пары ключ - значение
"""
film = {
    "title": "Хранители снов",
    "director": "Питер Рэмси",
    "year": "2012",
    "budget": "Фэнтези",
    "main_actor": "Ледяной Джек",
    "slogan": "Время",
}
print(*film.keys())
print(*film.values())
print(*film.items())
print("==========5===========\n")
"""
3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
"""
my_dictionary = {"num1": 375, "num2": 567, "num3": -37, "num4": 21}
print(sum(my_dictionary.values()))
print("============6=========\n")
"""
3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1] 
"""
list_37 = [1, 2, 3, 4, 5, 3, 2, 1]
# new_list37 = list(set(list_37))
# print(new_list37)
print(list(set(list_37)))
print("===========7==========\n")
"""
3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     - найдите значения, которые встречаются в обоих множествах
     - найдите значения, которые не встречаются в обоих множествах
     - проверьте являются ли эти множества подмножествами друг друга 
"""
set1 = {"a", "z", 1, 5, 9, 12, 100, "b"}
set2 = {5, "z", 1, 8, 9, 21, 100, "l", 785}
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))
print(set1.issubset(set2))
print(set2.issuperset(set1))
print("===========8==========")

