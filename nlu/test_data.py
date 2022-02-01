import yaml

data = yaml.safe_load(open('nlu\\train.yml', 'r', encoding='utf-8').read())

for cmd in data['commands']:
    print(cmd)