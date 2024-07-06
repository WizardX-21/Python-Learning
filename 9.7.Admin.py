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

class Admin(User):
  def __init__(self, first_name, last_name, age, location, job):
    super().__init__(first_name, last_name, age, location, job)
    self.privileges = ['can add post', 'can delete post', 'can ban user']

  def show_privileges(self):
     print(f'Administrators set of privileges: ')
     for privilege in self.privileges:
      print(f'-{privilege}')  

User1 = Admin('Benton','tennison',21 , 'New york', 'Analyst') 
User1.describe_user()  
User1.show_privileges()