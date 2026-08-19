import utils
import menu


def main():

    menu.show_main_menu()

    while True :
        user_input = utils.is_num_option_valid(input("\nChoose An Option :\t"))

        if user_input is None:
            print("\nSomething goes wrong\tChoose an Option between (1 - 6).\n")

        else:
            menu.handle_option(user_input)
            menu.show_main_menu()

        

if __name__ == "__main__":
    
    main()



    

    


