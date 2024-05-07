from store import Store
from product import Product
import datetime
#this is the main python modules
# creating a funtion for prompting
def propmt_user():
    print()
    print("**" * 25)
    print()
    print("Go ahead and choose from the list of choices bellow to perform needed operations")
    print("1. Add Product to store\n2. Update Product\n3. Remove Product from \
store\n4. Generate report on a product\n5. Generate report on store \
\n6. Generate a graphical report \n7. Exit the program")

# generating automatic dates for when products are being added
date1 = datetime.datetime.now().strftime("%Y/%m/%d")
def main():
    #declaring and initializing global variables
    query_flag = True

    #store creation prompt
    print("--------------WELCOME TO FREEDIV, INVENTORY MADE EASY------------------")
    print("The first thing to do is to have a store!!")
    name = input("What should be the name of your store: ")
    user_store = Store(name)
    print(f"A store name {user_store.print_name()} has been created successfully")

    #user prompting
    propmt_user()
    #controling structure of querying
    while query_flag:
        user_choice = int(input("Waiting for your choice: "))
        
        if user_choice == 1:
            name = input("What is the name of the product: ")
            cp = float(input("How much is the original cost: "))
            sp = float(input("How much do you intend to sell it for: "))
            amount = int(input("how many of the products are added to store: "))
            item = Product(name, cp, sp, amount, date1)
            user_store.add_product(item)
            print(f"{amount} of {name} to be added to {user_store.print_name()}")
            propmt_user()
        elif user_choice == 2:
            print("Store products being updated")
        elif user_choice == 3:
            product_name = input("Enter the product to take out of store: ")
            user_store.delete_product(product_name)
            print(f"{product_name} is taken out of store")
            propmt_user()
        elif user_choice == 4:
            item = input("Enter the name of the products to query: ")
            print(f"Printing info about {item}....")
            print(user_store.pro_info(item))
            propmt_user()
        elif user_choice == 5:
            user_store.gen_reports()
            propmt_user()
        elif user_choice == 6:
            print("Generating a graphical report on the products in the store")
            propmt_user()
        elif user_choice == 7:
            query_flag = False
            print("Thank you for using this software to manage your inventory, see you next time!!!")
        else :
            print("you entered an incorrect choice please check, and try again")
            propmt_user()

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