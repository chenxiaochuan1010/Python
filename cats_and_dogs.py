def print_to_screen(filename):
    """Read lines of a file, and print out each line."""
    try:
        with open(filename) as f:
            lines = f.readlines()
        print("\nReading file: %s" % filename)
        for line in lines:
            print(line.rstrip())

    except FileNotFoundError:
        print("The file %s does not exist." % filename)
        # pass # fail silently

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    print_to_screen(filename)
