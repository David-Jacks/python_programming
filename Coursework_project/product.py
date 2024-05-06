#product module

class Product:
    __name = ""
    __cost_price = 0.0
    __selling_price = 0.0
    __available = 0
    __expiring_date = ""

    def __init__(self, name, cp, sp, stock_amt, exp_date):
        self.__name = name
        self.__cost_price = cp
        self.__selling_price = sp
        self.__expiring_date = exp_date
        self.__available = stock_amt

    # updating product info
    def update_product(self, sp):
        self.__selling_price = sp
        
    #product reports
    def pro_reports(self):
        print("==" * 50)
        return (f"Product name -> {self.__name} \nProduct price -> {self.__selling_price} \nnumber of {self.__name} sold \
-> {self.__available} \nExpiring on {self.__expiring_date}\nProfit made on each {self.__name} \
-> {(self.__selling_price - self.__cost_price)} \nAvailable {self.__name} in stock -> {self.__available}")
    
    # string format printing of class
    def __str__(self):
        return (f"{self.__name}")

    #Object representation of products
    # def __repr__(self) -> str:
    #     return (f"{self.__name}")




