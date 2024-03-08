import json
with open("sample-data.json", "r") as f:
    j = json.load(f)
for x in j['imdata']:
    del x
print(j)