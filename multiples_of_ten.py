number = input("\nInput your number, I'll tell you if the number is a multiple of 10 or not: ")
number = int(number)

if number >= 10 and number % 10 == 0:
    print("\nThe number %i is a multiple of 10." % number)
else:
    print("\nThe number %i is NOT a multiple of 10." % number)
