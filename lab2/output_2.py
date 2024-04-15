class UserType:
    ENGINEER = 1
    MANAGER = 2

class User:
    def __init__(self, name, age, user_type, phone):
        self.name = name
        self.age = age
        self.user_type = user_type
        self.phone = phone

    def print_details(self):
        user_type_str = "Engineer" if self.user_type == UserType.ENGINEER else "Manager"
        print("Name:", self.name)
        print("Age:", self.age)
        print("Type:", user_type_str)
        print("Phone:", self.phone)

user = User("John", 25, UserType.ENGINEER, "0509379992")
user.print_details()
