import string
import random

def user_details():
   firstName = input("Enter your first name ")

   lastName = input("Enter your last name ")

   email = (input("Enter your Email "))

   details = [firstName, lastName, email]

   return details


def get_password(details):
    length = 5
    random.choice(string.ascii_lowercase)
    random_password = "".join(random.choice(string.ascii_lowercase) for i  in range(length))
    password = str(details[0][0:2] + details[1][-2:] + random_password)

    return password

container = []
status = True
while status:
    details = user_details()

    password = get_password(details)
    print("This is your password: " + str(password))
    
    accept_password = input("Is the password okay? type yes or no: ")
    passed = True
    while passed:
       if accept_password == "yes":
           details.append(password)

           container.append(details)
           passed = False
       else: 
           new_password = (input("Enter password with 7 or more characters: "))
           len_pass = True
           while len_pass:
               if len(new_password) <= 7:
                   print("Your password is less than 7 characters")
                   new_password = input("Enter Password: ")
               if len(new_password) >= 7:
                 details.append(new_password)

                 container.append(details)
                 len_pass = False
                 passed = False

    new_user = input(str("would you like to enter a new user? Yes or No: "))
    if (new_user == "no"):
       status = False
   
    for item in container:
       print(item)
    if new_user == "yes":
       status = True
   

