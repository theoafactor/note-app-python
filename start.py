from database import db

## initialize our tables
db.createUsersTable()
db.createNotesTable()

print("""
--- Welcome to the Notes Application ---
 """)

result = db.loginUser()



if result == None:
    print("\n--------------------------------------------------")
    print("\nUser with that account does not exist. \nDo you want to register?")
    response = input("Enter 'Y' for Yes or 'N' for No: ")

    if response == "N":
        print("Goodbye!")
        exit()
    elif response == "Y":
        errors = []
        fullname = input("Enter your fullname: ").strip()
        email = input("Enter your email address: ").strip()
        gender = input("Enter 'male', 'female' or 'others': ").strip()
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        password_confirmation = input('Enter password again: ').strip()

        if len(fullname) == 0:
            errors.append("You did not enter your full name")
        if len(email) == 0:
            errors.append("You did not enter email")
        if len(gender) == 0:
            errors.append("You did not enter gender")
        if gender is not 'male' or gender is not 'female' or gender is not 'others':
            errors.append("Enter 'male', 'female' or 'others' for gender")

        if len(username) == 0:
            errors.append("You did not enter username: ")
        
        if len(password) == 0:
            errors.append("You did not enter password")
        
        if len(password_confirmation) == 0:
            errors.append("You did not enter password confirmation")
        
        if password != password_confirmation:
            errors.append("Password and Password confirmation must match!")

        if len(errors) == 0:
            # there are no errors
            db.registerUser(fullname, email, username, gender, password)
        else:
            # there are errors
            print(errors)
        



## check if the username and password exist
