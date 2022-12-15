from sellerSection import sellerSection
from customerSection import customerSection

#####SELLER USERNAME - admin
#####SELLER PASSWORD - admin123
while True:
    try:
        seller = sellerSection()
        customer = customerSection()

        print("WELCOME TO THE ABC FOOD CITY".center(60,'-'))
        print("PLEASE ENTER A NUMBER TO ACCESS THE SYSTEM".center(60,'-'))
        print(" (1) I'm a Manager\n (2) I'm a Customer")
        mainnum = int(input("-- "))

        while True:
            if mainnum == 1:
                seller.run()
                mainnum = seller.mainnum
                
            elif mainnum == 2:
                customer.run()
                mainnum = customer.mainnum

            else:
                print("Invalid Response. Try again.")
                mainnum = int(input("-- "))
    except:
        print("\n")
        print("UNKNOWN ERROR HAS BEEN OCCURED".center(60," "))
        print("PROGRAM IS RESTARTING".center(60," "))
        print("\n")
