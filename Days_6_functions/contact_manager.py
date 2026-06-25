"""A little project to revise function, dictionnaries, and lists 
    
    Users can :
    - Add a contact (dictionnary with informations => name, tel)
    - Show the contact's list 
"""
user_contact = []
def menu():
    print("""
            Welcome to contact Manager CLI App

            Choose an option :
            1. Add a contact
            2. Show contacts
          """)
    try:    
        user_option = int(input("Choose option (1 or 2) "))
        handle_user_option (user_option)
        
    except ValueError as e:
        print(e)
        menu()


    

def handle_user_option (option):
    while (option != 1 and option != 2):
        print("Input is incorrect . Try again\n")
        menu()
    if option == 1:
        try:
            name_contact = input("enter the name's contact ")
            tel_contact = int(input("enter tel contact "))
            add_contact({"name": name_contact, "tel": tel_contact}, user_contact)
        except:
            print("tel contact must be digit ")
        menu()
    else:
        show_contact(user_contact)
    
def add_contact (contact, contacts):
    """Users can add contact.
        Args :
            contact (dict) : Users's contact to add
            contact_list(list) : DSA to simulate DB
        Returns :
            contact_list
    """
    if contact in contacts:
        print(f"Sorry this contact exists already ! Your input : name :{contact["name"]} , Tel:{contact["tel"]} ")
        show_contact()
    contacts.append(contact)
    print("Contact Added !")
    menu()

def show_contact(contacts):
    """Show all User's contact."""
    if not contacts : 
        print("Vous n'avez encore aucun contact")
        menu()
    for contact in contacts:
        print(f"\nContact {contact["name"]} information\n\t Name :{contact["name"]}\n\t{contact["tel"]}")
    menu()

menu()

    


