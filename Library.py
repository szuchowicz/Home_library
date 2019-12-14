from tkinter import *
from tkinter.messagebox import *
import backend
import os

'''
Main window function definition
'''


def verify_data_values(data_values):
    # check if user insert values to all field
    if "" in data_values:
        showerror("Incorrect value", "Please fill all places")
    else:
        # check if year and ISBN are integer values
        try:
            int(data_values[2])
            int(data_values[3])
            return True
        except ValueError:
            showerror("Incorrect value", "Year and ISBN should be integer values")


def view_function():
    # Print all records in current database into output window
    output_text.delete(0, END)
    for books in backend.view(db_name):
        output_text.insert(END, books)


def search_function():
    # search for record in db
    search_for_author = book_author.get()
    search_for_title = book_title.get()
    search_for_year = book_year.get()
    search_for_isbn = book_ISBN.get()

    output_text.delete(0, END)
    for books in backend.search(db_name, search_for_author, search_for_title, search_for_year, search_for_isbn):
        output_text.insert(END, books)


def add_function():
    # add new book
    add_author = book_author.get()
    add_title = book_title.get()
    add_year = book_year.get()
    add_isbn = book_ISBN.get()
    add_values = (add_author, add_title, add_year, add_isbn)

    # verification user input
    if verify_data_values(add_values) is True:
        backend.add_book(db_name, add_values[0], add_values[1], add_values[2], add_values[3])
        output_text.delete(0, END)
        output_text.insert(END, add_values)


def clean_entries():
    title_entry.delete(0, END)
    author_entry.delete(0, END)
    year_entry.delete(0, END)
    ISBN_entry.delete(0, END)


def close_app():
    main_window.destroy()


def show_selected_details(event):
    try:
        global selected_book
        # get the current book details into tuple
        index = output_text.curselection()[0]
        selected_book = output_text.get(index)

        # clean entries
        title_entry.delete(0, END)
        author_entry.delete(0, END)
        year_entry.delete(0, END)
        ISBN_entry.delete(0, END)

        # Push proper details into entries
        author_entry.insert(END, selected_book[1])
        title_entry.insert(END, selected_book[2])
        year_entry.insert(END, selected_book[3])
        ISBN_entry.insert(END, selected_book[4])

    except IndexError:
        pass


def delete_book():
    backend.delete_book(db_name, selected_book[0])

    # Refresh output listbox and clean entries
    clean_entries()
    view_function()


def update_book():
    # get new details from entries
    new_author = book_author.get()
    new_title = book_title.get()
    new_year = book_year.get()
    new_isbn = book_ISBN.get()
    update_values = (new_author, new_title, new_year, new_isbn)

    # verification user input
    if verify_data_values(update_values) is True:
        backend.update_book(db_name, update_values[0], update_values[1], update_values[2], update_values[3],
                            selected_book[0])

    # Refresh output listbox
    view_function()


'''
Select db functions definition
'''


def show_existing_db():
    # check for all db's in app folder to put it into select_db_window
    for root, dirs, files in os.walk(os.curdir, topdown=True):
        for file in files:
            if file.endswith(".db"):
                select_db_window.insert(END, str(file))


def db_selected(event):
    global db_name
    try:
        index = select_db_window.curselection()[0]
        db_name = select_db_window.get(index)
        main_window.title(f"My library - {db_name}")
        # Clean list of books and entries
        clean_entries()
        output_text.delete(0, END)
        db_choose.withdraw()
        main_window.deiconify()
    except IndexError:
        pass


def change_db():
    db_choose.deiconify()

    # Refresh databases list
    select_db_window.delete(0, END)
    show_existing_db()


def create_db():
    create_db_window.deiconify()


'''
Create new database function
'''


def create_db_exit():
    create_db_window.destroy()
    db_choose.deiconify()


def create_new_db(event):
    global db_name
    name = new_db_entry.get()
    db_name = f"{name}.db"

    if os.path.exists(db_name):
        showerror("Incorrect db name", "This database already exists")
    else:
        backend.create_table(db_name)
        main_window.title(f"My library = {db_name}")
        create_db_window.destroy()
        db_choose.withdraw()
        main_window.deiconify()


main_window = Tk()


db_choose = Toplevel(master=main_window, width=30, height=30)
db_choose.pack_propagate(0)
db_choose.title("Select database")

# New db create window
create_db_window = Toplevel(master=db_choose, width=30, height=20)
create_db_window.title("Create new database")
create_db_window.withdraw()


"""
Visual elements of create window
"""

create_db_label = Label(create_db_window, text="Input name of new database and press enter")
create_db_label.grid(row=0, column=0)

new_db_name = StringVar()
new_db_entry = Entry(create_db_window, textvariable=new_db_name)
new_db_entry.grid(row=1, column=0)
new_db_entry.bind('<Return>', create_new_db)

create_window_exit = Button(create_db_window, text="Exit", command=create_db_exit)
create_window_exit.grid(row=2, column=0)

"""
Visual elements of select window
"""

instruction_label = Label(db_choose, text="Click on db You want to open or create new one")
instruction_label.grid(row=0, column=0)

select_db_window = Listbox(db_choose, width=40)
select_db_window.grid(row=1, column=0, rowspan=2)
select_db_window.bind('<<ListboxSelect>>', db_selected)

new_db_button = Button(db_choose, text="Create new database", width=20, command=create_db)
new_db_button.grid(row=1, column=1)

exit_all_button = Button(db_choose, text="Exit program", width=20, command=close_app)
exit_all_button.grid(row=2, column=1)


"""
Visual elements of main window definition below
"""

# Labels
title_label = Label(main_window, text="Title")
title_label.grid(row=0, column=0)

author_label = Label(main_window, text="Author")
author_label.grid(row=0, column=2)

year_label = Label(main_window, text="Year")
year_label.grid(row=1, column=0)

ISBN_label = Label(main_window, text="ISBN")
ISBN_label.grid(row=1, column=2)

# Entry fields
book_title = StringVar()
title_entry = Entry(main_window, textvariable=book_title)
title_entry.grid(row=0, column=1)

book_author = StringVar()
author_entry = Entry(main_window, textvariable=book_author)
author_entry.grid(row=0, column=3)

book_year = StringVar()
year_entry = Entry(main_window, textvariable=book_year)
year_entry.grid(row=1, column=1)

book_ISBN = StringVar()
ISBN_entry = Entry(main_window, textvariable=book_ISBN)
ISBN_entry.grid(row=1, column=3)

# Buttons

view_all_button = Button(main_window, text="View all", width=15, command=view_function)
view_all_button.grid(row=2, column=3)

search_button = Button(main_window, text="Search entry", width=15, command=search_function)
search_button.grid(row=3, column=3)

add_button = Button(main_window, text="Add entry", width=15, command=add_function)
add_button.grid(row=4, column=3)

update_button = Button(main_window, text="Update", width=15, command=update_book)
update_button.grid(row=5, column=3)

clean_button = Button(main_window, text="Clean entries", width=15, command=clean_entries)
clean_button.grid(row=6, column=3)

delete_button = Button(main_window, text="Delete", width=15, command=delete_book)
delete_button.grid(row=7, column=3)

change_db_button = Button(main_window, text="Change database", width=15, command=change_db)
change_db_button.grid(row=8, column=3)

exit_button = Button(main_window, text="Exit", width=15, command=close_app)
exit_button.grid(row=9, column=3)

# scrollbar

scrollbar = Scrollbar(main_window)
scrollbar.grid(row=2, column=2, rowspan=6)

# output listbox

output_text = Listbox(main_window, width=30, height=10, yscrollcommand=scrollbar.set)
output_text.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar.config(command=output_text.yview())

output_text.bind('<<ListboxSelect>>', show_selected_details)

show_existing_db()
main_window.withdraw()
main_window.mainloop()


# TODO add multiple databases possibility
# TODO add login window
