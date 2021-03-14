import json

from room import *

class RoomRepo:
    def __init__(self):
        self.rooms = []

    def readFile(self):
        with open("rooms.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                line_sep = line.split('/')
                room = Room(line_sep[0], line_sep[1], line_sep[2], line_sep[3], line_sep[4], line_sep[5])
                room.lnumber.append(line_sep[0])
                room.lcapacity.append(line_sep[1])
                room.lprice.append(line_sep[2])
                room.lcolor.append(line_sep[3])
                room.lseaview.append(line_sep[4])
                room.lavailability.append(line_sep[5])


    def writeToFile(self):
        room = Room
        with open("rooms.txt", 'w') as f:
            for i in range(len(room.lnumber) - 1):
                f.write(str(room.lnumber[i]) + ";" + str(room.lcapacity[i]) + ";" + str(room.lprice[i]) + ";" + str(
                    room.lcolor[i]) + ";" + str(room.lseaview[i]) + ";" + str(room.lavailability[i] + ";"))
                f.write('\n')
            f.write(str(room.lnumber[-1]) + ";" + str(room.lcapacity[-1]) + ";" + str(room.lprice[-1]) + ";" + str(
                room.lcolor[-1]) + ";" + str(room.lseaview[-1]) + ";" + str(room.lavailability[-1]) + ";")


    """
    This method  gets the list of rooms from text file "rooms.txt"
    """
    def loadFile(self):
        try:
            with open("rooms.txt", 'r') as f_read:
                savedRooms = json.load(f_read)
                self.rooms.clear()
                for savedRoom in savedRooms:
                    room = Room(*savedRoom)
                    self.rooms.append(room)
        except FileNotFoundError:
            self.rooms = []

    """
    This method updates the text file "rooms.txt"
    """
    def storeToFile(self):

        to_save = []
        for room in self.rooms:
            room_repr = [room.room_id, room.capacity, room.price, room.color, room.sea_view, room.availability]
            to_save.append(room_repr)
        with open("rooms.txt", 'w') as f_write:
            json.dump(to_save, f_write)

    """
    This method adds a room to the list
    input:a given room
    output:the list with the room added
    """
    def add_room(self, room):
        self.loadFile()
        self.rooms.append(room)
        self.storeToFile()

    """
    This method edits the price of a room from the list
    input:a given room_id, a new price
    output:the list with the edited price of the room with the given room_id
    """
    def edit_price(self, room_id, price):
        self.loadFile()
        for room in self.rooms:
            if room.room_id == room_id:
                room.price = price
        self.storeToFile()

    """
    This method searches for a room in the list
    input:a given room_id
    output:the room with the given room_id
    """
    def find_room_by_id(self, room_id):
        self.loadFile()
        for room in self.rooms:
            if room.room_id == room_id:
                return room
        return None

    """
    This method deletes a room from the list
    input:a given room
    output:the list with the room deleted
    """
    def delete_room_by_id(self, room_id):
        self.loadFile()
        room = self.find_room_by_id(room_id)
        if room is not None:
            self.rooms.remove(room)
        self.storeToFile()

    """
    This method returns the rooms list
    """
    def print_rooms(self):
        self.loadFile()
        return self.rooms
