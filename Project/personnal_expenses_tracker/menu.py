import expenses
import uuid
import utils
import sys
import time
from datetime import datetime

CATEGORIES = ("Food", "Transport","Housing","Health","Education","Shopping","Other")

def handle_option(option):

    match option:
        case 1 : option_1()
        case 2 : option_2()
        case 3 : option_3()
        case 4 : option_4()
        case 5 : option_5()
        case 6 : exit_menu()


def option_1 ():
    
     while True:
    
        amount = utils.handle_negative_value(input("\nAmount :\t"))

        if amount is not None:
            break
            


         
     user_id = uuid.uuid4().hex

     utils.display_category_menu(CATEGORIES)

     while True:
         category = utils.is_num_option_valid(input("\nCategory :\t"), range(1, len(CATEGORIES) + 1))

         if category is not None : 
             break

         print(f"\nSomething goes wrong ! Try with a value between (1 - 7)\n")


     description = input("\nDescription (optional) :\t ")

     date = datetime.now().strftime("%Y/%m/%d at %H:%M:%S")
     
     expenses.add_expense(
         {
         "id" : user_id,
         "amount" : amount,
         "category" : CATEGORIES[int(category) - 1],
         "description": description,
         "date": date
     })

     print("\nExepense successfully added !\n")


def option_2():

    print(
"""
===== VIEW YOUR EXPENSES =====
          
    1. Show Your Expenses
    2. Show Total Expenses
          
          """
          )


    
    while True:
            user_choice = input("Your Choice :\t")
            

            if utils.is_num_option_valid(user_choice,  range_ = [1,2]) is not None :
                break

            print("\nChoose between (1 - 2)\n")

    if user_choice == "1":

        print(
"""
===== SHOW YOUR EXPENSE INFO  =====
          
    1. Show All Expenses
    2. Show expenses from a specified category

""")
        while True:
            user_choice = input("\nYour Choice :\t")
            

            if utils.is_num_option_valid(user_choice,  range_ = [1,2]) is not None :
                break

            print("\nChoose between (1 - 2)\n")


        if user_choice == "1":

            expenses.display_expense()

        else:

            utils.display_category_menu(CATEGORIES)

            while True :

                num_category_option = utils.is_num_option_valid(input("\nYou have to choose between (1 - 7). Try Again !\nCategory :\t"), range(1, len(CATEGORIES) + 1))

                if num_category_option is not None:
                    break  

            expenses.display_expense(expense_category =  CATEGORIES[num_category_option - 1])
    
    else:
                print(
"""
===== SHOW YOUR TOTAL EXPENSES ACCOUNT=====
          
    1. Show Total Expenses
    2. Show Total per Category

""")
                while True:
                    user_choice = input("Your Choice :\t")
                            
                
                    if utils.is_num_option_valid(user_choice,  range_ = [1,2]) is not None :
                        break
                
                    print("Choose between (1 - 2)\n")
                
                
                if user_choice == "1":
                
                    expenses.display_total_expense()
                
                else:
                    
                    expenses.display_total_expense_per_category()
                

def option_3():

     print("\n===== UPDATE EXPENSE =====\n")

     while True:
         
         id = input("\nPlease Enter the ID of expense that you want modify\n ID :\t")
         id_exists = expenses.find_expense_index(id)

         if id_exists is not None:
             break

         print("There's no expense with this ID . Try Again ! \n")


     while True :
        amount = utils.handle_negative_value(input("\nAmount :\t"))

        if amount is not None:
            break
         
     utils.display_category_menu(CATEGORIES)

     while True :

        category = utils.is_num_option_valid(input("\nYou have to choose between (1 - 7). Try Again !\nCategory :\t"), range(1, len(CATEGORIES) + 1))

        if category is not None:
            break


     description = input("Description (optionnal) :\t ")

     expenses.update_expense(expense_id = id, 
                              new_exp_info = 
                              {
                                  "amount": amount,
                                  "category": CATEGORIES[category - 1],
                                  "description":description
                              })

     print("\n Expense successfully Updated\n")


def option_4():
     
     print("\n===== DELETE EXPENSE =====\n")

     id = input("Please Enter the ID of expense that you want modify\n ID :\t")
  
     while True :
        id_exists = expenses.find_expense_index(id)

        if id_exists is not None:
            break

        id = input("\nThere's no expense with this ID . Try Again ! \n ID :\t")
         
     expenses.delete_expense(id)

     print("\nExpense successfully deleted .\n")
     

def option_5():

    while True : 
        expense_id = input("\nEnter Expense ID :\t")
        id_exists = expenses.find_expense_index(expense_id)

        if id_exists is not None :
            break

        print("\nThere's no expense with this Id \tPlease Try Again.\n")

    expenses.display_expense(expense_id)


def show_main_menu():
    print(
        """
    =================================================
                 NOVATECH EXPENSES TRACKER
    =================================================
    
    1. Add a new expense
    2. View expenses
    3. Update an expense
    4. Delete an expense
    5. Search an expense
    6. Exit
    
    ----------------------------------------------
    
        """
    )
    

def exit_menu():

    print("System is shutting down ...")
    time.sleep(3)
    print("shutting down ...")
    time.sleep(1)

    
    sys.exit()