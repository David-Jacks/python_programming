from product import Product
#Store class

class Store:
    __products = []
    __purchases_made = 0
    __profit = 0.0
    __loses = 0.0

    def __init__(self, name):
        self.__name = name
        print(f"{self.__name} store created successfully")

    #printing the name of the store
    def print_name(self):
        return self.__name

    # adding products to store
    def add_product(self, product):
        self.__products.append(product)
    
    # deleting product from store
    def delete_product(self, product):
        for i in range(len(self.__products)):
            if product == self.__products[i]:
                return self.__products.pop(i)
        return ""

    # generating info about a product
    def pro_info(self, product):
        pro_list = self.__products
        for i in range(len(pro_list)):
            if product == pro_list[i].get_pro_name():
                return(pro_list[i].pro_reports())
        return ""
    
    #updating products in stores
    def update_product(self, name, atr, choice):
        for i in range(len(self.__products)):
            if self.__products[i].get_pro_name() == name:
                if choice == 1:
                    self.__products[i].update_product_price(atr)
                    return ("update completed")
                elif choice == 2:
                    self.__products[i].update_product_name(atr)
                    return("update completed")
                elif choice == 3:
                    self.__products[i].update_product_stock(atr)
                else:
                    return -1
        return ("")


    # calculating total profit and loses
    for i in range(len(__products)):
        __profit += __products[i].get_profit()
    # generating reports 
    def gen_reports(self):
        print("-" * 20)
        print(f"The total number of products in {self.__name} is {len(self.__products)}")
        print(f"The total profit is {self.__profit} and the total loses made is {self.__loses}")
        print()
        print("Below is the info about the available items in stock currently:")
        for item in self.__products:
            print(f"{item.pro_reports()}")

    #string representation
    def __str__(self):
        return (f"This is {self.__name} store")
