import yaml

def save_yaml(data, file_path):
    try:
        with open(file_path, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
            print('YAML saved successfully.')
    except (IOError, TypeError) as e:
        print(f'Error saving YAML: {e}')
