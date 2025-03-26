''' 
this is the start of my final project.
The code will act as the ticket purchasing
system for a movie theater
'''

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        A.customers[name] = email

    def buytik(self, movie, room, seat, payment):
        if movie.price > payment:
            print ("Not sufficient funds")
            exit(1)
        else:
            self.ticket = Ticket(movie, room, seat, movie.price)
        T.rooms["room"+str(room)].seats[f"seat{str(seat)}"].taken = True

    def canceltik(self):
        T.rooms[self.ticket.room].seats[f"seat{self.ticket.seat}"].taken = False
        del self.ticket


class Ticket:
    def __init__(self, movie, room, seat, price):
        self.movie = movie.title
        self.room = "room"+ str(room)
        self.seat = T.rooms[self.room].seats[f"seat{str(seat)}"].number
        self.price = price
        self.desc = f"{self.movie},{self.seat},{self.price}"
        
class Movie:
    def __init__(self, title, price, room):
        self.title = title
        self.price = price
        self.room = T.rooms[("room" + str(room))]

class Room:
    def __init__(self, number):
        self.location = number
        self.seats = {"seat"+str(i): Seat(i) for i in range(1,31)}

class Theater:
    def __init__(self):
        self.rooms = {"room"+str(i): Room(i) for i in range(1,11)}

class Seat:
    def __init__(self, number):
        self.number = number
        self.taken = False

class AllCustomers:
    def __init__(self):
        self.customers = {}
        
A = AllCustomers()
T = Theater()
M1 = Movie("Star Wars", 10, 1)
John = Customer("John", "John@gmail.com")
Jerry = Customer("Jerry", "Jerry@gmail.com")
print (A.customers)
John.buytik(M1, 1, 1, 10)
print (T.rooms["room1"].seats)
for i in T.rooms["room1"].seats.values():
    print (i.taken)
print (John.ticket.__dict__)
John.canceltik()
print (T.rooms["room1"].seats)
print (John.__dict__)