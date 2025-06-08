import json

def save_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            print('JSON saved successfully.')
    except (IOError, TypeError) as e:
        print(f'Error saving JSON: {e}')
