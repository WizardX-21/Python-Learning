users=['john','kevin','mark','ben','omni','admin']
if users:#checking if the list is not empty.
 for user in users:
  if user=='admin':
    print(f"Hello admin,would you like to see a status report?")
  else:
    print(f"hello {user},thank you for logging in again.")
else:
  print("we need to fine dome users.")

users=[] #removing users from list.
if not users:#rechecking whether list is empty or not.
  print('We need to find some users!')     