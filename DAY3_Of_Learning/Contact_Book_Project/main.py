from contact_manager import ContactManager

manager = ContactManager()

while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Show Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        manager.add_contact(name, phone, email)

    elif choice == "2":

        manager.show_contacts()

    elif choice == "3":

        name = input("Enter Name to Search: ")
        manager.search_contacts(name)

    elif choice == "4":

        name = input("Enter Name to Update: ")
        new_name = input("Enter New Name: ")
        new_phone = input("Enter New Phone Number: ")
        new_email = input("Enter New Email: ")

        manager.update_contacts(name, new_name , new_phone, new_email)

    elif choice == "5":

        name = input("Enter Name to Delete: ")
        manager.delete_contacts(name)

    elif choice == "6":

        print("Thank you for using My Contact Book.")
        break

    else:

        print("Invalid Choice. Please Try Again.")
