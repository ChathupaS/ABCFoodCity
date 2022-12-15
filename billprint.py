import datetime

class Bill:
    def __init__(self,productList,unitPrice,quantity):
        self.date = datetime.datetime.now()
        self.productList = productList
        self.unitPrice = unitPrice
        self.quantity = quantity

    def printBillHead(self):
        print("-"*60)
        print("ABC FOOD CITY".center(60," "))
        print(str(self.date).center(60," "))
        print("-"*60)

    def printBillFoot(self):
        print("THANK YOU! COME AGAIN!".center(60," "))
        print("-"*60)

    def getTotal(self):
        templist = []
        subTotList = []
        count = 0
        
        with open("product.txt","r") as file:
            for line in file:
                templist.append((line.strip()).split(" ")[0])

        for x in self.productList:
            if x not in templist:
                self.productList.remove(x)
                p = self.quantity.pop(count)
                count += 1
                print("\n")
                print(x,"is not available in our shop right now.")
                print("\n")

        l = len(self.productList)
        
        for value in range(l):
            subTot = self.quantity[value] * self.unitPrice[value]
            subTotList.append(subTot)
        print("Total Price = Rs."+str(sum(subTotList)))

    def printBill(self,paid):
        templist = []
        l = len(self.productList)
        
        self.printBillHead()
        print(("+"+"-"*19)*2+"+"+"-"*18+"+")
        print("|"+"Name".center(19," ")+"|"+"Quantity".center(19," ")+"|"+"Price".center(18," ")+"|")
        print(("+"+"-"*19)*2+"+"+"-"*18+"+")
        subTotList = []
        
        for value in range(l):
            subTot = self.quantity[value] * self.unitPrice[value]
            subTotList.append(subTot)
            print("|{:19s}|{:19s}|{:18s}|".format(self.productList[value]," "+str(self.quantity[value])," "+str(subTot)))
            print("+"+"-"*58+"+")
            
        print(("+"+"-"*19)*2+"+"+"-"*18+"+")
        print(("| Total : Rs."+str(sum(subTotList))).ljust(59)+"|")
        print("+"+"-"*58+"+")
        print(("| Balance : Rs."+str(paid-sum(subTotList))).ljust(59)+"|")
        print("+"+"-"*58+"+")
        self.printBillFoot()



