import uuid
import expenses
import utils
from datetime import datetime

CATEGORIES = ("Food", "Transport","Housing","Health","Education","Shopping","Other")

def handle_option(option):

    match option:
        case 1 : print("Option 1")
        case 2 : print("Option 2")
        case 3 : print("Option 3")
        case 4 : print("Option 4")
        case 5 : print("Option 5")
        case 6 : print("Option 6")

def option_1 ():


     amount = input("Amount :\t")
     # Verifier si le montant est valide (positif et digit)
     id = uuid.uuid4()

     utils.display_category_menu(CATEGORIES)
     category = input("Category :\t )")

     description = input("Description :\t (optionnal)")

     date = datetime.now().strftime("%Y/%m/%d at %H:%M:%s")
     
     expenses.add_expenses({
         "id" : id,
         "category" : category,
         "description": description,
         "date": date
     })

     

     
     