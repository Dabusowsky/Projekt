import xml.etree.ElementTree as ET

def save_xml(data, file_path):
    try:
        data.write(file_path, encoding='utf-8', xml_declaration=True)
        print('XML saved successfully.')
    except (IOError, AttributeError) as e:
        print(f'Error saving XML: {e}')
