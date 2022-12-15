class updateInfo:
    def __init__(self,infonum):
        self.infonum = infonum
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
        self.manualfilltxts()

    def manualfilltxts(self):
        fnamelist = []
        lnamelist = []
        idlist = []
        phonelist = []
        addresslist = []

        ####UPDATE FIRST NAME

        with open("firstnames.txt","r") as file:
            for line in file:
                temp = line.strip()
                fnamelist.append(temp)
            fnamelist[self.infonum] = self.fname
                
        with open("firstnames.txt","w") as file:
            for i in range(len(fnamelist)-1):
                file.write(fnamelist[i]+"\n")
            else:
                file.write(fnamelist[-1])

        #####UPDATE LAST NAME

        with open("lastnames.txt","r") as file:
            for line in file:
                temp = line.strip()
                lnamelist.append(temp)
            lnamelist[self.infonum] = self.lname
                
        with open("lastnames.txt","w") as file:
            for i in range(len(fnamelist)-1):
                file.write(lnamelist[i]+"\n")
            else:
                file.write(lnamelist[-1])

        #####UPDATE ID'S

        with open("ids.txt","r") as file:
            for line in file:
                temp = line.strip()
                idlist.append(temp)
            idlist[self.infonum] = self.id
                
        with open("ids.txt","w") as file:
            for i in range(len(fnamelist)-1):
                file.write(idlist[i]+"\n")
            else:
                file.write(idlist[-1])

        #####UPDATE PHONE NUMBERS

        with open("phones.txt","r") as file:
            for line in file:
                temp = line.strip()
                phonelist.append(temp)
            phonelist[self.infonum] = self.phone
                
        with open("phones.txt","w") as file:
            for i in range(len(fnamelist)-1):
                file.write(phonelist[i]+"\n")
            else:
                file.write(phonelist[-1])

        #####UPDATE ADDRESSES

        with open("addresses.txt","r") as file:
            for line in file:
                temp = line.strip()
                addresslist.append(temp)
            addresslist[self.infonum] = self.address
                
        with open("addresses.txt","w") as file:
            for i in range(len(fnamelist)-1):
                file.write(addresslist[i]+"\n")
            else:
                file.write(addresslist[-1])
