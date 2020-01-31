filename = 'learning_python.txt'

with open(filename) as file_object:
    # contents = file_object.read()
    # print(contents.rstrip())

    # for line in file_object:
        # print(line.rstrip())

    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
