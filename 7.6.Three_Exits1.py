#Using a conditional Test in while statement.
prompt = "Enter your age: "
age = 0
while age != -1:
  age = int(input(prompt))
  
  if age == -1:
    print("Exiting the loop.")
    break
  elif age < 3:
    print("The ticket is free.")
  elif age >= 3 and age <=12:
    print("The ticket is $10.")
  elif age > 12:
    print("The ticket is $15.")   


