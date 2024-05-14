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
# such that when in case a user wanting to enter a choice enters a character instead of a string then validation is checked
def get_int_input(mess) -> int:
    while True:
        user_input = input(mess)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("You entered an incorrect input, you could have killed a thousand!!\nEnter an \
integer value ")
# doing same validation for floating point valies
def get_float_input(mess) -> float:
    while True:
        check = False
        user_input = input(mess)
        try:
            user_input = float(user_input)
            check = True
        except ValueError:
            check = False
        if check:
            return user_input
        else:
            print("You entered an incorrect input, you could have killed a thousand!!\nEnter a \
floating point value ")

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
        user_choice = get_int_input("Waiting for your choice: ")

        if user_choice == 1:
            name = input("What is the name of the product: ")
            cp = get_float_input("How much is the original cost: ")
            sp = get_float_input("How much do you intend to sell it for: ")
            amount = get_int_input("how many of the products are added to store: ")
            item = Product(name, cp, sp, amount, date1)
            user_store.add_product(item)
            print(f"{amount} {name} to be added to {user_store.print_name()}")
        elif user_choice == 2:
            upd_prompt()
            choice = get_int_input("Choose from the options to continue updating: ")
            if choice == 1:
                name = input("Enter name of product: ")
                new_price = get_float_input("Enter new price: ")
                prod_price_update = user_store.update_product(name, new_price, choice)
                if prod_price_update == "":
                    print("Product not found in store, you can try adding to store")
                    continue
                print(prod_price_update)
            elif choice == 2:
                name = input("Enter name of product: ")
                new_name = input("Enter new name: ")
                prod_name_update = user_store.update_product(name, new_name, choice)
                if prod_name_update == "":
                    print("Product not found in store, you can try adding to store")
                    continue
                print(prod_name_update)
            elif choice == 3:
                name = input("Enter name of product: ")
                new_stock_amt = get_int_input("Enter new stock amount: ")
                prod_stock_update = user_store.update_product(name, new_stock_amt, choice)
                if prod_stock_update == "":
                    print("Product not found in store, you can try adding to store")
                    continue
                print(prod_stock_update)
            else:
                print("update canceled")
                continue
            
        elif user_choice == 3:
            # there is a bug here i need to fix -> trying to make the software more safe by confirming users decisions
            product_name = input("Enter the product to take out of store: ")
            del_choice = input(f"Are you sure about the decision to take {product_name} out of {user_store.print_name()}(y or n): ")
            pro_to_del = None
            if del_choice == "y" or del_choice == "Y":
                pro_to_del = user_store.delete_product(product_name)
            else:
                print("deletion terminated!")
                continue
            if pro_to_del == "":
                print("Product not found in store, try adding to store first")
                continue
            print(f"{pro_to_del} is taken out of store")
    
        elif user_choice == 4:
            item = input("Enter the name of the products to query: ")
            print(f"Printing info about {item}....")
            pro_to_query = user_store.pro_info(item)
            if pro_to_query == "":
                print("There is no product like that in the store, you will have to add it first")
            print(pro_to_query)
            
        elif user_choice == 5:
            report = user_store.gen_reports()
            if report == "":
                print("The Store is empty please try adding items")
                continue
           
        elif user_choice == 6:
            print("Generating a graphical report on the products in the store....")
            graph_report = user_store.gen_graph()
            if graph_report == "":
                print("The Store is empty please, there is no data to represent graphically, please add items to store")
                continue
            print("Product Stock Analysis generated!")
            
        elif user_choice == 7:
            query_flag = False
            print("Thank you for using this software to manage your inventory, see you next time!!!")
        else :
            print("you entered an incorrect choice please check, and try again")
            # propmt_user()


main()