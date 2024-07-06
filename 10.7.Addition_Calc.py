from pathlib import Path

path = Path('Guest_book.txt')
name_list = []
while True:
  name = input("Enter your full  name(or q to quit) : ")
  if name == 'q':
    break
  else:
   
   name_list.append(name.title())
#Convert the list of names to a single string with each name on a new line   
contents = '\n'.join(name_list)
path.write_text(contents)
print('The names have been written.')   