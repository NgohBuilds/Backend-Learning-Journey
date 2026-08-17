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
    
    while True :
        user_input = utils.is_num_option_valid(input("\nChoose An Option :\t"))

        if user_input :
            break

        print("\nSomething goes wrong\tChoose an Option between (1 - 6).\n")

    menu.handle_option(user_input)
    

if __name__ == "__main__" or __name__ == "__menu__":
    
    main()



    

    


