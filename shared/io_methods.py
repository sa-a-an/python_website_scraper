import csv
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def write_to_csv(data: list, file_path: str, filename: str, delimiter: str = ';', dirname: str = 'out') -> None:
    if not os.path.exists(os.path.join(file_path,dirname,filename + '.csv')):
        my_file = open(os.path.join(file_path,dirname,filename + '.csv'), "w+")
        my_file.close()
    with open(os.path.join(file_path,dirname,filename + '.csv'),'a+',encoding='utf-8',newline='') as handler:
        writer = csv.writer(handler,delimiter = delimiter)
        writer.writerow(data)

def read_from_json(json_path: str) -> json:
    with open(json_path, 'r', encoding='utf-8') as handler:
        json_data = json.load(handler)
        
    return json_data

def read_from_txt(filename: str, file_path: str, dirname: str = 'in') -> list:
    data = []

    with open(os.path.join(file_path, dirname, filename + '.txt'),'r', encoding='utf-8') as file:
        for line in file:
            data.append(line.replace('\n', ''))
    
    return data

def read_from_html(filename: str, file_path: str, dirname: str = 'in') -> list:
    data = []

    with open(os.path.join(file_path, dirname, filename + '.html'),'r', encoding='utf-8') as file:
        for line in file:
            data.append(line.replace('\n', ''))
    
    return ''.join(data)

def read_from_csv(filename: str, file_path:str, delimiter: str = ';',dirname: str= 'in') -> list:
    data = []

    with open(os.path.join(file_path,dirname,filename + '.csv'),'r', newline ='',encoding='utf-8') as handler:
        reader = csv.reader(handler,delimiter=delimiter)
        for row in reader:
            data.append(row)

    return data
