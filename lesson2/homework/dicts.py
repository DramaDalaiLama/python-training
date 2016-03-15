import json

with open('lists.json') as data_file:
    data = json.load(data_file)

def make_dict(data):
    result = {}
    for key in data['keys']:
        try:
            result.update({key: data['values'][data['keys'].index(key)]})
        except:
            result.update({key: None})
    return result

print make_dict(data)
