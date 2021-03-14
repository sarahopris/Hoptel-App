from Reservierung import *
import json


class ReservierungRepo:

    def __init__(self):
        self.bookings = []
        self.loadFile()
        self.start_date = []
        self.end_date = []

    """
    This method  gets the list of bookings from text file "bookings.txt"
    """

    def loadFile(self):
        try:
            with open("bookings.txt", 'r') as f_read:
                savedBookings = json.load(f_read)
                self.bookings.clear()
                for savedBooking in savedBookings:
                    booking = Reservation(*savedBooking)
                    self.bookings.append(booking)
        except FileNotFoundError:
            self.bookings = []
        except json.decoder.JSONDecodeError:
            self.bookings = []

    """
    This method updates the text file "bookings.txt"
    """

    def storeToFile(self):

        to_save = []
        for booking in self.bookings:
            booking_repr = [booking.guest_id, booking.first_name, booking.last_name, booking.room_id,
                            booking.start_date, booking.end_date]
            to_save.append(booking_repr)
        with open("bookings.txt", 'w') as f_write:
            json.dump(to_save, f_write)

    """
    This method adds an order.txt to the orderList
    input:a given order.txt
    output:the list with the order.txt added
    """

    def reservation(self, booking):
        self.bookings.append(booking)
        self.storeToFile()

    """
    This method returns the bookings list
    """

    def list_of_bookings(self):
        return self.bookings


"""

    def list_of_bookings(self):
        for guest in guests:
            if len(guest['bookings']) != 0:
                print('ID: {0}, Name: {1} {2}, Rooms booked : {3}, Check-in: {4}, Check-out: {5}'.format(guest['id'], guest['first_name'],
                                                                          guest['last_name'], guest['bookings'], self.start_date, self.end_date))

    # filtreaza toate camerele care au pretul mai mic decat cel dat
    def filter_rooms_by_price(self,price):
        filtered_rooms = []
        for room in rooms:
            if int(room['price']) <= price:
                filtered_rooms.append(room)
        return filtered_rooms


    def show_free_rooms(self):
        free_rooms = []
        for room in rooms:
            if self.roomRepo.validate_availability(room['id']):
                free_rooms.append(room)
        return self.roomRepo.print_rooms(free_rooms)


    def reservation(self, guest):
        bookings = []
        no_of_rooms = int(input('How many rooms do you want to book? '))
        for number in range(no_of_rooms):
            picked_room = int(input('Pick a room: '))
            if self.roomRepo.validate_availability(picked_room):
                bookings.append(picked_room)
                self.roomRepo.find_room_by_id(picked_room)['availability'] = 'occupied'
                print("Check-in Date: ")
                month = input("Month: ")
                month = validate_month(month)
                day = input("Day: ")
                day = validate_day(day, month)
                year = input("Year: ")
                year = validate_year(year)
                self.start_date = str(month) + "/" + str(day) + "/" + str(year)
                print("Check-out Date: ")
                month1 = input("Month: ")
                month1 = validate_month(month1)
                day1 = input("Day: ")
                day1 = validate_day(day1, month1)
                year1 = input("Year: ")
                year1 = validate_year(year1)
                self.end_date = str(month1) + "/" + str(day1) + "/" + str(year1)
        return guest.append(bookings)    
"""