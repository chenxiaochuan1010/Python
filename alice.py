filename = 'alice.txt'

try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    msg = "Sorry, the file %s does not exist." % filename
    print(msg)
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print("The file %s has about %i words." % (filename, num_words))
