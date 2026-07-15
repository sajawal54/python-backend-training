from book import Book 

class Library:
   """
  Represent a Library
   """
   def __init__(self):
    self.books = []

   def add_books(self , book):

     self.books.append(book)
     print("Book Added Successfully")

   def show_books(self):
      if len(self.books) == 0:
        print("No Books Available")
        return
      
      for book in self.books:
          book.display_info()
      
   def borrow_book( self , isbn):

      for book in self.books:
         if book.isbn == isbn:
            book.borrow_book()
            return
         
         print("Book  Not Found")

   def remove_book(self , isbn):
       for book in self.books:
          if book.isbn == isbn:
             self.books.remove(book)
             print("Book removed Successfully")
             return
          print("BOOK NOT FOUND")

   def return_book(self, isbn):

        for book in self.books:

            if book.isbn == isbn:
                book.return_book()
                return

        print("Book Not Found") 
      
  