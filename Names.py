#3.1 Names: Store the names of a few of your friends in a list called names. Print
#     each person’s name by accessing each element in the list, one at a time.
Friends=['Sujal','Roshan','Saurav','Naran','Anupam']
print(Friends[0].title())
print(Friends[1].title())
print(Friends[2].title())
print(Friends[-2].title())
print(Friends[-1].title())
print(Friends)

#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
#      printing each person’s name, print a message to them. The text of each message     #      should be the same, but each message should be personalized with the
#      person’s name.

print("hey "+Friends[0]+","+"how are you doing? ")
print("hey "+Friends[1]+","+"how are you doing? ")
print("hey "+Friends[2]+","+"how are you doing? ")
print("hey "+Friends[-2]+","+"how are you doing? ")
print("hey "+Friends[-1]+","+"how are you doing? ")

#3-3. Your Own List: Think of your favorite mode of transportation, such as a
#      motorcycle or a car, and make a list that stores several examples. Use your list
#      to print a series of statements about these items, such as “I would like to own a
#      Honda motorcycle.”
my_fav=['Red-Car','Dirt-Bike','Helicopter','Private-Plane']
print(f'I would love to go on a long drive in my own {my_fav[0]}.')
print(f'I would like to do a front flip from a hill with a {my_fav[1]}.')
print(f'I want to visit and watch different places of Nepal from {my_fav[2]}.')
print(f'I have {my_fav[-1]} to go anywhere in the world without any restrictions.')


