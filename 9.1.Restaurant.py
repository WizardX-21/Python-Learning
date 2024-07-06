class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name  # 'self' allows access to the instance attribute 'name'
        self.cuisine = cuisine  # 'self' allows access to the instance attribute 'cuisine'

    def open_restaurant1(self):
        print('The two pieces of information are:')
        print(self.name.title())  # 'self' allows access to the instance attribute 'name'
        print(self.cuisine.title())  # 'self' allows access to the instance attribute 'cuisine'

    def open_restaurant2(self):
        print(f'The {self.name.title()} is open now!')  # 'self' allows access to the instance attribute 'name'

best_restaurant = Restaurant('Black coffee', 'Spanish')
best_restaurant.open_restaurant1()
best_restaurant.open_restaurant2()
