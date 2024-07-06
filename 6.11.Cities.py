cities = {
  'Seoul':{
    'country':'South Korea',
    'population':790221129,
    'fact':'Culture Known',
  },
  
  'Toronto':{
    'country':'Canada',
    'population':7568392021,
    'fact':'Developed',
  },
  
  'Pokhara':{
    'country':'Nepal',
    'population':98496281,
    'fact':'Tourist favourite'
  },
}
for city,info in cities.items():
  print(f'{city} : {info}')