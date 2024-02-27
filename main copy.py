import pandas as pd
# A = abstract, B = base, C = class And ABC is Class and abc is module
# So a class which is not supposed to create instances and its rule is to define structure basically
from abc import ABC, abstractmethod

df = pd.read_csv("hotels.csv", dtype = {"id": str}) #dtype will load all the values as strings


class Hotel:
    watermark = "The Real Estate Company"
    def  __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availabilty to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index = False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False
    
    @classmethod #To create class method
    def get_hotel_count(cls, data):
        return len(data)
    
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return  False
        


class Ticket(ABC): 
    # Child of abstract  class ABC
    # So every child class which is inherited from parents class has to implement some method of the parents

    @abstractmethod
    def generate(self):
        pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        name: {self.the_customer_name}
        Hotel name: {self.hotel.name}
        """
        return  content
    
    @property # Making another properties and the method behave like variable 
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name
    
    @staticmethod # Staticmethod do not get self or cls argument and it looks like a function we use some other utilities
    def convert(amount):
        return amount * 1.2


class DigitalTicket(Ticket):
    def generate(self):
        return "Hello. this is your digital ticket"
    
    def download(self):
        pass


hotel1 = Hotel(hotel_id = "188")
hotel2 = Hotel(hotel_id = "134")

print(hotel1.available())

print(hotel1.name)
print(hotel2.name)

print(hotel1.watermark)
print(hotel2.watermark)

print(Hotel.watermark)

print(Hotel.get_hotel_count(data = df))
print(hotel1.get_hotel_count(data = df))

ticket = ReservationTicket(customer_name = "john smith", hotel_object = hotel1)
print(ticket.the_customer_name)

print(ticket.generate())

converted = ReservationTicket.convert(10)
print(converted)
