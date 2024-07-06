import random

class Die:
  def __init__(self,sides = 6):
    self.sides = sides

  def roll_die(self):  
    return random.randint(1, self.sides) 

#Create a 6-sided die and roll it 10 times
six_sided_die = Die()
print("Rolling a 6-sided die 10 times:")
for _ in range(10):
  print(six_sided_die.roll_die())

#Create a 10-sided die and roll it 10 times
ten_sided_die = Die(10)
print("Rolling a 6-sided die 10 times:")
for _ in range(10) :
  print(six_sided_die.roll_die())

#Create a 10-sided die and roll it 10 times.
twenty_sided_die = Die(20)
print("\nRolling a 20-sided die 10 times:")
for _ in range(10):
  print(twenty_sided_die.roll_die())   