requested_toppings=['mushroom','green peppers','extra cheese']
for requested_topping in requested_toppings:
 if requested_topping=='green peppers':
  print(f"Sorry,we are out of green peppers right now.")
 else: 
  print(f"Adding {requested_topping}.")
print("\nFinished making your pizza.")


#checking that the list is not empty.
requested_toppings=[]
if requested_toppings:
 for requested_topping in requested_toppings:
  print(f"Adding {requested_topping}.")
 print("\nFinished making your pizza.")
else:
 print("Are you sure you want a plain pizza?")