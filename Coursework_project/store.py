from product import Product
import matplotlib.pyplot as plt
#Store class

class Store:
    __products = []
    __purchases_made = 0
    __profit = 0.0

    def __init__(self, name):
        self.__name = name

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


   
    # generating reports 
    def gen_reports(self):
         # calculating total profit and loses
        #this is to always make sure that the profit amount is not mis calculated, if called multiple times
        self.__profit = 0.0
        for i in range(len(self.__products)):
            self.__profit += self.__products[i].get_profit()
        # printing reports
        print()
        print("-" * 50)
        print(f"The total number of products in {self.__name} is {len(self.__products)}")
        print(f"The estimated profit if all products are out of stock is {self.__profit}")
        print()
        print("Below is the info about the available items in stock currently:")
        for item in self.__products:
            print(f"{item.pro_reports()}")

    # generating graphical report
    def gen_graph(self):
        product_names = []
        stock_amount = []
        pro_list = self.__products
        
        # get the product names and thier coresponding stock value in differnt lists
        for i in range(len(pro_list)):
            product_names.append(pro_list[i].get_pro_name())
            stock_amount.append(pro_list[i].get_stock_amt())
        
        plt.figure(figsize=(6, 4)) #this is the size of the chart
        plt.bar(product_names, stock_amount, color="blue")
        plt.title("Product Stock Analysis")
        plt.xlabel("Product")
        plt.ylabel("Stock Amount")
        # plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()

    #string representation
    def __str__(self):
        return (f"This is {self.__name} store")
