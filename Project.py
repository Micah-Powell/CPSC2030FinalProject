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
        self.snacks = []

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


class Food(ABC):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

class Popcorn(Food):
    def __init__(self):
        self.__name = "popcorn"
        self.__price = 6

    def __repr__(self):
        return self.__name
    
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price

class Hotdog(Food):
    def __init__(self):
        self.__name = "hotdog"
        self.__price = 8

    def __repr__(self):
        return self.__name
    
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price

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
        K.movie_list[title] = [price, room]

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
        if self.taken:
            return (f"seat {self.number} is taken")
        else:
            return (f"seat {self.number} is availible")

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

class Kiosk:
    def __init__(self):
        self.movie_list = {}

    def get_movies(self):
        #lists every movie that is currently showing, as well as the price
        for movie, info in self.movie_list.items():
            print (f"{movie} costs ${info[0]} to watch, and is in room {info[1]}.")
    
    def get_seats(self, room):
        #displays which seats are availible
        for i in T.find_room(room).seats:
            print(T.find_room(room).seats[i])
    
    def new_customer(self, name, email):
        #creates a customer with the information provided
        customer = Customer(name, email)
        return customer

    def purchase_ticket(self, customer, movie, room, seat, payment):
        #purchases ticket
        try:
            customer.buytik(movie, room, seat, payment)
        except Exception as e:
            print (f"Ticket Purchase Failed Because {e}")
        
    def cancel_ticket(self, customer):
        #cancels ticket
        try:
            customer.canceltik()
        except Exception as e:
            print(f"Ticket Cancellation Failed Because {e}")

    def show_tickets(self, customer):
        print (customer.ticket)
        
    def order_popcorn(self, customer, payment):
        if payment >= 6:
            customer.snacks += Popcorn()

    def order_hotdog(self, customer, payment):
        if payment >= 8:
            customer.snacks += Hotdog()

    def main_menu(self):
        name = input("what is your name: ")
        if name not in A.customers:
            customer = Customer(name, input("email: "))
        else:
            customer = name
        while True:
            print("\n Main Menu")
            print("1. View Movies")
            print("2. View Seats")
            print("3. Buy Ticket")
            print("4. Cancel Ticket")
            print("5. Buy Food")
            print("6. Show Ticket")
            print("7. Exit")
            choice = input("Enter choice: ")
            

            if choice == "1":
                self.get_movies()
                print ("When buying tickets, the Movie Code is the first letter of every word capitalized")

            elif choice == "2":
                room_number = int(input("Enter room number: "))
                #room = T.find_room(room_number)
                self.get_seats(room_number)

            elif choice == "3":
                room_number = int(input("Room number: "))
                seat = int(input("Seat number: "))
                payment = int(input("Payment: "))
                moviecode = (input("Movie Code: "))
                movie = globals()[moviecode]
                self.purchase_ticket(customer, movie, room_number, seat, payment)

            elif choice == "4":
                self.cancel_ticket(customer)

            elif choice == "5":
                print("1. Popcorn: $6")
                print("2. Hodog: $8")
                fchoice = input("Enter Choice: ")

                if fchoice == "1":
                    payment = int(input("payment: "))
                    if payment >= 6:
                        customer.snacks.append(Popcorn())
                        print (f"Purchase complete, these are your current snacks: {customer.snacks}")
                    else:
                        print ("not sufficient funds")

                elif fchoice == "2":
                    payment = int(input("payment: "))
                    if payment >= 8:
                        customer.snacks.append(Hotdog())
                        print (f"Purchase complete, these are your current snacks: {customer.snacks}")
                    else:
                        print ("not sufficient funds")
            
                else:
                    print("invalid choice, returning to menu")
                
            elif choice == "6": 
                self.show_tickets(customer) 
            elif choice == "7":
                print("Thanks for visiting!")
                break

            else:
                print("Invalid choice.")

        



        
A = AllPeople()
T = Theater()
K = Kiosk()
SW = Movie("Star Wars", 10, 1)
HP = Movie("Harry Potter", 10, 2)
HG = Movie("Hunger Games", 10, 3)
I = Movie("Interstellar", 15, 4)

K.main_menu()
