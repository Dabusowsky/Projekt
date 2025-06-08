import json

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print('JSON loaded successfully.')
            return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Error loading JSON: {e}')
        return None
