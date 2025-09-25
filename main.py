import json

data = {}

def save_data(site, email, password):
  data[site] = {
      'email': email,
      'senha': password
  }


over = False
while not over:
  while True:
    print("What do you want to do?")
    user_choice = int(input("1. Save a new password.\n2. Search an existing password.\n3. Leave\n"))
    if user_choice == 1:
      site_input = input("Type in the site: ")
      email_input = input("Type in your E-mail: ")
      password_input = input("Type in your password: ")

      save_data(site = site_input, email = email_input, password = password_input)
      break
    elif user_choice == 2:
      site_input = input("Type in the site: ")
      if site_input in data:
        print(data[site_input])
        break
      else:
        print("No information for this site.")
      break
    elif user_choice == 3:
      print("Goodbye!!")
      over = True
    else:
      print("Oops, that's an invalid option, choose only between options 1, 2 or 3")
