alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
#accessing values in dictionaries.
new_points = alien_0['points']
print(f"You just earned {new_points} points!.")
#Adding new key-value pairs
alien_0['x_position']=0
alien_0['Y_position']=25
print(alien_0)
#Modifying value
alien_0['color']='yellow'
print(f'The alien is now {alien_0["color"]}.')
