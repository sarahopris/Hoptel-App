class Reservation:
    llname = []
    lfname = []
    lcamera = []
    lcheckin = []
    lcheckout = []

    def __init__(self, first_name, last_name, id_room, check_in, check_out):
        self.first_name = first_name
        self.last_name = last_name
        self.id_room = id_room
        self.check_in = check_in
        self.check_out = check_out


    def get_firstName(self):
        return self.first_name

    def set_firstName(self, first_name):
        self.first_name = first_name

    def get_lastName(self):
        return self.last_name

    def set_lastName(self, last_name):
        self.last_name = last_name

    def get_roomID(self):
        return self.id_room

    def set_roomID(self, id):
        self.id_room = id

    def get_checkin(self):
        return self.check_in

    def set_checkin(self, check_in):
        self.check_in = check_in

    def get_checkout(self):
        return self.check_out

    def set_checkout(self, check_out):
        self.check_out = check_out


    def __str__(self):
            return self.first_name + "," + self.last_name + "," + str(self.id_room) + "," + str(self.check_in) + "," + str(self.check_out)


def read_file_rez():
    with open("bookings.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            line_sep = line.split('/')
            rez = Reservation(line_sep[0], line_sep[1], line_sep[2], line_sep[3], line_sep[4])
            rez.llname.append(line_sep[0])
            rez.lfname.append(line_sep[1])
            rez.lcamera.append(line_sep[2])
            rez.lcheckin.append(line_sep[3])
            rez.lcheckout.append(line_sep[4])


def append_file_rez():
    rez = Reservation
    with open("bookings.txt", 'a') as f:
        f.write('\n')
        f.write(str(rez.llname[-1]) + "/" + str(rez.lfname[-1]) + "/" + str(rez.lcamera[-1]) + "/" + str(rez.lcheckin[-1]) + "/" + str(rez.lcheckout[-1]) + "/")


def write_file_rez():
    rez = Reservation
    with open("bookings.txt", 'w') as f:
        for i in range(len(rez.llname) - 1):
            f.write(str(rez.llname[i]) + "/" + str(rez.lfname[i]) + "/" + str(rez.lcamera[i]) + "/" + str(rez.lcheckin[i]) + "/" + str(rez.lcheckout[i]) + "/")
            f.write('\n')
        f.write(str(rez.llname[-1]) + "/" + str(rez.lfname[-1]) + "/" + str(rez.lcamera[-1]) + "/" + str(rez.lcheckin[-1]) + "/" + str(rez.lcheckout[-1]) + "/")
