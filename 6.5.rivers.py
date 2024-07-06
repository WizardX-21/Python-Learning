rivers={'nile':'egypt','gandaki':'Nepal','ganga':'india'}
for key,value in rivers.items():
  print(f'The {key.title()} runs through the {value.title()}.')
print(f'The list of rivers are:')  
for river in rivers.keys():
  print(river.title())

print(f'The list of countries are:')
for country in rivers.values():
  print(country.title())