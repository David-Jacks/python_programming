#product module

class Product:
    __name = ""
    __cost_price = 0.0
    __selling_price = 0.0
    __available = 0
    __date_of_purchase = ""

    def __init__(self, name, cp, sp, stock_amt, date):
        self.__name = name
        self.__cost_price = cp
        self.__selling_price = sp
        self.__available = stock_amt
        self.__date_of_purchase = date

    # updating product info
    def update_product(self, sp):
        self.__selling_price = sp

    #geting the name of the product
    def get_pro_name(self):
        return(self.__name)

    # get profit on an item
    def get_profit(self):
        return (self.__selling_price - self.__cost_price)
    #product reports
    def pro_reports(self):
        print("==" * 50)
        return (f"Product name -> {self.__name} \nProduct price -> {self.__selling_price} \nnumber sold \
-> {self.__available} \nPurchased on {self.__date_of_purchase}\nProfit made on each {self.__name} \
-> {(self.__selling_price - self.__cost_price)} \nAvailable in stock -> {self.__available}")
    
    # string format printing of class
    def __str__(self):
        return (f"{self.__name}")

    #Object representation of products
    # def __repr__(self) -> str:
    #     return (f"{self.__name}")




