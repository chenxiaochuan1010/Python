import json

filename = 'favorite_number.json'
try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    with open(filename, 'w') as f:
        prompt = "Let me know your favorite number: "
        favorite_number = input(prompt)
        json.dump(favorite_number, f)
        print("Number saved.")
else:
    prompt = "I know your favorite number!"
    prompt += " It's " + favorite_number + '.'
    print(prompt)

