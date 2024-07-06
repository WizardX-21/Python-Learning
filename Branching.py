x=42
y=int(input("enter a guess for y : "))
if y < x:
  print("guess is too low")
elif x<y:
  print("guess is too high")
else:
  print("guess is same.")   