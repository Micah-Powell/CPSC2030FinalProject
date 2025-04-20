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

class Food(ABC):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

class Popcorn(Food):
    def __init__(self, name, price):
        super().__init__(name, price)

class Hotdog(Food):
    def __init__(self, name, price):
        super().__init__(name, price)

    def buytik(self, movie, room, seat, payment):
        #checks if the payment is sufficient and then creates a ticket based on the information provided and reserves the seat by changing its taken value to True
        if movie.price > payment:
            print ("Not sufficient funds")
            exit(1)
        if T.find_room(room).findseat(seat).taken == True:
            print ("Seat is already reserved")
            exit(1)
        else:
            self.ticket = Ticket(movie, room, seat, movie.price)
        T.find_room(room).findseat(seat).buy()

    def canceltik(self):
        #deletes the ticket from the users attributes and returns the seats taken value to False
        T.find_room(self.ticket.room).findseat(self.ticket.seat).cancel()
        del self.ticket

class AllPeople:
    def __init__(self):
        self.customers = {}
        self.employees = {}

class Ticket:
    def __init__(self, movie, room, seat, price):
        self.__movie = movie.title
        self.__room = room
        self.__seat = T.find_room(room).findseat(seat).number
        self.__price = price
    
    @property
    def movie(self):
        return self.__movie
   
    @property
    def room(self):
        return self.__room
    
    @property
    def seat(self):
        return self.__seat
    
    @property
    def price(self):
        return self.__price
    
    def __repr__(self):
        #changes the display value of printing an object of this class to the string below
        return (f"Movie:{self.movie}, Seat Number:{self.seat}, Ticket Price:{self.price}")
        
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
    
class Theater:
    def __init__(self):
        self.__rooms = {"room"+str(i): Room(i) for i in range(1,11)}

    def find_room(self, roomnumber):
        #searches through theater's rooms untill it finds the desired room and returns that object
        for i in self.rooms:
            if "room"+str(roomnumber) == i:
                return self.rooms[i]

    @property
    def rooms(self):
        return self.__rooms

class Room:
    def __init__(self, number):
        self.__location = number
        self.__seats = {"seat"+str(i): Seat(i) for i in range(1,31)}

    def findseat(self, seatnumber):
        #searches through room's seats untill it finds the desired seat and returns that object
        for i in self.seats:
            if "seat"+str(seatnumber) == i:
                return self.seats[i]
    
    @property
    def location(self):
        return self.__location

    @property
    def seats(self):
        return self.__seats
    

class Seat:
    def __init__(self, number):
        self.__number = number
        self.__taken = False

    def __repr__(self):
        #changes the display value of printing an object of this class to the string below
        return (f"seat {self.number} is taken -->{self.taken}")

    def buy(self):
        #changes the taken value of the seat to True
        self.taken = True

    def cancel(self):
        #changes the taken value of the seat to False
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


        
A = AllPeople()
T = Theater()
M1 = Movie("Star Wars", 10, 1)
# John = Customer("John", "John@gmail.com")
# Jerry = Customer("Jerry", "Jerry@gmail.com")
# Tim = Employee("Tim", "Tim@gmail.com", "Manager")
# print (A.customers)
# print (A.employees)
# John.buytik(M1, 1, 1, 10)
# print (T.rooms["room1"].seats)
# for i in T.rooms["room1"].seats.values():
#     print (i.taken)
# print (John.ticket)
# John.canceltik()
# print (T.rooms["room1"].seats)
# print (John.__dict__)