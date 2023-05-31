import json
import yaml
with open('myfile.json','r') as json_file:
    ourjson = json.load(json_file)
print("\n\n---")
print(yaml.dump(ourjson))
