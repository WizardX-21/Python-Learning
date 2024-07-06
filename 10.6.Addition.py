def add_numbers():
  try:
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))
  except:
      print(f'Sorry,you need to enter valid numbers.')
  else:
       result = num1 + num2
       print(f'The result of adding {num1} and {num2} is {result}.')   
add_numbers()          
