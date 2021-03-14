import functionality
from roomRepo import RoomRepo


class RoomController:

    def __init__(self):
        self.roomRepo = RoomRepo()

    """
    This method returns the rooms list
    """
    def print_rooms(self):
        return self.roomRepo.print_rooms()

    """
    This method adds a room to the list
    input:a given room
    output:the list with the room added
    """
    def add_room(self, room):
        self.roomRepo.add_room(room)

    """
    This method searches for a room in the list
    input:a given room_id
    output:the room with the given room_id
    """
    def find_room_by_id(self, room_id):
        room = self.roomRepo.find_room_by_id(room_id)
        if room is None:
            raise AttributeError("There is no movie with this id!")
        return room

    """
    This method edits the price of a room from the list
    input:a given room_id, a new price
    output:the list with the edited price of the room with the given room_id
    """
    def edit_price(self, room_id, price):
        self.roomRepo.edit_price(room_id, price)

    """
    This method deletes a room from the list
    input:a given room
    output:the list with the room deleted
    """
    def delete_room_by_id(self, room_id):
        self.roomRepo.delete_room_by_id(room_id)


    def filter_room_by_view(self, ans):
        sea_views = []
        if ans == 'y':
            for room in self.roomRepo.print_rooms():
                if room.sea_view == 'yes':
                    sea_views.append(room)
        if ans == 'n':
            for room in self.roomRepo.print_rooms():
                if room.sea_view == 'no':
                    sea_views.append(room)
        return sea_views


    def filter_room_by_price(self, price):
        room_by_price = []
        for room in self.roomRepo.print_rooms():
            if int(room.price) <= int(price):
                room_by_price.append(room)
        return room_by_price


    def filter_both(self, price, seaview):
        room_by_price = []
        filtered_rooms = []
        for room in self.roomRepo.print_rooms():
            if int(room.price) <= int(price):
                room_by_price.append(room)
        if seaview == 'y':
            for room1 in room_by_price:
                if room1.sea_view == 'yes':
                    filtered_rooms.append(room1)
        if seaview == 'n':
            for room1 in room_by_price:
                if room1.sea_view == 'no':
                    filtered_rooms.append(room1)
        return filtered_rooms


    """
    This method updates the text file "rooms.txt"
    """
    def storeToFile(self):
        self.roomRepo.storeToFile()


    def validate_price(self, price):
        while functionality.check_float(price) is False or functionality.check_positive(float(price)) is False:
            price = input('Enter a valid price(positive number): ')
        return price

    # camerele pot fi de o persoana, pana la maxim 5 persoane
    def validate_capacity(self, capacity):
        while functionality.check_int(capacity) is False or 1 > int(capacity) or int(capacity) > 5:
            capacity = input('Enter a valid capacity(a number between 1 and 5): ')
        return capacity

    def validate_availability(self, roomNo):
        for room in self.roomRepo.rooms:
            if room['Number'] == roomNo:
                if room['availability'] == 'available':
                    return True
                else:
                    return False