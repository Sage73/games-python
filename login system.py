email = ""
password = ""


def account():
    print("starting program...")

    def create_account():
        global email
        global password
        print("- create an account")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        with open('mega_poor_database.txt', 'r') as shish:
            data = shish.readlines()
        data[1] = f'{email}\n'
        data[3] = f'{password}\n'
        shish.close()
        with open('mega_poor_database.txt', 'w') as megashish:
            megashish.writelines(data)
        megashish.close()

    def login():
        global email
        global password
        database = open('mega_poor_database.txt')
        lines = database.read().split()
        correct_email = lines[1]
        correct_password = lines[3]
        database.close()
        print("- Login")
        access_email = input("Enter your email: ")
        if access_email == correct_email:
            access_password = input("Enter your password: ")
            if access_password == correct_password:
                print("you are logged in")
            else:
                print("wrong password")
        else:
            print("invalid email, check if it is correct")

    account = input("do you have an account? y/n: ")
    if account.lower() == "no" or account.lower() == "n":
        create_account()
        ask_login = input("account created... do you want to log in? y/n: ")
        if ask_login.lower() == "yes" or ask_login.lower() == "y":
            login()
        else:
            print("closing program...")
    elif account.lower() == "yes" or account.lower() == "y":
        login()


account()
