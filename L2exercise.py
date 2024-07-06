#verb = input ("Enter a verb: ")
#print("I can",verb,"better than you!")
#print((verb+" " )* 5)

# Ask the user for a verb
verb = input("Please enter a verb: ")

# Print the customized sentence
print(f"I can {verb} better than you!")

# Print the verb 5 times in a row separated by spaces without a space at the end
print(" ".join([verb] * 5))
