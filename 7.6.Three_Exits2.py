#Using an Active Variable to Control How Long the Loop Runs
prompt = "Enter your age (or Enter 'quit' to finish): "
active = True
while active:
  age_input = input(prompt)

  if age_input.lower() == 'quit':
    active = False
  else:
    age = int(age_input)
    if age < 3:
      print("The ticket is free.")
    elif age >= 3 and age <=12:
     print("The ticket is $10.")
    elif age > 12:
     print("The ticket is $15.")  