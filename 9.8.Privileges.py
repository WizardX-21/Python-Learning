class User():
    def __init__(self, first_name, last_name, age, location, job):
        self.name = first_name
        self.last = last_name
        self.age = age
        self.location = location
        self.job = job

class Admin(User):
  def __init__(self, first_name, last_name, age, location, job):
    super().__init__(first_name, last_name, age, location, job)
    self.privileges = Privileges

class Privileges:
  def __init__(self, privileges = ['can add post', 'can delete post', 'can ban user']):
    self.privileges = privileges

  def show_privileges(self):
     print(f'Administrators set of privileges: ')
     for privilege in self.privileges:
      print(f'-{privilege}') 


User1 = Admin('Benton','tennison',21 , 'New york', 'Analyst') 
  
User1.privileges.show_privileges()     