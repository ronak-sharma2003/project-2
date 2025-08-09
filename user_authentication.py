predefined_username = 'ronak.08'
predefined_password = 'Ronak@123'


#prompts the user to enter a username and password

username = input("Enter your username: ")
password = input("Enter your password: ")



#username and password match

if username == predefined_username:
    if password == predefined_password:
        print("Welcome! Login was successful")
    else:
        print("incorrect password!")

else: 
    print("Invalid username")   