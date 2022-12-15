from covidForm import form
from sellerSection import sellerSection
from updateinfo import updateInfo
sell = sellerSection()

class customerSection:
    def __init__(self):
        self.seller = "Chathupa"
        self.mainnum = 2
        self.pnic = ""
        self.idcount = 0
        
    def run(self):
        flag = True
        tlname = ""
        tfname = ""
        tnic = "1"
        isRegistered = False
        print(" PLEASE ENTER YOUR NIC NUMBER TO CONTINUE | PRESS # TO GO BACK ".center(60,'-'))
        while len(tnic)<7:
            tnic = input("-- ")
            if tnic == "#":
                print("WELCOME TO THE ABC FOOD CITY".center(60,'-'))
                print("PLEASE ENTER A NUMBER TO ACCESS THE SYSTEM".center(60,'-'))
                print(" (1) I'm a Manager\n (2) I'm a Customer")
                self.mainnum = int(input("-- "))
                return
            if len(tnic)<7:
                print("NIC number you've entered is in wrong format or invalid. Please enter a valid NIC number.")
            self.pnic = tnic
        #Checking if the member is already Registered to our shop
        with open("ids.txt","r") as file:
            for line in file:
                if tnic in line:
                    isRegistered = True
                    break
                    
        #if the member is registered
        if isRegistered:
            #Check his/her namae to greet and to make sure he succesfully logged
            with open("ids.txt","r") as file2:
                tcount = 0
                for line in file2:
                    if tnic not in line:
                        tcount += 1
                    else:
                        break
            with open("firstnames.txt","r") as file3:
                tcount2 = 0
                for line in file3:
                    if tcount2 != tcount:
                        tcount2 += 1
                    else:
                        tfname = line.strip()
                        break

            with open("lastnames.txt","r") as file4:
                tcount3 = 0
                for line in file4:
                    if tcount3 != tcount:
                        tcount3 += 1
                    else:
                        tlname = line.strip()
                        break

            #MainMenu Starts        
            print("Hello "+tfname,tlname+"!")
            print("Welcome Back! Pick a number to continue")
            while flag:
                print(" (1) Place an order and print a bill\n (2) View Stocks Available\n (3) View Price List\n (4) View/Edit contact information\n (5) Go back to main menu")
                dothis = int(input("-- "))
                while True:
                    ###PLACE AN ORDER AND CREATE BILL
                    if dothis == 1:
                        sell.task1()
                        print("\n")
                        break
                    
                    ###VIEW STOCKS
                    elif dothis == 2:
                        sell.viewstocks()
                        print("\n")
                        break

                    ###VIEW PRICE LIST
                    elif dothis == 3:
                        sell.viewprices()
                        print("\n")
                        break

                    ###VIEW/UPDATE INFORMATION
                    elif dothis == 4:
                        self.getinfo()
                        print("\n")
                        print("  (1) These details are WRONG. I want to update them.\n  (2) These details are CORRECT. Go back")
                        task4num = int(input("-- "))
                        while True:
                            if task4num == 1:
                                info = updateInfo(self.idcount)
                                info.fill()
                                tnic = info.id
                                self.pnic = tnic
                                print("YOUR INFORMATION HAS BEEN SUCCESFULLY UPDATED.")
                                print("\n")
                                break

                            elif task4num == 2:
                                print("\n")
                                break

                            else:
                                print("Invalid input. Please Try again!")
                                task4num = int(input("-- "))
                        break
                        
                    elif dothis == 5:
                        print("WELCOME TO THE ABC FOOD CITY".center(60,'-'))
                        print("PLEASE ENTER A NUMBER TO ACCESS THE SYSTEM".center(60,'-'))
                        print(" (1) I'm a Manager\n (2) I'm a Customer")
                        self.mainnum = int(input("-- "))
                        flag = False
                        break
                    
                    else:
                        print("Invalid input. Please Try again!")
                        dothis = int(input("-- "))
                
            
        #if the member is not registered fill the covid form
        else:
            while True:
                print("--Hello! looks like you are not registered to our shop.")
                print("--Due to the pandemic situation in the country please fill this form to continue")
                print("--You only need to fill it once because our system will save your details.")
                print(" (1)Continue to the Registration Form\n (2)Main Menu")
                num2 = int(input("--"))
                if num2 == 1:
                    f = form()
                    f.fill()
                    print("Thank you Registering!".center(60,'-'))
                    break

                elif num2 == 2:
                    print("WELCOME TO THE ABC FOOD CITY".center(60,'-'))
                    print("PLEASE ENTER A NUMBER TO ACCESS THE SYSTEM".center(60,'-'))
                    print(" (1) I'm a Manager\n (2) I'm a Customer")
                    self.mainnum = int(input("-- "))
                    break

                else:
                    print("Invalid Response. Try again.")

    def getinfo(self):
        fname = ""
        lname = ""
        nic = ""
        phone = ""
        address = ""
        self.idcount = 0
        with open("ids.txt","r") as file:
            for line in file:
                if self.pnic not in line:
                    self.idcount += 1
                else:
                    nic = line.strip()
                    break

        with open("firstnames.txt","r") as file:
            count2 = 0
            for line in file:
                if count2 != self.idcount:
                    count2 += 1
                else:
                    fname = line.strip()
                    break
                
        with open("lastnames.txt","r") as file:
            count3 = 0
            for line in file:
                if count3 != self.idcount:
                    count3 += 1
                else:
                    lname = line.strip()
                    break

        with open("phones.txt","r") as file:
            count4 = 0
            for line in file:
                if count4 != self.idcount:
                    count4 += 1
                else:
                    phone = line.strip()
                    break

        with open("addresses.txt","r") as file:
            count5 = 0
            for line in file:
                if count5 != self.idcount:
                    count5 += 1
                else:
                    address = line.strip()
                    break
        print("YOUR CONTACT INFORMATION".center(60,'-'))
        print("First Name :",fname)
        print("Last Name :",lname)
        print("NIC Number :",nic)
        print("Phone Number :",phone)
        print("Address :",address)
