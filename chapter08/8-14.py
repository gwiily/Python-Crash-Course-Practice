def make_car(manufacturer, model, **other_info):
	car_info={}
	car_info['manufacturer'] = manufacturer
	car_info['model'] = model
	for key, value in other_info.items():
		car_info[key] = value

	return car_info


car_info = make_car('honda', 'accord', year=1991, color='white', headlights='popup')
print(car_info)