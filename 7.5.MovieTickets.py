prompt = "Enter your age: "
age = ""
while True:
  age = int(input(prompt))
  if age < 3:
    print("The ticket is free.")
  elif age >=3 and age <=12 :
    print("The ticket is $10")
  elif age > 12:
     print("The ticket is $15.")
     
  

