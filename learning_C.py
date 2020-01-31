filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.rstrip()
    line = line.replace('Python', 'C')
    print(line)

