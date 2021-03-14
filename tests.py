from Reservierung import *
import unittest
from GuestRepo import *
from roomRepo import *


class MyTests(unittest.TestCase):

    def testAddGuest(self):
        self.guestRepo = GuestRepo()
        old_length = len(guests)
        bookings = []
        guest1 = {'id': 6, 'first_name': 'Raris', 'last_name': 'Pop',
                  'bookings': bookings}
        self.guestRepo.add_guest(guest1)
        new_length = len(guests)
        self.assertGreater(new_length, old_length)

    def testEditLastName(self):
        self.guestRepo = GuestRepo()
        guest_id = 4
        guest = self.guestRepo.find_guest_by_id(guest_id)
        if guest is not None:
            initial_lastname = guest['last_name']
            last_name = 'Margin'
            guest['last_name'] = last_name

        self.assertNotEqual(initial_lastname, guest['last_name'])

    def testDeleteGuest(self):
        self.guestRepo = GuestRepo()
        old_length = len(guests)
        guest_id = 6
        self.guestRepo.delete_guest_by_id(guest_id)
        new_length = len(guests)
        self.assertGreater(old_length, new_length)

    def testAddRoom(self):
        self.roomRepo = RoomRepo()
        initial_length = len(rooms)
        room1 = {'Number': 5, 'capacity': 3, 'price': 130, 'color': 'red', 'sea view': 'no',
                 'availability': 'available'}
        self.roomRepo.add_room(room1)
        new_length = len(rooms)
        self.assertGreater(new_length, initial_length)

    def testDeleteRoom(self):
        self.roomRepo = RoomRepo()
        old_length = len(rooms)
        self.roomRepo.delete_room_by_id(5)
        new_length = len(rooms)
        self.assertGreater(old_length, new_length)

    def testAvailability(self):
        self.roomRepo = RoomRepo()
        self.assertTrue(self.roomRepo.validate_availability(0))
        self.assertTrue(self.roomRepo.validate_availability(1))
        self.assertTrue(self.roomRepo.validate_availability(2))
        self.assertTrue(self.roomRepo.validate_availability(3))

    def testBooking(self):
        self.roomRepo = RoomRepo()
        self.guestRepo = GuestRepo()
        initial_booking_list = []
        guest_id = 1
        guest = self.guestRepo.find_guest_by_id(guest_id)
        initial_booking_list.append(guest['bookings'])
        bookings = []
        picked_room = 0
        if self.roomRepo.validate_availability(picked_room):
            bookings.append(picked_room)
            self.roomRepo.find_room_by_id(picked_room)['availability'] = 'occupied'

        self.assertFalse(self.roomRepo.validate_availability(picked_room))


if __name__ == '_main_':
    unittest.main()
