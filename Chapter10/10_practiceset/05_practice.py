#Class of train with info and functionalititess

class train:

    def BookT(self):
        Book = input("Do you want to book your ticket (y/n)?")
        if(Book == 'y'):
            print("Ticket book successfully")
        else:
            print("No seat is reserved for now, Try again later....")

    def fairInfo(self):
        City = input("Enter the city name: ")

        if(City == "New Bombay"):
            print("The fair of train for New Bombay is Rs/=4590 ")
        elif (City == "Delhi"):
            print("The fair of train for Delhi is Rs/=3500 ")
        elif (City == "Kolkata"):
            print("The fair of train for Kolkata is Rs/=2500 ")
        else:
            print("No fair info available for this city")

    #here i want to see the status and the no of seat i booked.
    def getStatus(self):
        bookedSeat = int(input("Enter the no of seats you have booked online?"))
        if(bookedSeat > 0):
            print("The train is on time and will reach the destination on time.")
            print(f"You have booked {bookedSeat} seats.")
        else:
            print("No seats are booked yet.")

train1 = train()
train1.fairInfo()
train1.BookT()
train1.getStatus()

