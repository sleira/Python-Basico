import json
import time

# Construir un JSON
data = {
'name': 'anna',
'sex': 'woman',
'age': 20,
'country': 'germany'
}
blog = {
'title': 'my blog',
'created': time.time(),
'comments': [
{'name':'user 1', 'comment': 'this is comment 1'},
{'name':'user 2', 'comment': 'this is comment 2'},
{'name':'user 3', 'comment': 'this is comment 3'}
]
}

json_data = json.dumps(data)
json_data2 = json.dumps(blog)
print(json_data)
print(json_data2)

json_o1 = json.loads(json_data)
json_o2 = json.loads(json_data2)

print('----Datos_json_o1---')
print(json_o1['name'])
print(json_o1['sex'])
print(json_o1['age'])
print(json_o1['country'])

