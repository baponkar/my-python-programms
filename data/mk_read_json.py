import json

fileobj = open('example_2.json','rt')
menu = fileobj.read()
fileobj.close()
print(menu)
menu_json = json.dumps(menu)

print(menu_json)















