#step:1 Define the show_magicians function
def show_magicians(magicians):
 """Print the name of each magician in the list."""
 for magician in magicians:
  print(magician)


  #Step:2 Define the make_great function
def make_great(magicians):
   """Add 'the great' to each magician's name and return a new list."""
   great_magicians = []
   for magician in magicians:
    great_magicians.append(magician + " the Great")
   return great_magicians


    #step:3 Create the original list of magicians

magicians = ['Harry Houdini','David Copperfield','Penn Jillete','Teller','Dynamo']

    #step:4 Call make_great with a copy of original list and store the result in anew variable
    
great_magicians = make_great(magicians[:])

    #step:5 Print the original and modified lists
print("original magicians:")
show_magicians(magicians)

print("\nGreat magicians:")
show_magicians(great_magicians)