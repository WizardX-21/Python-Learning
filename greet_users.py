def greet_users(names):
  for name in names:
    msg = "Hello," + name.title() + "!"
    print(msg)
usernames = ['ben','elon','mark','bill']
greet_users(usernames)    