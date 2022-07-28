

def get_user():
    user_name = input("Enter Your user name: ")
    print(f"Welcome {user_name}." )

def menu():
    print("1. Add book")
    print("1. Search books")
    print("3. Delete  book")

    selection = input()

    if selection == 1:
        add_book()
    elif selection == 2:
        search_book()
    elif selection == 3:
        return None
    else:
        print("Invalid selection")
        menu()
