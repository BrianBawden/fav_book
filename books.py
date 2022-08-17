
# from os.path import exists as file_exists
import os
import csv
import tkinter as tk

file_exists = os.path.exists

def main():
    books = True

    while books == True:
        user_input = input("Run Menu? (y/n): ")
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
    print("5. Edit book")
    print("6. Total pages read")
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
    elif selection == "5":
        edit_book(book_list)
    elif selection == "6":
        pages_read(book_list)
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

    delete_list, search_by, user_search = search_book(file)

    with open(file, "r") as inp, open("temp_file.csv", "w+") as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[search_by] != user_search:
                writer.writerow(row)

        if file_exists(file):
            os.remove(file)
            os.rename("temp_file.csv", file)

def p_books(file):

    # Create and set the GUI for the book_list_window view.
    book_list_window = tk.Tk()
    book_list_window.resizable(width=False, height=False)
    book_list_window.title("Book List")

    col_names = ("Title","Author","Genre","Pages","Notes")
    for i, col_name in enumerate(col_names, start=0):
        tk.Label(book_list_window, text=col_name).grid(row=3, column=i, padx=40)

    with open(file, "r", newline="") as passfile:
        reader = csv.reader(passfile)
        next(reader)
        data = list(reader)

    entrieslist = []
    for i, row in enumerate(data, start=4):
        entrieslist.append(row[0])
        for col in range(0, 5):
            tk.Label(book_list_window, text=row[col]).grid(row=i, column=col)

    # The close_button will stop the window and the program continues, but the window doesn't close itself.


    # close_button = tk.Button(book_list_window, text="Close", command=book_list_window.destroy).grid(column=0, row=6, sticky=tk.W, pady=10)

    book_list_window.mainloop()
            
def edit_book(file):
    
    print("What book do you want to edit: ")
    delete_book(file)
    add_book(file)

def pages_read(file):

    read_pages = 0
    with open(file, "r") as books:
        view_books = csv.reader(books)
        next(view_books)
        for row in view_books:
            read_pages += int(row[3])
        print(f"Pages read: {read_pages}")
    
main()
# add_book("book_list.csv")
# print(search_book("book_list.csv"))
# delete_book("book_list.csv")
# p_books("book_list.csv")
# edit_book("book_list.csv")
# pages_read("book_list.csv")
