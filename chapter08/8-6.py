def city_country(name, country):
	return name.title()+", "+country.title()

city1 = city_country("hangzhou", "china")
city2 = city_country("newyork", "american")
city3 = city_country("beijing", "china")

print(city1)
print(city2)
print(city3)