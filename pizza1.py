def make_pizza(size, *toppings):
  print(f'\nMaking a {str(size)}-inch pizza with the following toppings:')
  for topping in toppings:
    print(f'- {topping}')

make_pizza(14,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese') 
