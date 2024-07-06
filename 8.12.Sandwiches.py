def sandwich_info(*sandwiches):
  print(f'The sandwich is : ')
  for sandwich in sandwiches: 
    print(f'- {sandwich}')
  
sandwich_info('psaizza','premium','veg','over500') 
sandwich_info('south-indian')
sandwich_info('western-style','light-meal')