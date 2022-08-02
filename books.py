
# from os.path import exists as file_exists
import os
import csv

file_exists = os.path.exists

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
    print("4. Print books")
    print("0. exit menu")

    selection = input()

    if selection == "1":
        add_book(book_list)
    elif selection == "2":
        search_book(book_list)
    elif selection == "3":
        delete_book(book_list)
    elif selection == "4":
        p_books(book_list)
    elif selection == "0":
        return None
    else:
        print("Invalid selection")
        menu()

def add_book(file):

    new_title = input("Enter the title: ")
    new_author = input("Enter the author: ")
    new_genre = input("Enter the genre: ")
    new_page = input("Enter the number of page: ")
    new_notes = input("Enter the notes: ")

    fields = ["Title", "Author", "Genre", "Pages", "Notes"]
    fields_dict = {"Title": new_title, "Author": new_author, "Genre": new_genre, "Pages": new_page, "Notes": new_notes}

    if file_exists(file):
        with open(file, "a") as csv_file:
            dict_object = csv.DictWriter(csv_file, fieldnames=fields)

            dict_object.writerow(fields_dict)


def search_book(file):
    print("0. Title")
    print("1. Author")
    print("2. Genres")
    search_by = int(input("Please enter selection: "))
    user_search = input("Enter your search: ")

    search_list = []
    if file_exists(file):
        with open(file, "r") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            for item in reader:
                if item[search_by] == user_search:
                    search_list.append(item)
                    print(item)
            return search_list, search_by, user_search

def delete_book(file):

    print("Enter book information to be deleted:")
    delete_list, search_by, user_search = search_book(file)

    with open(file, "r") as inp, open("temp_file.csv", "w+") as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[search_by] != user_search:
                writer.writerow(row)

        if file_exists(file):
            os.remove(file)
            os.rename("temp_file.csv", file)
            print("deleted")

def p_books(file):
    count = 1
    with open(file, "r") as books:
        view_books = csv.reader(books)
        next(view_books)
        for row in view_books:
            print(f"{count}. {row[0]} by {row[1]}")
            count += 1
            
    
main()
# add_book("book_list.csv")
# print(search_book("book_list.csv"))
# delete_book("book_list.csv")
# p_books("book_list.csv")