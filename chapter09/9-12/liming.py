from admin import Admin

# 实例
liming = Admin("li", "ming", "male")
liming.privileges.add_privileges(["can add post", "can delete post", "can ban user"])
liming.describe_user()
liming.privileges.show_privileges()