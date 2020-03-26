class Stock:
    def __init__(self, s, n, pPrice, cPrice):
        #consturtors
        self.__symbol = s
        self.__stock_name= n
        self.__previousClosingPrice = pPrice
        self.__currentPrice = cPrice

# get methods
    def getName(self):
        return self.__name

    def getSymbol(self):
        return self.__symbol

    def getpPrice(self):
        return self.__previousClosingPrice

    def getcPrice(self):
        return self.__currentPrice
   #set methods
    def setpPrice(self, pPrice):
        self.__previousClosingPrice

    def setpPrice(self, cPrice):
        self.__currentPrice

    def getChange(self):
        return ((self.__currentPrice - self.__previousClosingPrice) / self.__previousClosingPrice) * 100

def main():
    myStock = Stock("INTC", "INTEL", 20.5, 20.35)
    print("Stock named", myStock.getName(), 'has changed by', myStock.getChange(), "%")

main()