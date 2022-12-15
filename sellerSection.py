from billprint import Bill
from product import Product

class sellerSection:
    def __init__(self):
        self.seller = ["Chathupa","Sandeep"]
        self.mainnum = 1
    def run(self):
        print("PLEASE ENTER LOGIN DETAILS TO CONTINUE".center(60,'-'))
        username = input("USERNAME: ")
        password = input("PASSWORD: ")
        if username == "admin" and password == "admin123":
            flag1 = True
            print("LOGIN SUCCESS".center(60,'-'))
            print("YOU ARE NOW ENTERING THE MANAGEMNET SYSTEM".center(60,'-'))
            print("ENTER A NUMBER TO CONTINUE".center(60,'-'))
            while flag1:
                print(" (1)Create a bill\n (2)Add a new product to the shop\n (3)Update an existing product\n (4)View Stocks\n (5)View Price List\n (6)Go Back")
                managenum = int(input("-- "))
                while True:
                    if managenum == 1:
                        self.task1()
                        break

                    elif managenum == 2:
                        self.task2()
                        break

                    elif managenum == 3:
                        while True:
                            print("   (1) Add Stocks\n   (2) Remove Stocks")
                            task3num = int(input("-- "))
                            if task3num == 1:
                                self.task3_1()
                                break
                            elif task3num == 2:
                                self.task3_2()
                                break
                            else:
                                print("Invalid input")
                        break

                    elif managenum == 4:
                        self.viewstocks()
                        print("\n")
                        break

                    elif managenum == 5:
                        self.viewprices()
                        print("\n")
                        break

                        
                    elif managenum == 6:
                        print("WELCOME TO THE ABC FOOD CITY".center(60,'-'))
                        print("PLEASE ENTER A NUMBER TO ACCESS THE SYSTEM".center(60,'-'))
                        print(" (1) I'm a Manager\n (2) I'm a Customer")
                        self.mainnum = int(input("-- "))
                        username = ""
                        password = ""
                        flag1 = False
                        break

                    else:
                        print("Invalid Response. Try again.")
                        managenum = int(input("-- "))
                
        else:
            print("INVALID USERNAME/PASSWORD!")
            print(" (1) Try again")
            print(" (2) Go back")
            num2 = int(input("-- "))
            while True:
                if num2 == 1:
                    self.mainnum = num2
                    break
                elif num2 == 2:
                    print("WELCOME TO THE ABC FOOD CITY".center(60,'-'))
                    print("PLEASE ENTER A NUMBER TO ACCESS THE SYSTEM".center(60,'-'))
                    print(" (1) I'm a Manager\n (2) I'm a Customer")
                    self.mainnum = int(input("-- "))
                    break
                else:
                    print("Invalid Response. Try again.")
                    print(" (1) Try again")
                    print(" (2) Go back")
                    num2 = int(input("-- "))

    def getProducts(self):
        productPriceList = []
        with open("price.txt","r") as file:
            for line in file:
                temp = line.strip()
                productPriceList.append(temp)
        return productPriceList

    def displayBill(self,pNames,oQuantity,products):
        productList = pNames
        unitPrices = []
        item = 0
        checker2 = 1
        checker3 = 1
        for p in productList:
            for oneP in products: #['Apple 10', 'Mango 20', 'Banana 30', 'Milk 40']
                if p in oneP:
                    checker2 = 0
                    unitP = int(oneP.split(" ")[1])
                    unitPrices.append(unitP)
                    productRemove = Product(p,unitP)
                    productRemove.autoUpdate(oQuantity[item])
                    if productRemove.checker == 1:
                        checker3 = 0
                        break
            if checker3 == 0:
                break
            item+=1

        
        if checker2 == 0 and productRemove.checker == 0 :
            bill = Bill(productList,unitPrices,oQuantity)
            bill.getTotal()
            paid = int(input("PAID (RS.) = "))
            bill.printBill(paid)
            print("\n")
        elif checker2 == 1:
            print("\n")
            print("An item you've choosed is not in our shop right now.")
            print("\n")
            return
        else:
            print("\n")
            return

    def createBill(self,orderList,products):
        pNames = []
        oQuantity = []
        for value in orderList:
            if value == "#":
                break
            n = value.split(" ")
            pNames.append(n[0])
            oQuantity.append(int(n[1]))
        if len(pNames)==0:
            return "!!-------------------- NOTHING BOUGHT --------------------!!"
        self.displayBill(pNames,oQuantity,products)

    def task1(self):
        products = self.getProducts()
        print("!-BILL CREATION STARTED-!")

        itemList = []
        i=1
        item = ""
        addmore = ""
        while addmore != "#":
            print("PRESS 1 TO ADD NEXT ITEM | PRESS # TO STOP ADDING")
            addmore = input("-- ")
            if addmore == "1":
                item = input("ITEM" +str(i)+": ")
                qy = input("QUANTITY: ")
                itemList.append(item+" "+qy)
                
                i+=1
            elif addmore == "#":
                itemList.append("#")
        self.createBill(itemList,products)

##################################################################################
        
    def addNewItem(self,productName,unitPrice,stock):
        prod = Product(productName,unitPrice)
        prod.manualUpdateADD(stock)
        print("NEW ITEM SUCCESFULLY ADDED".center(60,'-'))
        print("\n")
        
    def task2(self):
        print("ADD A NEW ITEM".center(60,'-'))
        name = input("NAME OF THE PRODUCT -- ")
        uprice = int(input("UNIT PRICE OF THE PRODUCT -- "))
        stock = int(input("QUANTITY OF THE PRODUCT -- "))
        self.addNewItem(name,uprice,stock)

###################################################################################

    def addStock(self,productName,unitPrice,stock):
        prod = Product(productName,unitPrice)
        prod.manualUpdateADD(stock)
        print("ITEM UPDATED SUCCESFULLY".center(60,'-'))
        print("\n")

    def removeStock(self,productName,unitPrice,stock):
        current = 0
        current2 = 0
        
        with open("product.txt",'r') as file:
            for line in file:
                if productName in line:
                    current = line.strip().split(" ")[1]
        prod = Product(productName,unitPrice)
        prod.manualUpdateMINUS(stock)
        
        with open("product.txt",'r') as file:
            for line in file:
                if productName in line:
                    current2 = line.strip().split(" ")[1]
        

        if current > current2:
            print("ITEM UPDATED SUCCESFULLY".center(60,'-'))
            print("\n")

    def task3_1(self):
        print("UPDATE STOCK".center(60,'-'))
        name = input("NAME OF THE PRODUCT -- ")
        uprice = int(input("UNIT PRICE OF THE PRODUCT -- "))
        stock = int(input("QUANTITY OF THE PRODUCT -- "))
        self.addStock(name,uprice,stock)

    def task3_2(self):
        print("UPDATE STOCK".center(60,'-'))
        name = input("NAME OF THE PRODUCT -- ")
        uprice = int(input("UNIT PRICE OF THE PRODUCT -- "))
        stock = int(input("QUANTITY OF THE PRODUCT -- "))
        self.removeStock(name,uprice,stock)

    def viewstocks(self):
        plistx = []
        qlistx = []
        print("+"+"-"*57+"+")
        print("|"+"AVAILABLE PRODUCT LIST".center(57,' ')+"|")
        print("+"+"-"*28+"+"+"-"*28+"+")
        with open("product.txt","r") as file:
            for line in file:
                temp = (line.split(" ")[0]).strip()
                plistx.append(temp)
        with open("product.txt","r") as file:
            for line in file:
                temp = (line.split(" ")[1]).strip()
                qlistx.append(temp)
        for i in range(len(plistx)):
            print("|"+plistx[i].center(28," ")+"|"+qlistx[i].center(28)+"|")
        print("+"+"-"*28+"+"+"-"*28+"+")

    def viewprices(self):
        prolist = []
        prilist = []
        print("+"+"-"*57+"+")
        print("|"+"PRICE LIST".center(57,' ')+"|")
        print("+"+"-"*28+"+"+"-"*28+"+")
        with open("price.txt","r") as file:
            for line in file:
                temp = (line.split(" ")[0]).strip()
                prolist.append(temp)
        with open("price.txt","r") as file:
            for line in file:
                temp = (line.split(" ")[1]).strip()
                prilist.append(temp)
        for i in range(len(prolist)):
            print("|"+prolist[i].center(28," ")+"|"+("Rs."+prilist[i]+"/=").center(28)+"|")
        print("+"+"-"*28+"+"+"-"*28+"+")
        
