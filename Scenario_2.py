import json


new_data = []

files = ['pos_0.png.json', 'pos_10010.png.json', 'pos_10492.png.json']
change_data = {
    'Vehicle': 'Car',
    'License Plate': 'Number'
}

keys = list(change_data.keys())


def file_read(filename):
    with open(filename, "r") as f:
        data = json.load(f)
        for item in data['objects']:
            if item['classTitle'] in keys:
                item['classTitle'] = change_data[item['classTitle']]
        return data


for dataItem in files:
    combined_data = file_read(dataItem)
    new_data.append(combined_data)

with open('new_data.json', 'w') as f:
    json.dump(new_data, f)






