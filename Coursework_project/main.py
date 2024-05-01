from store import Store
from product import Product
import datetime
#this is the main python modules

date1 = datetime.datetime.now().strftime("%Y/%m/%d")
# print(date1 < date2)
def main():

    print("--------------WELCOME TO FREEDIV, INVENTORY MADE EASY------------------")
    print("Choose from the list of choices bellow to perform needed operation")
    print("1. Create a Store\n2. Add Product to store\n3. Update Product\n4. Remove Product from \
store\n5. Generate report about store \
\n6. Exit the program\nEnter Choice: ")
    
    product_A = Product("Biscuit", 20.0, 30.0, date1)
    product_B = Product("Bag", 10.0, 15.0, date1)
    print(product_A)

    Freediv = Store("Freediv")
    Freediv.add_product(product_A)
    Freediv.add_product(product_B)
    print(Freediv)
    # Freediv.gen_reports()
    # pass

main()