filename = 'programming_pool.txt'

prompt = "Why do you like programming? Please tell me the reason: \n"
response = ''

while response != 'q':
    response = input(prompt)
    if response != 'q':
        with open(filename, 'a') as f:
            f.write(response + '\n')

