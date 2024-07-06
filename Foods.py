my_foods=['pizza','falafel','carrot_cake']
friends_food=my_foods[:]
my_foods.append("cannoli")
print(f"My favourite foods are:")
print(my_foods)
print(f"\nMy friend's favourite foods are:")
print(friends_food)
for food in my_foods:
  print(food)
for food in friends_food:
  print(food)  