from abc import ABC, abstractmethod
''' 
this is the start of my final project.
The code will create the managing
system for a movie theater
'''

class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Employee(Person):
    def __init__(self, name, email, position):
        super().__init__(name, email)
        self.position = position
        A.employees[name] = position
        
class Customer(Person):
    def __init__(self, name, email):
        super().__init__(name, email)
        A.customers[name] = email

    def buytik(self, movie, room, seat, payment):
        if movie.price > payment:
            print ("Not sufficient funds")
            exit(1)
        elif T.rooms["room"+str(room)].seats[f"seat{str(seat)}"].taken == True:
            print ("Seat is already reserved")
            exit(1)
        else:
            self.ticket = Ticket(movie, room, seat, movie.price)
        T.rooms["room"+str(room)].findseat(seat).buy()

    def canceltik(self):
        T.rooms[self.ticket.room].findseat(self.ticket.seat).cancel()
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
        self.__title = title
        self.__price = price
        self.__room = T.rooms[("room" + str(room))]

    @property
    def title(self):
        return self.__title
    
    @property
    def price(self):
        return self.__price
    
    @property
    def room(self):
        return self.__room

class Room:
    def __init__(self, number):
        self.__location = number
        self.__seats = {"seat"+str(i): Seat(i) for i in range(1,31)}

    def findseat(self, seatnumber):
        for i in self.seats:
            if "seat"+str(seatnumber) == i:
                return self.seats[i]
    
    @property
    def location(self):
        return self.__location

    @property
    def seats(self):
        return self.__seats
    
class Theater:
    def __init__(self):
        self.__rooms = {"room"+str(i): Room(i) for i in range(1,11)}

    @property
    def rooms(self):
        return self.__rooms

class Seat:
    def __init__(self, number):
        self.__number = number
        self.__taken = False

    def buy(self):
        self.taken = True

    def cancel(self):
        self.taken = False

    @property
    def number(self):
        return self.__number

    @property
    def taken(self):
        return self.__taken
    
    @taken.setter
    def taken(self, taken):
        if type(taken) == bool:
            self.__taken = taken

class AllPeople:
    def __init__(self):
        self.customers = {}
        self.employees = {}

        
A = AllPeople()
T = Theater()
M1 = Movie("Star Wars", 10, 1)
John = Customer("John", "John@gmail.com")
Jerry = Customer("Jerry", "Jerry@gmail.com")
Tim = Employee("Tim", "Tim@gmail.com", "Manager")
print (A.customers)
print (A.employees)
John.buytik(M1, 1, 1, 10)
print (T.rooms["room1"].seats)
for i in T.rooms["room1"].seats.values():
    print (i.taken)
print (John.ticket.__dict__)
John.canceltik()
print (T.rooms["room1"].seats)
print (John.__dict__)