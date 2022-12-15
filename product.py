class Product:
    def __init__(self,productName,unitPrice):
        self.productName = productName
        self.unitPrice = unitPrice
        self.checker = 0

    def autoUpdate(self,boughtQuantity):
        productList = []
        quantityList = []
        with open("product.txt",'r') as file:
            for line in file:
                product,quantity = line.strip().split(" ")
                productList.append(product)
                quantityList.append(int(quantity))
                
            if self.productName in productList:
                if boughtQuantity <= quantityList[productList.index(self.productName)]:
                    quantityList[productList.index(self.productName)] = quantityList[productList.index(self.productName)]-boughtQuantity

                elif quantityList[productList.index(self.productName)] == 0:
                    print("\n")
                    print(self.productName, "is out of stock!")
                    self.checker = 1
                    return
                    
                #If Someone buys more than what is left     
                else:
                    print("\n")
                    print("Only",str(quantityList[productList.index(self.productName)])+" "+self.productName+"s left in the store!")
                    self.checker = 1
                    return
                
            else:
                print("\n")
                print(self.productName, "is out of stock!")
                self.checker = 1
                return

        with open("product.txt",'w') as file:
            for i in range(len(productList)-1):
                file.write(productList[i] + " " + str(quantityList[i]) + "\n")
            else:
                file.write(productList[-1] + " " + str(quantityList[-1]))

            
    def manualUpdateADD(self,boughtQuantity):
        productList = []
        quantityList = []
        priceList = []
        with open("product.txt",'r') as file:
            for line in file:
                product,quantity = line.strip().split(" ")
                productList.append(product)
                quantityList.append(int(quantity))
                
            if self.productName in productList:
                quantityList[productList.index(self.productName)] = quantityList[productList.index(self.productName)]+ boughtQuantity

        with open("price.txt","r") as file:
            for line in file:
                price = line.strip().split(" ")[1]
                priceList.append(price)

            if self.productName in productList:
                priceList[productList.index(self.productName)] = self.unitPrice
                
        if self.productName in productList:
            with open("product.txt",'w') as file:
                for i in range(len(productList)-1):
                    file.write(productList[i] + " " + str(quantityList[i]) + "\n")
                else:
                    file.write(productList[-1] + " " + str(quantityList[-1]))
            with open("price.txt",'w') as file:
                for i in range(len(productList)-1):
                    file.write(productList[i] + " " + str(priceList[i]) + "\n")
                else:
                    file.write(productList[-1] + " " + str(priceList[-1]))
            
        else:
            with open("price.txt",'w') as file:
                for i in range(len(productList)):
                    file.write(productList[i] + " " + str(priceList[i]) + "\n")
                else:
                    file.write(self.productName + " " + str(self.unitPrice))
            with open("product.txt",'w') as file:
                for i in range(len(productList)):
                    file.write(productList[i] + " " + str(quantityList[i]) + "\n")
                else:
                    file.write(self.productName + " " + str(boughtQuantity))

    def manualUpdateMINUS(self,boughtQuantity):
        productList = []
        quantityList = []
        priceList = []
        with open("product.txt",'r') as file:
            for line in file:
                product,quantity = line.strip().split(" ")
                productList.append(product)
                quantityList.append(int(quantity))
                
            if self.productName in productList:
                if boughtQuantity <= quantityList[productList.index(self.productName)]:
                    quantityList[productList.index(self.productName)] = quantityList[productList.index(self.productName)]-boughtQuantity

                elif quantityList[productList.index(self.productName)] == 0:
                    print(self.productName, "is out of stock!")
                    return
                    
                #If Someone buys more than what is left     
                else:
                    print("Only",str(quantityList[productList.index(self.productName)])+self.productName+"s left in the store!")
                    return
            else:
                print(self.productName, "is out of stock!")
                return
            
        with open("price.txt","r") as file:
            for line in file:
                price = line.strip().split(" ")[1]
                priceList.append(price)

            if self.productName in productList:
                priceList[productList.index(self.productName)] = self.unitPrice
                
        if self.productName in productList:
            with open("product.txt",'w') as file:
                for i in range(len(productList)-1):
                    file.write(productList[i] + " " + str(quantityList[i]) + "\n")
                else:
                    file.write(productList[-1] + " " + str(quantityList[-1]))
            with open("price.txt",'w') as file:
                for i in range(len(productList)-1):
                    file.write(productList[i] + " " + str(priceList[i]) + "\n")
                else:
                    file.write(productList[-1] + " " + str(priceList[-1]))
            
        else:
            with open("price.txt",'w') as file:
                for i in range(len(productList)):
                    file.write(productList[i] + " " + str(priceList[i]) + "\n")
                else:
                    file.write(self.productName + " " + str(self.unitPrice))
            with open("product.txt",'w') as file:
                for i in range(len(productList)):
                    file.write(productList[i] + " " + str(quantityList[i]) + "\n")
                else:
                    file.write(self.productName + " " + str(boughtQuantity))
