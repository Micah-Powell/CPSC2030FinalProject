''' 
this is the start of my final project.
The code will act as the ticket purchasing
system for a movie theater
'''

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def buytik(self, movie, seats, payment):
        pass
        
class Movie:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Room:
    def __init__(self, number):
        self.location = number
        self.seats = {"Seat"+str(i): Seat(i) for i in range(1,31)}

class Theater:
    def __init__(self):
        self.rooms = {"room"+str(i): Room(i) for i in range(1,11)}

class Seat:
    def __init__(self, loc):
        self.loc = loc

        
T = Theater()

print (T.rooms["room1"].seats)
