import json
from contact import Contact
from pathlib import Path

class ContactManager:

  def __init__(self):
      self.contacts = []

      self.file_path = Path(__file__).parent / "contacts.json"
      self.load_contacts()
     


  def add_contact(self, name, phone_number, email):

    for contact in self.contacts:
        if contact.phone_number == phone_number:
            print("Number already exists.")
            return

    contact = Contact(name, phone_number, email)

    self.contacts.append(contact)

    print("Contact Added Successfully")


  def save_contacts(self):
    
    data = []

    for contact in self.contacts:
      data.append(contact.to_dic())
    
    with open(self.file_path , "w") as file:
        json.dump(data , file , indent=4)


  def load_contacts(self):
    
    if not self.file_path.exists():
       return
    
    with open(self.file_path , "r") as file:
        data = json.load(file)

    for item in data:
       contact = Contact(item["name"] , item["phone_number"] , item["email"])

       self.contacts.append(contact)

  def show_contacts(self):
     if len(self.contacts) == 0:
        print("No Contact Found")
        return
     
     for contact in self.contacts:
        contact.show_contact_details()


  def search_contacts(self , name):
     
     for contact in self.contacts:
        
        if contact.name.lower() == name.lower():
           print("Contact Found")
           contact.show_contact_details()
           return contact
        
     print("Contact Not Found")
     return None
  

  def update_contacts(self , name ,new_name, new_phone_number , new_email):
     
     for contact in self.contacts:
        
        if contact.name.lower() == name.lower():
           
           contact.name = new_name
           contact.phone_number = new_phone_number
           contact.email = new_email

           self.save_contacts() 
           print("Contact Updated Successfully")

        print("Contact Not Found")


  def delete_contacts(self , name):
     for contact in self.contacts:
        
        if contact.name.lower() == name.lower():
           print("Contact Found")
           self.contacts.remove(contact)
           self.save_contacts()
           print("Contact Removed Successfully")
           return
        
     print("Contact Not found")
       
       


  
     