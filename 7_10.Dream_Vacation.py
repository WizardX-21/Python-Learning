Poll = {}
polling_active = True
while polling_active:
  name = input('\nWhat is your name? ')
  dream_vacation = input('If you could visit one place in the world,\nwhere would you go? ')

  Poll[name] = dream_vacation

  repeat = input("Would you like to let another person take the poll? (yes/ no) ")
  if repeat == 'no':
    polling_active = False

print(f'---Poll results---')
for name,dream_vacation in Poll.items():
  print(f'{name.title()} would like to go to {dream_vacation.title()}.')
  

