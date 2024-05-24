my_dict = {'borsh': 'борщ', 'potato': 'картошка'}
print(f'Словарь: {my_dict}')
print(f"Cуществующий ключ: {my_dict.get('potato')}")
print(f"Отсутствующий ключ: {my_dict.get('salo')}")
my_dict.update({'cabbage': 'капуста', 'salo': 'сало'})
deleted_item = my_dict.pop('borsh')
print(f'Удаленное значение: {deleted_item}')
print(f'Обновленный словарь: {my_dict}')
my_set = {1, 2, 3, 'a', True, 1.23, 'a', (1, 2), (1, 2), 1, 2, 3}
print(f'Множество: {my_set}')
my_set.add(42)
my_set.add('Help')
my_set.remove(1)
print(f'Обновленное множество: {my_set}')