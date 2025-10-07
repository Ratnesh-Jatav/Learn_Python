#  Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def book_ticket(self):
        if self.seats > 0:
            self.seats -= 1
            print(f"Ticket booked successfully! Seats left: {self.seats}")
        else:
            print("No seats available!")

    def get_status(self):
        print(f"Train: {self.name}, Seats available: {self.seats}")

    def get_fare(self):
        print(f"Fare for train {self.name} is: {self.fare}")
train1 = Train("Express", 500, 100)
train1.get_status()
train1.get_fare()
train1.book_ticket()
train1.get_status() 