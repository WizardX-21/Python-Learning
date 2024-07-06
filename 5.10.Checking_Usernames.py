#•	 Make a list of five or more usernames called current_users.
current_users=['mark','ben','kevin','john','elon']
new_users=['simon','ryan','chris','Ben','purav','John']
current_users_lower=[users.lower() for users in current_users]

for new_user in new_users:
  if new_user.lower() in current_users_lower:
    print(f"you will need to enter a new username.")
  else:
    print("the username is available.")  