def formatted_name(first_name,last_name):
  full_name = first_name + ' ' + last_name
  return full_name.title()

formatted_name('linux','parrot')
musician = formatted_name('jimi','hendrix')
print(musician)
singer = formatted_name('kali','linux')
print(singer)