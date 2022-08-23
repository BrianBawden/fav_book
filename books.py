
# from os.path import exists as file_exists
import os
import csv
from re import S
import tkinter as tk

file_exists = os.path.exists


def add_book(file):


    # add book function
    def add_book_function():
        # csv file to add to list
        csv_book = "/Users/brian/projects/fav_book/book_list.csv"


        try:

            fields = ["Title", "Author", "Genre", "Pages", "Notes"]
            fields_dict = {"Title": new_title.get(), "Author": new_author.get(), "Genre": new_genre.get(), "Pages": new_pages.get(), "Notes": new_notes.get()}

            with open(csv_book, "a") as csv_file:
                dict_object = csv.DictWriter(csv_file, fieldnames=fields)

                dict_object.writerow(fields_dict)

            clear()

        except ValueError:
            pass

    def clear():
        [widget.delete(0, tk.END) for widget in add_book_window.winfo_children() if isinstance(widget, tk.Entry)]


    # create add_book_window
    add_book_window = tk.Toplevel(menu_window)
    add_book_window.geometry("600x350")
    # add_book_window.eval('tk::PlaceWindow . center')
    add_book_window.title("Add Book")

    # make labels from add_labels visible in add_book_window with a for loop and enumerate
    add_labels = ("Title: ", "Author: ", "Genre", "Pages: ", "Notes: ")
    for i, add_label in enumerate(add_labels, start=0):
        tk.Label(add_book_window, text=add_label).grid(row=i, column=0, padx=15, pady=10)


    # set up entry boxes for the new book
    new_title = tk.StringVar()
    title_entry = tk.Entry(add_book_window, textvariable=new_title, font= "ariel 20")
    title_entry.grid(column=1, row=0, sticky=tk.W, padx=15, pady=10)

    new_author = tk.StringVar()
    author_entry = tk.Entry(add_book_window, textvariable=new_author, font= "ariel 20")
    author_entry.grid(column=1, row=1, sticky=tk.W, padx=15, pady=10)

    new_genre = tk.StringVar()
    genre_entry = tk.Entry(add_book_window, textvariable=new_genre, font= "ariel 20")
    genre_entry.grid(column=1, row=2, sticky=tk.W, padx=15, pady=10)

    new_pages = tk.StringVar()
    pages_entry = tk.Entry(add_book_window, textvariable=new_pages, font= "ariel 20")
    pages_entry.grid(column=1, row=3, sticky=tk.W, padx=15, pady=10)

    new_notes = tk.StringVar()
    notes_entry = tk.Entry(add_book_window, textvariable=new_notes, font= "ariel 20")
    notes_entry.grid(column=1, row=4, sticky=tk.W, padx=15, pady=10)


    # Add and cancel buttons
    add_button = tk.Button(add_book_window, text="Add Book", command=add_book_function).grid(column=0, row=5, padx=15, pady=10)

    cancel_button = tk.Button(add_book_window, text="Cancel", command=lambda: [add_book_window.destroy()]).grid(column=1, row=5, sticky=tk.W, pady=10)

   

    # End of add_book_window
    add_book_window.mainloop()



def search_book(file):

    def search(search_in, search_for):

        search_by = search_in
        user_search = search_for

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

    search_book_window = tk.Toplevel(menu_window)
    search_book_window.resizable(width=False, height=False)
    search_book_window.geometry("350x350")
    search_book_window.title("Search Books")

    r = tk.IntVar()

    tk.Radiobutton(search_book_window, text="Title", variable=r, value=0).pack()
    tk.Radiobutton(search_book_window, text="Author", variable=r, value=1).pack()
    tk.Radiobutton(search_book_window, text="Genres", variable=r, value=2).pack()

    user_search = tk.StringVar()
    searching = tk.Entry(search_book_window, textvariable=user_search).pack()

    tk.Button(search_book_window, text="Search", command=lambda: search(r.get(), searching)).pack()

    search_book_window.mainloop()


    # search_by = r.get()
    # user_search = input("Enter your search: ")

    # search_list = []
    # if file_exists(file):
    #     with open(file, "r") as csv_file:
    #         reader = csv.reader(csv_file)
    #         next(reader)

    #         for item in reader:
    #             if item[search_by] == user_search:
    #                 search_list.append(item)
    #                 print(item)
    #         return search_list, search_by, user_search

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

def view_books(file):

    # Create and set the GUI for the book_list_window view.
    book_list_window = tk.Toplevel(menu_window)
    book_list_window.resizable(width=False, height=False)
    # book_list_window.eval('tk::PlaceWindow . center')
    book_list_window.title("Book List")

    col_names = ("Title","Author","Genre","Pages","Notes")
    for i, col_name in enumerate(col_names, start=0):
        tk.Label(book_list_window, text=col_name, padx=10, pady=10).grid(row=3, column=i, padx=40)

    with open(file, "r", newline="") as passfile:
        reader = csv.reader(passfile)
        next(reader)
        data = list(reader)

    entrieslist = []
    for i, row in enumerate(data, start=4):
        entrieslist.append(row[0])
        for col in range(0, 5):
            tk.Label(book_list_window, text=row[col], padx=10, pady=10).grid(row=i, column=col)

    # The close_button will stop the window and the program continues, but the window doesn't close itself.


    # close_button = tk.Button(book_list_window, text="Close", command=book_list_window.destroy).grid(column=0, row=6, sticky=tk.W, pady=10)

    book_list_window.mainloop()

    
            
def edit_book(file):
    
    print("What book do you want to edit: ")
    delete_book(file)
    add_book(file)

def pages_read(file):

    read_window = tk.Tk()
    read_window.resizable(width=False, height=False)
    read_window.eval('tk::PlaceWindow . center')
    read_window.title("Total Pages Read")

    read_pages = 0
    with open(file, "r") as books:
        view_books = csv.reader(books)
        next(view_books)
        for row in view_books:
            read_pages += int(row[3])
        # print(f"Pages read: {read_pages}")
    
    you_read = "You have read: " + str(read_pages)

    tk.Label(read_window, text=you_read, padx=50, pady=20, font="ariel 20").pack()


    read_window.mainloop()




book_list = "book_list.csv"

# Create Zoe's book list window
menu_window = tk.Tk()
menu_window.geometry("350x350")
# menu_window.eval("tk::PlaceWindow . center")
menu_window.title("Zoe's Books")


zoes_label = tk.Label(menu_window, text="Zoe's Books App", font="bold 20").grid(column=0, row=0, columnspan=3, padx=20, pady=20)


a_book = tk.Button(menu_window, text="Add Book", command=lambda: add_book(book_list)).grid(column=0, row=1, padx=20, pady=20)
v_book = tk.Button(menu_window, text="View Books", command=lambda: view_books(book_list)).grid(column=0, row=2, padx=20, pady=20)
v_pages = tk.Button(menu_window, text="Total Pages", command=lambda: pages_read(book_list)).grid(column=0, row=3, padx=20, pady=20)
s_book = tk.Button(menu_window, text="Search Books", command=lambda: search_book(book_list)).grid(column=1, row=1, padx=20, pady=20)


menu_window.mainloop()


# print("1. Add book")
# print("2. Search books")
# print("3. Delete book")
# print("4. Print books")
# print("5. Edit book")
# print("6. Total pages read")
# print("0. exit menu")

# selection = input()

# if selection == "1":
#     add_book(book_list)
# elif selection == "2":
#     search_book(book_list)
# elif selection == "3":
#     delete_book(book_list)
# elif selection == "4":
#     p_books(book_list)
# elif selection == "5":
#     edit_book(book_list)
# elif selection == "6":
#     pages_read(book_list)
# elif selection == "0":
#     return None
# else:
#     print("Invalid selection")
#     menu()
