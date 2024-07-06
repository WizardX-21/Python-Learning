def show_magicians(magicians_names):
  for magicians in magicians_names:
   print(magicians)
def make_great(magicians):
  great_magicians = []
  for magician in magicians:
      great_magicians.append(magician + " the Great")
  return great_magicians    
  
 
magicians = ['joe','mark','hypno']
great_magicians = make_great(magicians[:])

print("Original magicians:")
show_magicians(magicians)

print("\nGreat magicians:")
show_magicians(great_magicians)