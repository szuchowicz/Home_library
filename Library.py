from tkinter import *
from tkinter.messagebox import *
import backend


def view_function():
    output_text.delete(0, END)
    for books in backend.view():
        output_text.insert(END, books)


def search_function():
    search_for_author = book_author.get()
    search_for_title = book_title.get()
    search_for_year = book_year.get()
    search_for_isbn = book_ISBN.get()

    output_text.delete(0, END)
    for books in backend.search(search_for_author, search_for_title, search_for_year, search_for_isbn):
        output_text.insert(END, books)


def add_function():
    add_author = book_author.get()
    add_title = book_title.get()
    add_year = book_year.get()
    add_isbn = book_ISBN.get()

    backend.add_book(add_author, add_title, add_year, add_isbn)

    output_text.delete(0, END)
    output_text.insert(END, (add_author, add_title, add_year, add_isbn))


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
        showerror("No book selected", "No book to select")


def delete_book():
    backend.delete_book(selected_book[0])

    # Refresh output listbox
    view_function()


def update_book():
    # get new details from entries
    new_author = book_author.get()
    new_title = book_title.get()
    new_year = book_year.get()
    new_isbn = book_ISBN.get()
    backend.update_book(new_author, new_title, new_year, new_isbn, selected_book[0])

    # Refresh output listbox
    view_function()


main_window = Tk()
main_window.title("My Library")

"""
Visual elements definition below
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

view_all_button = Button(main_window, text="View all", width=10, command=view_function)
view_all_button.grid(row=2, column=3)

search_button = Button(main_window, text="Search entry", width=10, command=search_function)
search_button.grid(row=3, column=3)

add_button = Button(main_window, text="Add entry", width=10, command=add_function)
add_button.grid(row=4, column=3)

update_button = Button(main_window, text="Update", width=10, command=update_book)
update_button.grid(row=5, column=3)

delete_button = Button(main_window, text="Delete", width=10, command=delete_book)
delete_button.grid(row=6, column=3)

exit_button = Button(main_window, text="Exit", width=10, command=close_app)
exit_button.grid(row=7, column=3)

clean_button = Button(main_window, text="Clean entries", width=10, command=clean_entries)
clean_button.grid(row=8, column=3)

# scrollbar

scrollbar = Scrollbar(main_window)
scrollbar.grid(row=2, column=2, rowspan=6)

# output listbox

output_text = Listbox(main_window, width=30, height=10, yscrollcommand=scrollbar.set)
output_text.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar.config(command=output_text.yview())

output_text.bind('<<ListboxSelect>>', show_selected_details)

main_window.mainloop()

# TODO add multiple databases possibility
# TODO add login window
