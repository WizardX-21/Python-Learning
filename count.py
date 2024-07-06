#WAP to count the number of unique letters there are in string.
s=input("Enter your word to count unique letters: ").lower()
seen=''
for char in s:
  if char not in seen:
    seen += char
  else:#pass is used in py to do nothing.
    pass
print(len(seen))    
