alien1={'X_position':0,'y_position':25, 'speed':'medium'}
print(f'Original X_Position: {alien1['X_position']}')
# Move the alien to the right.
#Determine how far to move the alien based on its current speed.
if alien1['speed'] == 'slow':
  X_increment = 1
elif alien1['speed'] == 'medium':
  X_increment = 2
else:
  #this must be a fast alien.
  X_increment = 3
#The new position is the old position plus the increment.
alien1['X_position']=alien1['X_position'] + X_increment
print(f'New X-position: {alien1["X_position"]}')       
#Removing key-value pairs:
print(alien1)
del alien1['speed']
print(alien1)

#Dictionary of similar objects
favourite_languages={
  'jen':'python',
  'sarah':'C',
  'edward':'ruby',
  'phil':'python',

}
print(f'Sarahs favourite language is:{favourite_languages['sarah']}')