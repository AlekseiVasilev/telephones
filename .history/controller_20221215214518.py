from user_interface import choice
from remove_contact import delete_contact
from add_contact import add_contacts
from edit_contact import edit_contact
from search import search_by

def procedure(choice):
    if choice == 1:
        add_contacts()
    elif choice == 2:
        delete_contact()
    elif choice == 3:
        edit_contact()
    elif choice == 4:
        search_by(atr, search_data)
    elif choice == 5:
        #чтение из файла BD.csv
    elif choice == 


