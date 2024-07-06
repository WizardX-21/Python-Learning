#Make an empty list for storing aliens.
aliens=[]
#make 30 green aliens.
for alien_number in range(30):
  new_alien = {'color':'green','points':'5','speed':'slow'}
  aliens.append(new_alien)

for alien in aliens[0:3]:
  if alien['color'] == 'green':
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['points'] = 10
  elif alien['color'] == 'yellow':
    alien['color'] = 'red'
    alien['speed'] = 'fast'
    alien['points'] = 15


#show the first five aliens.
for alien in aliens[:5]:
  print(alien)
#Show how many aliens have been created.
print('Total numbers of aliens:'+ str(len(aliens)))    

