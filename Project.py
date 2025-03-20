''' 
this is the start of my final project.
The code will act as the ticket purchasing
system for a movie theater
'''

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def buytik(self, movie, room, seat, payment):
        if movie.price > payment:
            print ("Not sufficient funds")
            exit(1)
        else:
            self.ticket = Ticket(movie, room, seat, movie.price)

    def canceltik(self):
        del self.ticket


class Ticket:
    def __init__(self, movie, room, seat, price):
        self.movie = movie.title
        room = "room"+ str(room)
        self.seat = T.rooms[room].seats[f"seat{str(seat)}"].number
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
        

T = Theater()
M1 = Movie("Star Wars", 10, 1)
John = Customer("John", "John@gmail.com")
John.buytik(M1, 1, 12, 10)
print (John.ticket.__dict__)
John.canceltik()
print (John.__dict__)