#  3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
#   would you invite? Make a list that includes at least three people you’d like to
#   invite to dinner. Then use your list to print a message to each person, inviting
#   them to dinner.
Guests=['Richard','Ashok','Maruti']
print(f'{Guests[0]},you are invited to dinner.')
print(f'{Guests[1]},you are invited to dinner.')
print(f'{Guests[-1]},you are invited to dinner.')

#3-5. Changing Guest List: You just heard that one of your guests can’t make the
#    dinner, so you need to send out a new set of invitations. You’ll have to think of
#    someone else to invite.

#Start with your program from Exercise 3-4. Add a print statement at the
#end of your program stating the name of the guest who can’t make it.
print(Guests[0].title())
# Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
Guests[0]='Browney'
# Print a second set of invitation messages, one for each person who is still
# in your list.
print(f'{Guests[0]},heartily welcome to dinner.')
print(f'{Guests[1]},heartily welcome to dinner.')
print(f'{Guests[-1]},heartily welcome to dinner.')

#3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.

#  •	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
#bigger dinner table.
#•	 Use insert() to add one new guest to the beginning of your list.
#•	 Use insert() to add one new guest to the middle of your list.
#•	 Use append() to add one new guest to the end of your list.
#•	 Print a new set of invitation messages, one for each person in your list
print(f'hey everyone,I found a bigger dinner table.')
Guests.insert(0,'Ram')
Guests.insert(1,'Sita')
Guests.append('Laxman')

print(Guests)
print(f' {Guests[0]}, heartily welcome to dinner.')
print(f' {Guests[1]}, heartily welcome to dinner.')
print(f' {Guests[-1]}, heartily welcome to dinner.')
#3-7. Shrinking Guest List:
# Start with your program from Exercise 3-6. Add # a new line that prints a
# message saying that you can invite only two people for dinner
print(f'I am extremely sorry to put everyone through this but i can only invite only two people for dinner.')

#Use pop() to remove guests from your list one at a time until only two
#names remain in your list. Each time you pop a name from your list, print
#a message to that person letting them know you’re sorry you can’t invite
#them to dinner.
print(Guests)
print(f'{Guests[2]},I am sorry I cannot invite you to dinner.')
Guests.pop(2)

print(f'{Guests[2]},I am sorry I cannot invite you to dinner.')
Guests.pop(2)

print(Guests)
print(f'{Guests[0]},youre welcome to dinner.')
print(f'{Guests[1]},youre welcome to dinner.')
print(f'{Guests[2]},youre welcome to dinner.')
print(f'{Guests[-1]},youre welcome to dinner.')

#3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
#through 3-7 (page 46), use len() to print a message indicating the number
#of people you are inviting to dinner.
print(len(Guests))
print(f"I am inviting {len(Guests)} guests in todays dinner.")

# Use del to remove the last two names from   your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

del Guests[3]
del Guests[2]
del Guests[1]
del Guests[0]
print(Guests)


