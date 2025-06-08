import yaml

def load_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            print('YAML loaded successfully.')
            return data
    except (FileNotFoundError, yaml.YAMLError) as e:
        print(f'Error loading YAML: {e}')
        return None
