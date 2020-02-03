def formmated_city_country_name(city, country, population=''):
    """Return a single string: City, Country - population xxx"""
    if population:
        city_country_name = city.title() + ', ' + country.title()
        city_country_name +=  ' - population ' + str(population)
    else:
        city_country_name = city.title() + ', ' + country.title()
    return city_country_name
