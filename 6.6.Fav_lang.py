favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print(favorite_languages)
people=['saif','ali','mark','edward','phil']
for member in people:
  if member in favorite_languages.keys():
    print('Thankyou for responding.')
  else:
    print('you are invited to take this poll.')
