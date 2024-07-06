class User():
    def __init__(self, first_name, last_name, age, location, job):
        self.name = first_name
        self.last = last_name
        self.age = age
        self.location = location
        self.job = job
        

    def describe_user(self):
        print(f'\nSummary of the user information:')
        print(f'-{self.name.title()}')
        print(f'-{self.last.title()}')
        print(f'-{self.age}')
        print(f'-{self.location.title()}')
        print(f'-{self.job.title()}')      

    def greet_user(self):
        print(f'Your are welcome {self.name.title()} {self.last.title()}')

user1 = User('Benton','tennison',21 , 'New york', 'Analyst')
user2 = User('Kevin','korner',27 , 'Texas', 'Watcher')
user3 = User('Gwen','tennison',25 , 'Las Vegas', 'Keeper')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()


        