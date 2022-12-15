class form:
    def __init__(self):
        self.fname = " "
        self.lname = " "
        self.id = " "
        self.phone = " "
        self.address = " "
    
    def fill(self):
        while len(self.fname)<2:
            self.fname = input("First Name: ")
            if len(self.fname)<2:
                print("This field is required to fill to continue.")
        while len(self.lname)<2:
            self.lname = input("Last Name: ")
            if len(self.lname)<2:
                print("This field is required to fill to continue.")
        while len(self.id)<2:
            self.id = input("NIC Number: ")
            if len(self.id)<2:
                print("This field is required to fill to continue.")
        while len(self.phone)<2:
            self.phone = input("Phone Number: ")
            if len(self.phone)<2:
                print("This field is required to fill to continue.")
        while len(self.address)<2:    
            self.address = input("Address: ")
            if len(self.address)<2:
                print("This field is required to fill to continue.")
        self.autofilltxts()

    def autofilltxts(self):
        fnamelist = []
        lnamelist = []
        idlist = []
        phonelist = []
        addresslist = []

        ####APPEND FIRST NAME

        with open("firstnames.txt","r") as file:
            for line in file:
                temp = line.strip()
                fnamelist.append(temp)
                
        with open("firstnames.txt","w") as file:
            for i in range(len(fnamelist)):
                file.write(fnamelist[i]+"\n")
            else:
                file.write(self.fname)

        #####APPEND LAST NAME

        with open("lastnames.txt","r") as file:
            for line in file:
                temp = line.strip()
                lnamelist.append(temp)
                
        with open("lastnames.txt","w") as file:
            for i in range(len(fnamelist)):
                file.write(lnamelist[i]+"\n")
            else:
                file.write(self.lname)

        #####APPEND ID'S

        with open("ids.txt","r") as file:
            for line in file:
                temp = line.strip()
                idlist.append(temp)
                
        with open("ids.txt","w") as file:
            for i in range(len(fnamelist)):
                file.write(idlist[i]+"\n")
            else:
                file.write(self.id)

        #####APPEND PHONE NUMBERS

        with open("phones.txt","r") as file:
            for line in file:
                temp = line.strip()
                phonelist.append(temp)
                
        with open("phones.txt","w") as file:
            for i in range(len(fnamelist)):
                file.write(phonelist[i]+"\n")
            else:
                file.write(self.phone)

        #####APPEND ADDRESSES

        with open("addresses.txt","r") as file:
            for line in file:
                temp = line.strip()
                addresslist.append(temp)
                
        with open("addresses.txt","w") as file:
            for i in range(len(fnamelist)):
                file.write(addresslist[i]+"\n")
            else:
                file.write(self.address)
