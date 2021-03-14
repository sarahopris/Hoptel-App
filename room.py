class Room:
    lnumber = []
    lcapacity = []
    lprice = []
    lcolor = []
    lseaview = []
    lavailability = []

    def __init__(self, id, capacity, price, color, sea_view, availability):
        self.id = id
        self.capacity = capacity
        self.price = price
        self.color = color
        self.sea_view = sea_view
        self.availability = availability


    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, capacity):
        self.capacity = capacity

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_view(self):
        return self.sea_view

    def set_view(self, sea_view):
        self.sea_view = sea_view

    def get_availability(self):
        return self.availability

    def set_availability(self, availability):
        self.availability = availability


    def __str__(self):
        return str(self.id) + "," + str(self.capacity) + "," + str(self.price) + "," + self.color + "," + self.sea_view + "," + self.availability


def read_file_room():
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


def write_file_room():
    room = Room
    with open("rooms.txt", 'w') as f:
        for i in range(len(room.lnumber) - 1):
            f.write(str(room.lnumber[i]) + "/" + str(room.lcapacity[i]) + "/" + str(room.lprice[i]) + "/" + str(
                room.lcolor[i]) + "/" + str(room.lseaview[i]) + "/" + str(room.lavailability[i] + "/"))
            f.write('\n')
        f.write(str(room.lnumber[-1]) + "/" + str(room.lcapacity[-1]) + "/" + str(room.lprice[-1]) + "/" + str(
            room.lcolor[-1]) + "/" + str(room.lseaview[-1]) + "/" + str(room.lavailability[-1]) + "/")


def append_file_room():
    room = Room
    with open("rooms.txt", 'a') as f:
        f.write('\n')
        f.write(str(room.lnumber[-1]) + "/" + str(room.lcapacity[-1]) + "/" + str(room.lprice[-1]) + "/" + str(
            room.lcolor[-1]) + "/" + str(room.lseaview[-1]) + "/" + str(room.lavailability[-1]) + "/")
