#3-8. Seeing the World: Think of at least five places in the world you’d like to
#visit.
#Store the locations in a list. Make sure the list is not in alphabetical order
places=['niagra','pokhara','newzealand','norway','switzerland']
print(places)
#Use sorted() to print your list in alphabetical order without modifying the
#actual list.
print(sorted(places))
print(places)

#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print(sorted(places,reverse=True))
print(places)
#Use reverse() to change the order of your list. Print the list to show that its
#order has changed.
places.reverse()
print(places)

#Use reverse() to change the order of your list again. Print the list to show
#it’s back to its original order.
places.reverse()
print(places)
#	 Use sort() to change your list so it’s stored in alphabetical order. Print the
#list to show that its order has been changed.
places.sort()
print(places)
#Use sort() to change your list so it’s stored in reverse alphabetical order.
#Print the list to show that its order has #changed.
places.sort(reverse=True)
print(places)
