def formatted_name(first_name, last_name):
  full_name = first_name + ' ' + last_name
  return full_name.title()
while True:
  print('\nPlease tell me your name:')
  print(f'Enter q to quit at anytime.')
  f_name = input('First name: ')
  if f_name == 'q':
    break
  l_name = input('Last name: ')
  if l_name == 'q':
    break
  format_name = formatted_name(f_name,l_name)
  print(f'\nHello, {format_name}!')