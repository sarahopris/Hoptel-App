class Guest:
    llname = []
    lfname = []

    def __init__(self, last_name, first_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_lastName(self):
        return self.last_name

    def set_lastName(self, last_name):
        self.last_name = last_name

    def get_firstName(self):
        return self.first_name

    def set_firstName(self, first_name):
        self.first_name = first_name

    def __str__(self):
        return self.first_name + "," + self.last_name


def read_file_guest():
    with open("guests.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            line_sep = line.split('/')
            guest = Guest(line_sep[0], line_sep[1])
            guest.llname.append(line_sep[0])
            guest.lfname.append(line_sep[1])


def append_file_guest():
    guest = Guest
    with open("guests.txt", 'a') as f:
        f.write('\n')
        f.write(str(guest.llname[-1]) + "/" + str(guest.lfname[-1]) + "/")


def write_file_guest():
    guest = Guest
    with open("guests.txt", 'w') as f:
        for i in range(len(guest.llname) - 1):
            f.write(str(guest.llname[i]) + "/" + str(guest.lfname[i]) + "/")
            f.write('\n')
        f.write(str(guest.llname[-1]) + "/" + str(guest.lfname[-1]) + "/")

