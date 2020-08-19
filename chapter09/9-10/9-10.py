# 导入Restaurant类
import restaurant

# 实例
Haagen_Dazs = restaurant.IceCreamStand("Häagen-Dazs")
Haagen_Dazs.flavors = ['strawberry', 'chocolate', 'oreo']

Haagen_Dazs.describe_restaurant()
Haagen_Dazs.show_flavors()


chongqinghuoguo = restaurant.Restaurant("chongqinghuoguo", "hotpot")
chongqinghuoguo.describe_restaurant()