

class Book:
  """
  Represent a book in the library
  """

  def __init__(self , title , author , isbn):
      self.title = title
      self.author = author
      self.isbn = isbn
      self.__available = True

  def borrow_book(self):
   if self.__available:
        self.__available = False
        print("Book Borrowed Successfully")
   else:
      print("Book Already Borrowed")

  def return_book(self):
      if not self.__available:
         self.__available = True
         print("Book returned successfully")
      else:
         print("Book is laready available")
  
  def display_info(self):
      """
      Checking the availablity of the book
      """
      status = "Available" if self.__available else "Borrowed"
      """
      Display the detail of the book
      """
      print(f"Title: {self.title}")
      print(f"Author:   {self.author}")
      print(f"ISBN:  {self.isbn}")
      print(f"Status: {status} ")

book1 = Book("Encyclopedia" ,"Sajawal Jameel" , "101")
book2 = Book("SAWAT VALLEY" ,"RSJ" , "102")

book1.display_info()
book2.display_info()



