#product module

class Product:
    def __init__(self, name, cp, sp, stock_amt, date):
        self.__name = name
        self.__cost_price = cp
        self.__selling_price = sp
        self.__available = stock_amt
        self.__date_of_purchase = date

    # updating product info
    def update_product_name(self, name):
        self.__name = name
    
    def update_product_price(self, sp):
        self.__selling_price = sp
    
    def update_product_stock(self, stc_amt):
        self.__available = stc_amt

    #geting the name of the product
    def get_pro_name(self):
        return(self.__name)

    # get available product in stock
    def get_stock_amt(self):
        return self.__available
    
    # get profit on an item
    def get_profit(self):
        return (self.__selling_price - self.__cost_price) * self.__available
    #product reports
    def pro_reports(self):
        print("==" * 50)
        return (f"Product name -> {self.__name} \nProduct price -> {self.__selling_price} \
\nPurchased on {self.__date_of_purchase} \nProfit made on each {self.__name} \
-> {(self.__selling_price - self.__cost_price)}  \nTotal profit to be made -> {(self.__selling_price - self.__cost_price) * self.__available}\
\nAvailable in stock -> {self.__available}")
    
    # string format printing of class
    def __str__(self):
        return (f"{self.__name}")
