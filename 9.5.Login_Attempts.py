class User:
    def __init__(self, first, last, age, location, job,):
        self.First = first
        self.Last = last
        self.age = age
        self.Location = location
        self.job = job
        self.login_attempts = 0#Initialize login attempts to 0.

    def describe_user(self):
        print(f'\nSummary of the user information:')
        print(f'-{self.First.title()}')
        print(f'-{self.Last.title()}')
        print(f'-{self.age}')
        print(f'-{self.Location.title()}')    
        print(f'-{self.job.title()}')   

    def greet_user(self):
        print(f'Your are welcome {self.First.title()} {self.Last.title()}')     
       
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

#Creating instances of User class:
user1 = User('Benton','tennison',21 , 'New york', 'Analyst')
user2 = User('Kevin','korner',27 , 'Texas', 'Watcher')
user3 = User('Gwen','tennison',25 , 'Las Vegas', 'Keeper')

#Calling describe_user and greet_user methods for each instance
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

#Incrementing login attempts several times for user1
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f'\nLogin attempts for {user1.First} {user1.Last} : {user1.login_attempts}')

#Resetting login_attempts for user1
user1.reset_login_attempts()
print(f'Login attempts for {user1.First} {user1.Last} after reset : {user1.login_attempts}')
