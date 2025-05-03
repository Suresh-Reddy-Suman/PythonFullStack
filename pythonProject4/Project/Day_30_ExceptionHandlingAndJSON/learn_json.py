import json

try:
    with open('file.json', mode='r') as file:
        data = json.load(file)
except:
    with open('file.json', mode='w') as file:
        json.dump({}, file)
    with open('file.json', mode='r') as file:
        data = json.load(file)
finally:

    with open('file.json', mode='w') as new_version:
        data.update({'data': 'Keerthi'})
        json.dump(data, new_version, indent=4)
