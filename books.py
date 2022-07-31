
from os.path import exists as file_exists
import csv



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

    book_list = "book_list.csv"

    print("1. Add book")
    print("2. Search books")
    print("3. Delete book")
    print("0. exit menu")

    selection = input()

    if selection == "1":
        add_book()
    elif selection == "2":
        search_book(book_list)
    elif selection == "3":
        delete_book()
    elif selection == "0":
        return None
    else:
        print("Invalid selection")
        menu()

def add_book():
    print("add")

    # "I decided to get the program to read the file first."
    # book_list = "book_list.csv"
    # if file_exists(book_list):
    #     with open(book_list, "a") as csv_file:
    #         csv_
    # print("add done")


def search_book(file):
    print("search")
    if file_exists(file):
        print("Found file")
    print("search done")

def delete_book():
    print("delete")


main()