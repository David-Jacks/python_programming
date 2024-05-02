from store import Store
from product import Product
import datetime
#this is the main python modules

date1 = datetime.datetime.now().strftime("%Y/%m/%d")
# print(date1 < date2)
def main():
    #declaring and initializing global variables
    user_store = ""
    active_store = False
    query_flag = True

    #user prompting
    print("--------------WELCOME TO FREEDIV, INVENTORY MADE EASY------------------")
    print("Choose from the list of choices bellow to perform needed operations")
    print("1. Create a Store\n2. Add Product to store\n3. Update Product\n4. Remove Product from \
store\n5.Generate report on a product\n6. Generate report on store \
\n7. Generate a graphical report \n8. Exit the program")

    #controling structure of querying
    while query_flag:
        user_choice = int(input("Waiting for your choice: "))
        if user_choice == 1:
            if not active_store:
                name = input("What should be the name of your store: ")
                user_store = Store(name)
                print(f"A store name {user_store.print_name()} has been created successfully")
                print()
                active_store = True
            else :
                print(f"A store named {user_store.print_name()} has already been created, \
you can manage one store at a time, so please try other options to manage your store")
                print()
        elif user_choice == 2:
            name = input("What is the name of the product: ")
            cp = float(input("How much is the original cost: "))
            sp = float(input("How much do you intend to sell it for: "))
            amount = int(input)
            print("Products to be added to the store")
        elif user_choice == 3:
            print("Store products being updated")
        elif user_choice == 4:
            print("Product being taken out of store")
        elif user_choice == 5:
            print("Printing info about a product")
        elif user_choice == 6:
            print("Printing a general report about the store")
        elif user_choice == 7:
            print("Generating a graphical report on the products in the store")
        elif user_choice == 8:
            query_flag = False
            print("Thank you for using this software to manage your inventory, see you next time!!!")
        else :
            print("you entered an incorrect choice please check, and try again")

    # product_A = Product("Biscuit", 20.0, 30.0, date1)
    # product_B = Product("Bag", 10.0, 15.0, date1)
    # print(product_A)

    # Freediv = Store("Freediv")
    # Freediv.add_product(product_A)
    # Freediv.add_product(product_B)
    # print(Freediv)
    # Freediv.gen_reports()
    # pass

main()