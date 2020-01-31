filename = 'guest_book.txt'

prompt = "\nEnter your name"
prompt += "\nEnter 'q' to end the program: "

name = ""
while name != 'q':
    name = input(prompt)
    print("Hello %s" % name.title())
    if name != 'q':
        with open(filename, 'a') as f:
            f.write(name.title() + " has logged in." + '\n')

