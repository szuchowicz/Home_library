import sqlite3


def create_table():
    conn = sqlite3.connect("My_library.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS My_books (ID INTEGER PRIMARY KEY, Author TEXT, Title TEXT, "
                "Year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()


def add_book(author, title, year, isbn):
    conn = sqlite3.connect("My_library.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO My_books VALUES(NULL,?,?,?,?)", (author, title, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("My_library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM My_books")
    all_books = cur.fetchall()
    conn.close()
    return all_books


def search(author="", title="", year="", isbn=""):
    conn = sqlite3.connect("My_library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM My_books WHERE Author=? OR Title=? OR Year=? OR isbn=?", (author, title, year, isbn))
    selected_books = cur.fetchall()
    conn.close()
    return selected_books


def delete_book(book_id):
    conn = sqlite3.connect("My_library.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM My_books WHERE ID=?", (book_id, ))
    conn.commit()
    conn.close()


def update_book(author, title, year, isbn, book_id):
    conn = sqlite3.connect("My_library.db")
    cur = conn.cursor()
    cur.execute("UPDATE My_books SET Author=?, Title=?, Year=?, isbn=? WHERE ID=?", (author, title, year, isbn, book_id))
    conn.commit()
    conn.close()


create_table()


