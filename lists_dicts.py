lists = [3, 5, 7, 9 , 10.5]
print(lists)
lists.append('Python')
print(len(lists))
print(lists[0])
print(lists[-1])
print(lists[1:5])
lists.remove('Python')

dicts = {'city': 'Москва', 'temperature': '20'}
print(dicts['city'])
dicts['temperature'] = int(dicts['temperature']) - 5

print(dicts.get('country', 'Россия'))
dicts['date'] = '27.05.2019'
print(len(dicts))

