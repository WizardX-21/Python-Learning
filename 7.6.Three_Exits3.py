#Using a Break Statement to Exit the Loop
prompt = "Enter your age (or Enter 'quit' to finish): "
while True:
  age_input = input(prompt)

  if age_input.lower() == 'quit':
    print('Exiting the loop.')
    break
  else:
    age = int(age_input)
    if age < 3:
      print("The ticket is free.")
    elif age >= 3 and age <=12:
     print("The ticket is $10.")
  
    elif age > 12:
     print("The ticket is $15.")