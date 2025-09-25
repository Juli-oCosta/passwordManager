import json

data = {}

def save_data(site, email, password):
  data[site] = {
      'email': email,
      'password': password
  }
  print(f"\n--- Password for {site} saved succesfuly! ---\n")

def search_password():
    site_input = input("Which site do you want to search?: ").lower()
    if site_input in data:
        info = data[site_input]
        print("\n--- Information found ---")
        print(f"Site: {site_input}")
        print(f"Email/User: {info['email']}")
        print(f"Password: {info['password']}") # No Colab inicialmente vamos exibir a senha, será melhorado quando eu utilizar outra IDE
        print("---------------------------\n")
    else:
        print(f"\n--- No information found for '{site_input}'. ---\n")


while True:
  user_choice = input("What do you want to do?\n1. Save a new password.\n2. Search an existing password.\n3. Leave\nChoose an option: ")

  if user_choice == '1':
    site_input = input("Type in the site: ").lower()
    email_input = input("Type in your E-mail: ")
    password_input = input("Type in your password: ")

    save_data(site = site_input, email = email_input, password = password_input)
  elif user_choice == '2':
      search_password()
  elif user_choice == '3':
    print("Goodbye!!")
    break
  else:
    print("\n--- Invalid option. Please, choose 1, 2 ou 3. ---\n")
