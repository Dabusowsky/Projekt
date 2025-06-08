import xml.etree.ElementTree as ET

def load_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        print('XML loaded successfully.')
        return root
    except (FileNotFoundError, ET.ParseError) as e:
        print(f'Error loading XML: {e}')
        return None
