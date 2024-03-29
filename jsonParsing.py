import json


color = '{"name": "Rahul", "languages": ["Java", "Python"]}'

#Loads method parse Json string and it returns dictionary
dict_colors = json.loads(color)
print(type(dict_colors))
print(dict_colors)
print(dict_colors['name'])
print(dict_colors['languages'])
list_languages = dict_colors['languages']
print(list_languages[0])

#*************** Parse content in Json File *****************
with open('C:\\Users\\USER\\Documents\\Python Softserve\\Ejercicios\\Ejercicios\\prueba.json') as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data['shipTo'])
    dict_two = data['shipTo']
    print(dict_two['address'])

exampleJSON = (
    '{"test1":[{"lang1": "Java", "lang2": "Python", "other":["fortran", "go", "C"]}]}')

data = json.loads(exampleJSON)

print(data["test1"][0]["other"][1])