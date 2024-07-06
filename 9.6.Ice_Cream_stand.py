class Restaurant:
    def __init__(self, name, cuisine, ):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f'\nThe two pieces of information are: ')
        print('-'+self.name.title())    
        print('-'+self.cuisine.title())  

    def open_restaurant(self):
        print(f'The {self.name.title()} is open now!')

    def set_number_served(self, number):
         self_number_served = number

    def increment_number_served(self, number):
        self.number_served += number

#Create an instance of Restaurant class.
restaurant = Restaurant('Black Coffee', 'Spanish')      

print(f'The number of customers served: {restaurant.number_served}')
print(f'The number of customers served after changed: {restaurant.number_served}')

#Update the number of customers served.
restaurant.set_number_served(10)
print(f'The number of customers served after setting: {restaurant.number_served}')

#Increment the number of customers served.
restaurant.increment_number_served(7)
print(f'The number of customers served after incrementing: {restaurant.number_served}')

#Define the IceCreamStand that inherits from Restaurant
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine,):
        super().__init__(name, cuisine,)
        self.flavor = ['Vanilla','Chocolate','Mango', 'Creamy']
        
    def dispaly_flavor(self):
        print(f'The flavors are:')
        for flavor in self.flavor:
            print('-' + flavor)

Favourite = IceCreamStand('Cold Icecreams', 'Premium')       
Favourite.describe_restaurant()
Favourite.dispaly_flavor()

        
        
            