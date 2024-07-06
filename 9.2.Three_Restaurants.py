class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name  # 'self' allows access to the instance attribute 'name'
        self.cuisine = cuisine  # 'self' allows access to the instance attribute 'cuisine'
        
    def describe_restaurant(self):
        print('The two pieces of information are:')
        print(self.name.title())  # 'self' allows access to the instance attribute 'name'
        print(self.cuisine.title())  # 'self' allows access to the instance attribute 'cuisine'

    def open_restaurant(self):
        print(f'The {self.name.title()} is open now!')  # 'self' allows access to the instance attribute 'name'

restaurant1 = Restaurant('Black coffee', 'Spanish')
restaurant2 = Restaurant('Green Garden', 'Italian')
restaurant3 = Restaurant('Sushi Place', 'Japanese')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

