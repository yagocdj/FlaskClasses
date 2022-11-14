# d = {'key1': 'value1', 'key2': 'value2'}
# print(d)
# print(d['key1'])

salaries = {'John': 20, 'Sally': 30, 'Sammy': 15}
salaries['Cindy'] = 100
salaries['John'] = salaries['John'] + 40
# or
# salaries['John'] = 30
print(salaries['Sally'])
print(salaries['Cindy'])

people = {'Carla': {'salary': 10, 'age': 30}, 'Maria': [40, 10, 30]}
print(people['Maria'][0])
print(people['Carla']['age'])

d = {'k1': 10, 'k2': 20, 'k3': 30}
print(d.keys())
print(d.values())
print(d.items())