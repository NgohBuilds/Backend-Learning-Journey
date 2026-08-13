import uuid
import expenses
from main import main
import utils
from datetime import datetime

CATEGORIES = ("Food", "Transport","Housing","Health","Education","Shopping","Other")

def handle_option(option):

    match option:
        case 1 : option_1()
        case 2 : print("Option 2")
        case 3 : print("Option 3")
        case 4 : print("Option 4")
        case 5 : print("Option 5")
        case 6 : print("Option 6")
    main()

def option_1 ():

     try:
         amount = utils.handle_negative_value(int(input("Amount :\t")))
     except:
         amount = 0

     while not amount :
        try:
            amount = utils.handle_negative_value(int(input("\nIncorrect Value (either negative value or non-digit). Try Again !\nAmount :\t")))
        except:
            amount = 0
         
     # Verifier si le montant est valide (positif et digit)
     id = uuid.uuid4().hex

     utils.display_category_menu(CATEGORIES)
     category = utils.is_num_option_valid(input("Category :\t"), range(1, len(CATEGORIES) + 1))
     while category is None :
        category = utils.is_num_option_valid(input("\nYou have to choose between (1 - 7). Try Again !\nCategory :\t"), range(1, len(CATEGORIES) + 1))

     description = input("Description (optionnal) :\t ")

     date = datetime.now().strftime("%Y/%m/%d at %H:%M:%S")
     
     expenses.add_expenses({
         "id" : id,
         "amount" : amount,
         "category" : CATEGORIES[int(category) - 1],
         "description": description,
         "date": date
     })
     print("Task Successfully Added ! ")


     

     
     