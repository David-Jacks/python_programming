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
        # pro_ind = self.__products.index(product)
        self.__products.remove(product)

    # generating info about a product
    def pro_info(self, product):
        pro_list = self.__products
        for i in range(len(pro_list)):
            if product == pro_list[i].__name:
                return(pro_list[i].pro_reports())
        
    # generating reports 
    def gen_reports(self):
        print("--" * 20)
        for item in self.__products:
            print(f"{item.pro_reports()}")

    #string representation
    def __str__(self):
        return (f"This is {self.__name} store")
