#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
#pizza names in a list, and then use a for loop to print the name of each pizza.
pizzas=['Margherita','Pepperoni','Hawaiian','Veggie']
for pizza in pizzas:
  print(pizza)
  print(f"I like {pizza} pizza.\n")
print(f'I really love pizza!')  
#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
#(page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
#Then, do the following:
#•	 Add a new pizza to the original list.
#•	 Add a different pizza to the list friend_pizzas.
#•	 Prove that you have two separate lists. Print the message, My favorite
#pizzas are:, and then use a for loop to print the first list. Print the message,
#My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
friends_pizza=pizzas[:]
pizzas.append('water')
print(f"My favourite pizzas are:")
for items in pizzas:
  print(items)

print(f"My friend's favourite pizzas are:")  
for items in friends_pizza:
  print(items)

