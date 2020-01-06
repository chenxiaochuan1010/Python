sandwich_orders = ['steak with blue cheese', 'pastrami with slaw',
        'corned beef with horseradish slaw', 'roast beef and smoked gouda',
        'spicy roast beef and brie', 'italian deli']

finished_sandwiches = []

while sandwich_orders:
    sandwich_made = sandwich_orders.pop()
    print("I made you %s." % sandwich_made.title())
    finished_sandwiches.append(sandwich_made)

# List all sandwiches been made
print("\nHere's a list of all sanwiches those have been made:")
for sandwich in finished_sandwiches:
    print(' - ' + sandwich.title())
