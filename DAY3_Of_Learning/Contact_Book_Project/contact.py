

class Contact:

  def __init__(self , name , phone_number , email):

    self.name = name
    self.phone_number = phone_number
    self.email = email

  def show_contact_details(self):

    print(f"Name : {self.name}")
    print(f"Phone Number : {self.phone_number}")
    print(f"Email : {self.email}")

  def  to_dic(self):
     return {
      "name" : self.name,
      "phone_number" : self.phone_number,
      "email" : self.email
            }
  