def city_country(city_name, country_name):
    city_formatted = '\"' + city_name + ', ' + country_name + '\"'
    return city_formatted.title()

city1 = city_country('beijing', 'china')
city2 = city_country('tokyo', 'japan')
city3 = city_country('berlin', 'germany')
print(city1)
print(city2)
print(city3)
