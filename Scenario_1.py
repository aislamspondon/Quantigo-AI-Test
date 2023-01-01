import json


def file_read(filename):
    with open(filename, "r") as f:
        data = json.load(f)
        return data


def check_class_title(filename):
    vehicle_presence = 0
    licence_plate_presence = 0
    check_file = file_read(filename)
    formatted_file = file_read('formatted_pos_0.png.json')[0]
    if check_file['objects']:
        for item in check_file['objects']:
            if item['classTitle'] == 'Vehicle':
                vehicle_presence += 1
            elif item['classTitle'] == 'License Plate':
                licence_plate_presence += 1
            else:
                vehicle_presence = 0
                licence_plate_presence = 0
    else:
        formatted_file = file_read('formatted_pos_10492.png.json')[0]

    formatted_file['dataset_name'] = filename
    formatted_file['annotation_objects']['vehicle']['presence'] = vehicle_presence
    formatted_file['annotation_objects']['license_plate']['presence'] = licence_plate_presence
    check_file['description'] = formatted_file

    return check_file


print(check_class_title('pos_10010.png.json'))


