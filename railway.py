class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getStatus(self):
        print("...............................")
        print(f"The name of train is {self.name}")
        print(f"The seats available in the train are:{self.seats}")
        print("...............................")

    def fareinfo(self):
        print(f"The price of the tickets is : Rs{self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked!!!! your seat number is : {self.seats}")
            self.seats=self.seats-1
        else:
            print("Sorry this train is full !!")

    def cancelTicket(self,seatNo):
        pass

a=Train("Chennai Express:14370",500,40)
a.getStatus()
a.bookTicket()
a.bookTicket()
a.bookTicket()
a.getStatus()

