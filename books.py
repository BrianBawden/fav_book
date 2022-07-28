def main():
    books = True

    while books == True:
        user_input = input("Do you want run books? (y/n): ")
        if user_input.strip().lower()[0] == "y":
            menu()
        elif user_input.strip().lower()[0] == "n":
            books = False
        else:
            print("invalid entry try again")
            main()

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
        delete_book()
    else:
        print("Invalid selection")
        menu()

def add_book():
    print("add")

def search_book():
    print("search")

def delete_book():
    print("delete")


main()