def word_counter(filename, word):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print("The file doesn't exist. Please check it again!")
    else:
        times = contents.lower().count(word)
        print("The word '%s' appears %i times in this file." % (word, times))

filename = 'alice.txt'
word_counter(filename, 'alice')
