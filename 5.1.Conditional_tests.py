#5-1. Conditional Tests: Write a series of conditional tests. Print a statement
#describing each test and your prediction for the results of each test.
food='mango'
print("Is food == 'mango'?I predict True.")
print(food=='mango')

print(f"\nIs food =='apple'? I predict false.")
print(food=='apple')
#•	 Tests for equality and inequality with strings
pizzas=['Margherita','Pepperoni','Hawaiian','Veggie']
print(pizzas=='Veggie')
print(pizzas != 'Water')
#Tests using the lower() function
print(pizzas[3].lower()=='veggie')
#Tests using the and keyword and the or keyword
print((pizzas=='veggie'and pizzas=='Veggie'))
print((pizzas=='slice' or pizzas=='Pepperoni'))
#•	 Test whether an item is in a list
drinks=['water','soda','cola']
if drinks in pizzas:
  print('awesome')
elif drinks not in pizzas:
  print("healthy")





#Numerical tests involving equality and inequality, greater than and
#less than, greater than or equal to, and less than or equal to
#print(2>9)
#print(2+4 ==6)
#print(7/3 != 7)
#print(9>8.9)
#print(2*4 >=8)
#print(3-4 <= 1)



