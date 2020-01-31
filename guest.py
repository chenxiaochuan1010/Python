filename = 'guest.txt'

prompt = "\nEnter your name: "
prompt += "\nEnter 'q' to end the program."

msg = ""
while msg != 'q':
    msg = input(prompt)
    if msg != 'q':
        with open(filename, 'a') as f:
            f.write('\n' + msg)

