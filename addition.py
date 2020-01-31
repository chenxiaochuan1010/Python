def addition():
    """Addition of two given numbers"""

    try:
        a = input("Input a number A: ")
        a = int(a)

        b = input("Input a number B: ")
        b = int(b)
    except ValueError:
        print("Please input only integers!")
    else:
        sum = a + b
        print("The sum of %i and %i is %i" % (a, b, sum))

addition()
