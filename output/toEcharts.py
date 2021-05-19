
import os
import json

def parse_file_info(file):
    words = file.replace('.json', '').split('-')
    return {
        'datatype': words[0],
        'command': words[1],
        'number': words[2],
        'size': words[3]
    }
    
def extract_scores(file):
    result = {}
    with open(file) as fh:
        content = fh.read()
        json_obj = json.dumps(content)
        print(json_obj)

cwd = os.getcwd()
for file in os.listdir(cwd):
    if os.path.isfile(file) and file.endswith('.json'):
        fileInfo = parse_file_info(file)
        # print(fileInfo)
        scores = extract_scores(file)