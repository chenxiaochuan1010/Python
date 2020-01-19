def make_car(builder, model, **car_info):
    """Add properties to a car"""
    profile = {}
    profile['manufacturer'] = builder
    profile['model_name'] = model
    for key, value in car_info.items():
        profile[key] = value
    return profile

car = make_car('subaru', 'outback', color='blue', tow_package='True')
print(car)
