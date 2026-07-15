from library import Library
from book import Book

library = Library()

while True:

    print("\n===== Library Management System =====")

    print("1. Add Book")
    print("2. Show Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Remove Book")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        title = input("Enter Title: ")
        author = input("Enter Author: ")
        isbn = input("Enter ISBN: ")

        book = Book(title, author, isbn)

        library.add_books(book)

    elif choice == "2":

        library.show_books()

    elif choice == "3":

        isbn = input("Enter ISBN: ")

        library.borrow_book(isbn)

    elif choice == "4":

        isbn = input("Enter ISBN: ")

        library.return_book(isbn)

    elif choice == "5":

        isbn = input("Enter ISBN: ")

        library.remove_book(isbn)

    elif choice == "6":

        print("Thank You")
        break

    else:

        print("Invalid Choice")