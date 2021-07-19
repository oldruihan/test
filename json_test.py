import json

jsonfile = open("naruto.json",'a',encoding="utf-8")



with open("naruto.json", encoding="utf-8") as f:
    data = json.load(f)

print(len(data))

sample = {"entity_1": "千手纲手","entity_2": "加藤断","relationship": "女友"}



