# prompt = "\nPlease enter the name of a city you have visited."
# prompt += "\n(Enter 'quit' when you are finished.)"

# while True:
    # city = input(prompt)

    # if city == 'quit':
        # break
    # elif city == '':
        # print("Input can't be blank. Please input again!")
    # else:
        # print("I'd love to go to %s!" % city.title())

def describe_city(city_name, city_country='China'):
    print("%s is in %s." % (city_name.title(), city_country.title()))

describe_city('wuhan')
describe_city(city_name='shanghai')
describe_city('tokyo', 'japan')
    
