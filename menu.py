import room

from ReservController import *
from Guest_Menu import *
from RoomController import *
from room import Room
from guest import Guest
from Reservierung import Reservation
from roomRepo import RoomRepo


class Menu:

    def __init__(self):
        self.guest_ctrl = GuestController()
        self.room_ctrl = RoomController()
        self.reserv_ctrl = ReservController()
        self.roomRepo = RoomRepo()

    def main_menu(self):
        while True:
            print('    MAIN MENU    ')
            print('1.Guests Menu')
            print('2.Rooms Menu')
            print('3.Reservations Menu')
            print('0.Exit')
            choice = int(input('Your choice: '))

            if choice == 1:
                self.guest_menu()
                break

            elif choice == 2:
                self.room_menu()
                break

            elif choice == 3:
                self.booking_menu()
                break

            if choice == 0:
                print('Come back soon! :)')
                break

    def guest_menu(self):
        while True:
            print('    GUESTS MENU    ')
            print('1.Add Guest')
            print('2.Edit Last Name')
            print('3.Delete Guest')
            print('4.Print Guests')
            print('9.Main Menu')
            print('0.Exit')
            choice = int(input('Your choice: '))

            if choice == 1:
                try:
                    guest_id = int(input('ID: '))
                    last_name = input('Last name: ')
                    first_name = input('First Name: ')
                    self.guest_ctrl.add_guest(guest_id, last_name, first_name)
                    print('New guest succesfully added!')
                except ValueError:
                    print('Please enter a number')

            elif choice == 2:
                try:
                    guest_id = int(input('ID of the guest: '))
                    last_name = input('New last name: ')
                    self.guest_ctrl.edit_last_name(guest_id, last_name)
                except ValueError:
                    print('Please enter a number')

            elif choice == 3:
                try:
                    guest_id = int(input('ID of the guest: '))
                    self.guest_ctrl.delete_guest_by_id(guest_id)
                    print('Succesfully deleted the guest!')
                except ValueError:
                    print('Please enter a number')

            elif choice == 4:
                guests = self.guest_ctrl.print_guests()
                for guest in guests:
                    print('ID: {0}, Name: {1} {2}'.format(guest.guest_id, guest.last_name, guest.first_name))

            elif choice == 9:
                self.main_menu()
                break

            elif choice == 0:
                print('Come back soon! :)')
                break

            else:
                print('Invalid option.')

    def room_menu(self):
        while True:
            print('    ROOM MENU    ')
            print('1.Add Room')
            print('2.Edit Price')
            print('3.Delete Room')
            print('4.Print Rooms')
            print('9.Main Menu')
            print('0.Exit')
            choice = int(input('Your choice: '))

            if choice == 1:
                try:
                    id = int(input('Number: '))
                    capacity = int(input('Capacity: '))
                    price = int(input('Price: '))
                    color = input('Color: ')
                    sea_view = input('Sea view: ')
                    availability = 'available'
                    room = Room(id, capacity, price, color, sea_view, availability)
                    self.room_ctrl.add_room(room)
                    print('New room succesfully added!')
                except ValueError:
                    print('Please enter a number')

            elif choice == 2:
                try:
                    room_id = int(input('ID of the room: '))
                    price = int(input('New price: '))
                    self.room_ctrl.edit_price(room_id, price)
                    print('Edit price succesfully!')
                except ValueError:
                    print('Please enter a number')

            elif choice == 3:
                try:
                    room_id = int(input('Number of the room: '))
                    self.room_ctrl.delete_room_by_id(room_id)
                    print('Succesfully deleted the room!')
                except ValueError:
                    print('Please enter a number')

            elif choice == 4:
                rooms = self.room_ctrl.print_rooms()
                for room in rooms:
                    print('Number: {0}, Capacity: {1}, Price: {2}, Color: {3}, Sea view: {4}, Availability: {5}'.format(room.room_id, room.capacity, room.price, room.color, room.sea_view, room.availability))

            elif choice == 9:
                self.main_menu()
                break

            elif choice == 0:
                print('Come back soon! :)')
                break

            else:
                print('Invalid option.')


    def booking_menu(self):
        while True:
            print('    RESERVATIONS MENU    ')
            print('1.Book a room')
            print('2.Print bookings')
            print('3.Filter Rooms ')
            print('4.Show free rooms')
            print('9.Main Menu')
            print('0.Exit')
            choice = int(input('Your choice: '))

            if choice == 1:
                try:
                    guest_id = int(input('ID of the guest for the booking: '))
                    guest = self.guest_ctrl.find_guest_by_id(guest_id)
                    room_id = int(input('Number of the room you want to book: '))
                    room = self.room_ctrl.find_room_by_id(room_id)
                    print("Check-in Date: ")
                    print("Format: Month/Day/Year")
                    start_date = input()
                    print("Check-out Date: ")
                    print("Format: Month/Day/Year")
                    end_date = input()
                    for room in self.roomRepo.rooms:
                        f = open('rooms.txt', 'rt')
                        lines = f.readlines()
                        for line in lines:
                            str = line[:-1]
                            comp = str.split('/')
                            data = f.read()
                            data = data.replace('available', 'occupied')
                            f.close()
                            f = open('rooms.txt', 'wt')
                            f.write(data)
                        f.close()

                    booking = Reservation(guest.guest_id, guest.last_name, guest.first_name, room.room_id, start_date, end_date)
                    self.reserv_ctrl.reservation(booking)
                except AttributeError as e:
                    print(e)

            elif choice == 2:
                bookings = self.reserv_ctrl.list_of_bookings()
                for booking in bookings:
                    print('ID: {0}, Name: {1} {2}, Room booked: {3}, Check-in: {4}, Check-out: {5}'.format(booking.guest_id, booking.last_name, booking.first_name, booking.room_id, booking.start_date, booking.end_date))

            elif choice == 3:
                criterion = input('Choose a filter option(price or sea view or both): ')
                if criterion == 'price':
                    print('Show the rooms with price less than: ')
                    price = int(input())
                    filteredrooms = self.room_ctrl.filter_room_by_price(price)
                    for room in filteredrooms:
                        print('Number: {0}, Capacity: {1}, Price: {2}, Color: {3}, Sea view: {4}, Availability: {5}'.format(
                                room.room_id, room.capacity, room.price, room.color, room.sea_view, room.availability))
                elif criterion == 'sea view':
                    print('Do you want a Sea view? ')
                    seaview = input('y/n: ')
                    filteredRooms1 = self.room_ctrl.filter_room_by_view(seaview)
                    for room in filteredRooms1:
                        print('Number: {0}, Capacity: {1}, Price: {2}, Color: {3}, Sea view: {4}, Availability: {5}'.format(
                                room.room_id, room.capacity, room.price, room.color, room.sea_view, room.availability))
                elif criterion == 'both':
                    print('Show the rooms with price less than: ')
                    price = int(input())
                    print('Sea view? ')
                    seaview = input('y/n: ')
                    filteredRooms2 = self.room_ctrl.filter_both(price, seaview)
                    for room in filteredRooms2:
                        print('Number: {0}, Capacity: {1}, Price: {2}, Color: {3}, Sea view: {4}, Availability: {5}'.format(
                                room.room_id, room.capacity, room.price, room.color, room.sea_view, room.availability))

            elif choice == 9:
                self.main_menu()
                break

            elif choice == 0:
                print('Come back soon! :)')
                break

            else:
                print('Invalid option.')


"""
    def booking_menu(self):
        while True:
            print('Customer Menu')
            print('1.Book a room')
            print('2.Print guests and bookings')
            print('3.Filter Rooms ')
            print('4.Show free rooms')
            print('9.Main Menu')
            print('0.Exit')
            choice = input('Your choice: ')
            choice = validate_int(choice)
            if choice == 1:
                guest_id = input('ID of the guest: ')
                guest_id = validate_int(guest_id)
                guest = self.guestRepo.find_guest_by_id(guest_id)
                if guest is not None:
                    print('The available rooms are: ')
                    self.rezRepo.show_free_rooms()
                    print(self.rezRepo.reservation(guest['bookings']))
                else:
                    print('Invalid option!')
            elif choice == 2:
                print("The guests and their bookings:",)
                print(self.rezRepo.list_of_bookings())
            elif choice == 3:
                criterion = input('Choose a filter option(price or sea view or both): ')
                if criterion == 'price':
                    print('Show the rooms with price less than: ')
                    price = int(input())
                    self.roomRepo.print_rooms(self.rezRepo.filter_rooms_by_price(price))
                elif criterion == 'sea view':
                    print('Do you want a Sea view? ')
                    seaview = input('y/n: ' )
                    self.roomRepo.print_rooms(self.rezRepo.filter_rooms_by_seaview(seaview))
                elif criterion == 'both':
                    print('Show the rooms with price less than: ')
                    price = int(input())
                    print('Sea view? ')
                    seaview = input('y/n: ')
                    self.roomRepo.print_rooms(self.rezRepo.filter_both(price, seaview))
                else:
                    print('Enter a valid criterion!')
            elif choice == 4:
                self.rezRepo.show_free_rooms()
            elif choice == 9:
                self.main_menu()
                break
            elif choice == 0:
                print('Thank you for your booking!')
                break
            else:
                print('Invalid option.')

"""

def start_programm():
    x = Menu()
    x.main_menu()


start_programm()
