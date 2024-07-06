sandwich_orders = ['Pastrami','Club sandwich','Pastrami', 'BLT sandwich','Reuben sandwich','Pastrami','Italian Sub']
finished_orders = []
print(f'\nThe deli has run out of Pastrami.')
while 'Pastrami' in sandwich_orders:
  sandwich_orders.remove('Pastrami')
finished_orders.append(sandwich_orders)
print(finished_orders)  