class Restaurant:
    def __init__(self, name, cuisine, ):
        self.name = name  
        self.cuisine = cuisine  
        self.number_served = 0 #Default value of 0.
      
    def describe_restaurant(self):
        print('The two pieces of information are:')
        print(self.name.title())  # 'self' allows access to the instance attribute 'name'
        print(self.cuisine.title())
        
    def open_restaurant(self):
        print(f'The {self.name.title()} is open now!') 

    def set_number_served(self,number):
        self.set_number_served = number

    def increment_number_served(self, number):
        self.number_served += number

#Creating an instance of the Restaurant class
restaurant = Restaurant('Black Coffee', 'Spanish')

#Print the number of the customers the restaurant has served
print(f'The number of customers served: {restaurant.number_served}')

#Change this value and print it again
restaurant.number_served  = 5
print(f'The number of customers served after changed: {restaurant.number_served}')

#Use the set_number_served() method and print the value again.
restaurant.set_number_served(10)
print(f'The number of customers served after setting: {restaurant.number_served}')

#Use the increment_number_served() method and print the value again.
restaurant.increment_number_served(7)
print(f'The number of customers served after incrementing: {restaurant.number_served}')

       