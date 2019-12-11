from tkinter import *

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

view_all_button = Button(main_window, text="View all", width=10)
view_all_button.grid(row=2, column=3)

search_button = Button(main_window, text="Search entry", width=10)
search_button.grid(row=3, column=3)

add_button = Button(main_window, text="Add entry", width=10)
add_button.grid(row=4, column=3)

update_button = Button(main_window, text="Update", width=10)
update_button.grid(row=5, column=3)

delete_button = Button(main_window, text="Delete", width=10)
delete_button.grid(row=6, column=3)

exit_button = Button(main_window, text="Exit", width=10)
exit_button.grid(row=7, column=3)

# scrollbar

scrollbar = Scrollbar(main_window)
scrollbar.grid(row=2, column=2, rowspan=6)

# output listbox

output_text = Listbox(main_window, width=30, height=10, yscrollcommand=scrollbar.set)
output_text.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar.config(command=output_text.yview())

main_window.mainloop()
