import json

filename = 'favorite_number.json'
with open(filename) as f:
    favorite_number = json.load(f)
print("I know your favorite number! It's %s." % favorite_number)
