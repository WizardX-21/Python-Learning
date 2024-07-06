#checking that the list is not empty.
requested_toppings=[]
if requested_toppings:
 for requested_topping in requested_toppings:
  print(f"Adding {requested_topping}.")
 print("\nFinished making your pizza.")
else:
 print("Are you sure you want aa plain pizza?")