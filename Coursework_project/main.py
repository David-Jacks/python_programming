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

#creating a function for update promting
def upd_prompt():
    print("1. update product price: \n2. update product name: \n3. update product amount in stock: \n4. cancel updating") 

# creating a custom input function that is going to validate user inputs to prevent any breakage in the program
def get_input(mess):
    while True:
        user_input = input(mess)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("You entered an incorrect input, you could have killed a thousand!!\nEnter an \
integer value to make a choice from the list of options")


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

    #controling structure of querying
    while query_flag:
        #user prompting
        propmt_user()
        user_choice = get_input("Waiting for your choice: ")

        if user_choice == 1:
            name = input("What is the name of the product: ")
            cp = float(input("How much is the original cost: "))
            sp = float(input("How much do you intend to sell it for: "))
            amount = int(input("how many of the products are added to store: "))
            item = Product(name, cp, sp, amount, date1)
            user_store.add_product(item)
            print(f"{amount} of {name} to be added to {user_store.print_name()}")
            # propmt_user()
        elif user_choice == 2:
            upd_prompt()
            choice = get_input("Choose from the options to continue updating: ")
            if choice == 1:
                name = input("Enter name of product: ")
                new_price = float(input("Enter new price: "))
                print(user_store.update_product(name, new_price, choice))
            elif choice == 2:
                name = input("Enter name of product: ")
                new_name = input("Enter new name: ")
                print(user_store.update_product(name, new_name, choice))
            elif choice == 3:
                name = input("Enter name of product: ")
                new_stock_amt = int(input("Enter new stock amount: "))
                print(user_store.update_product(name, new_stock_amt, choice))
            else:
                print("update canceled")
                continue
            
        elif user_choice == 3:
            product_name = input("Enter the product to take out of store: ")
            user_store.delete_product(product_name)
            print(f"{product_name} is taken out of store")
            # propmt_user()
        elif user_choice == 4:
            item = input("Enter the name of the products to query: ")
            print(f"Printing info about {item}....")
            print(user_store.pro_info(item))
            # propmt_user()
        elif user_choice == 5:
            user_store.gen_reports()
            # propmt_user()
        elif user_choice == 6:
            print("Generating a graphical report on the products in the store")
            user_store.gen_graph()
            # propmt_user()
        elif user_choice == 7:
            query_flag = False
            print("Thank you for using this software to manage your inventory, see you next time!!!")
        else :
            print("you entered an incorrect choice please check, and try again")
            # propmt_user()


main()