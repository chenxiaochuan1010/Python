while True:
    try:
        a = input("Input A('q' for quit): ")
        if a != 'q':
            a = int(a)
        else:
            break

        b = input("Input B('q' for quit): ")
        if b != 'q':
            b = int(b)
        else:
            break
    except ValueError:
        print("You must input only integers!")
    else:
        sum = a + b
        print("The sum of %i and %i is %i.\n" % (a, b, sum))
