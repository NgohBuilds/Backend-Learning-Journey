import utils
import menu

def main():
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

    user_input = utils.is_num_option_valid(input("\nChoose An Option :\t"))
    
    while user_input is None :
        user_input = utils.is_num_option_valid(input("\nChoose Option between (1 - 6).Try Again !\n Option : \t"))
    menu.handle_option(user_input)

if __name__ == "__main__" or __name__ == "__menu__":
    
    main()



    

    


