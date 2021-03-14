from tkinter import *
from guest import *
from Reservierung import *
from room import *


class BookingMenu:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.geometry("800x500")
        self.master.config(bg='#A093C4')
        self.master.title("Booking menu")

        self.title = Label(self.master, text="MAIN MENU", bg='#A093C4', fg="#4F3A85",
                           font=('times new roman bold', 28)).place(x=300, y=40)

        self.book_button = Button(self.master, text="Book a room", bg='#7F6CB1', fg="#020007", width=15, height=1,
                                         font=('times new roman', 15), command=self.book_window).place(x=110, y=200)

        self.show_bookings_button = Button(self.master, text="Show bookings", bg='#7F6CB1', fg="#020007", width=15, height=1,
                                         font=('times new roman', 15), command=self.show_window).place(x=110, y=300)

        self.price_button = Button(self.master, text="Filter by price", bg='#7F6CB1', fg="#020007", width=15,
                                           height=1, font=('times new roman', 15), command=self.price_window).place(x=540, y=150)

        self.view_button = Button(self.master, text="Filter by view", bg='#7F6CB1', fg="#020007", width=15,
                                          height=1, font=('times new roman', 15), command=self.view_window).place(
            x=540, y=250)

        self.both_button = Button(self.master, text="Filter by both", bg='#7F6CB1', fg="#020007", width=15,
                                  height=1, font=('times new roman', 15), command=self.both_window).place(
            x=540, y=350)

        self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                 command=self.close_window).place(x=730, y=450)

        self.quitButton = Button(self.master, text="Quit", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                 command=self.frame.quit).place(x=70, y=450)

        self.helpButton = Button(self.master, text="Help", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                 command=self.help_window).place(x=20, y=450)

    def book_window(self):
        self.booking = Toplevel(self.frame)
        app = BookRoom(self.booking)

    def show_window(self):
        self.show = Toplevel(self.frame)
        app = ShowBookings(self.show)

    def price_window(self):
        self.filterprice = Toplevel(self.frame)
        app = FilterByPrice(self.filterprice)

    def view_window(self):
        self.filterview = Toplevel(self.frame)
        app = FilterByView(self.filterview)

    def both_window(self):
        self.filterboth = Toplevel(self.frame)
        app = FilterByBoth(self.filterboth)

    def help_window(self):
        self.help = Toplevel(self.frame)
        app = Help(self.help)

    def close_window(self):
        self.master.destroy()


class BookRoom:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.guest = Guest
        self.rez = Reservation
        self.room = Room
        self.master.geometry('600x300')
        self.master.config(bg='#A093C4')
        self.master.title("Place order")

        self.lname = Label(self.master, text="Last name", bg='#A093C4', fg="#020007", font=('times new roman', 16)).place(
            x=40, y=40)

        self.entry_lname = Entry(self.master,  bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
        self.entry_lname.place(x=200, y=43)

        self.fname = Label(self.master, text="First name", bg='#A093C4', fg="#020007", font=('times new roman', 16)).place(
                x=40, y=90)

        self.entry_fname = Entry(self.master,  bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
        self.entry_fname.place(x=200, y=93)

        self.number = Label(self.master, text="Room number", bg='#A093C4', fg="#020007",
                            font=('times new roman', 16)).place(x=40, y=140)

        self.entry_number = Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
        self.entry_number.place(x=200, y=139)

        self.check_in_label = Label(self.master, text="Check in", bg='#A093C4', fg="#020007",
                                    font=('times new roman', 16)).place(x=40, y=190)

        self.entry_checkin = Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
        self.entry_checkin.place(x=200, y=189)

        self.check_out_label = Label(self.master, text="Check out", bg='#A093C4', fg="#020007",
                                     font=('times new roman', 16)).place(x=40, y=240)

        self.entry_checkout = Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
        self.entry_checkout.place(x=200, y=239)

        self.enter_button = Button(self.master, text="Enter", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                   command=lambda: self.verify(self.entry_lname.get(), self.entry_fname.get(), self.entry_number.get()))
        self.enter_button.place(x=450, y=240)

        self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                 command=self.close_window).place(x=530, y=240)


    def close_window(self):
        self.master.destroy()

    def verify(self, lname, fname, number):
        """
        Se cauta lname si fname in lista cu user, dc nu se gasesc, mesaj:
        Dc se gaseste, se creeaza entry_title pt film si se config. enter_button legat de functia movie_verify
        :param lname: entry_lname
        :param fname: entry_fname
        """
        self.lname = lname
        self.fname = fname
        self.number = number
        guest_found = False

        for i in range(len(self.guest.llname)):
            if self.guest.llname[i] == self.lname and self.guest.lfname[i] == fname:
                guest_found = True
                break

        if guest_found:
            if self.number not in self.room.lnumber:
                self.msg = Label(self.master, bg='#A093C4', font=(None, 20))
                self.msg.place(x=40, y=240, width=600, height=100)

                self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                         command=self.close_window).place(x=530, y=240)

                self.message = Label(self.master, text="Sorry, the room is not in the list :( ", bg='#A093C4', fg="red",
                                     font=('times new roman', 20))
                self.message.place(x=40, y=200)

            if self.number in self.room.lnumber:
                self.msg = Label(self.master, bg='#A093C4', font=(None, 20))
                self.msg.place(x=40, y=200, width=400, height=400)

                self.add_button = Button(self.frame, text="Place order",
                                         command=self.add_entry(self.entry_lname.get(), self.entry_fname.get(),
                                                                self.entry_number.get(), self.entry_checkin.get(), self.entry_checkout.get(), 'occupied'))
                self.add_button.place(x=400, y=139)

        if not guest_found:
            self.msg = Label(self.master, bg='#A093C4', font=(None, 20))
            self.msg.place(x=40, y=140, width=600, height=200)

            self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                     command=self.close_window).place(x=530, y=240)

            self.message = Label(self.master, text="Sorry, the guest is not in the list :(",  bg='#A093C4', fg="red",
                                 font=('times new roman', 20))
            self.message.place(x=40, y=150)

    def add_entry(self, lname, fname, number, checkin, checkout, availability):
        """
        Se adauga in liste si fisier lname, fname si movie, mesaj
        :param lname: entry_lname
        :param fname: entry_fname
        :param movie: entry_title
        """

        for i in range(len(self.rez.lcamera)):
            if self.rez.lcamera[i] == number:
                if int(self.rez.lcheckout[i][-4:]) == int(checkin[-4:]) and int(self.rez.lcheckout[i][:2]) == int(
                        checkin[:2]):
                    if int(self.rez.lcheckout[i][3:5]) <= int(checkin[3:5]):
                        self.availability = availability
                        self.rez.llname.append(lname)
                        self.rez.lfname.append(fname)
                        self.rez.lcamera.append(number)
                        self.rez.lcheckin.append(checkin)
                        self.rez.lcheckout.append(checkout)
                        append_file_rez()
                        self.message = Label(self.master, text="Room booked! ", bg='#A093C4', fg="#020007",
                                             font=('times new roman', 20))
                        self.message.place(x=40, y=200, width=600, height=100)
                    else:
                        self.message = Label(self.master, text="Room already booked! ", bg='#A093C4', fg="#020007",
                                             font=('times new roman', 20))
                        self.message.place(x=40, y=200, width=600, height=100)
                else:
                    self.availability = availability
                    self.rez.llname.append(lname)
                    self.rez.lfname.append(fname)
                    self.rez.lcamera.append(number)
                    self.rez.lcheckin.append(checkin)
                    self.rez.lcheckout.append(checkout)
                    append_file_rez()
                    self.message = Label(self.master, text="Room booked! ", bg='#A093C4', fg="#020007",
                                         font=('times new roman', 20))
                    self.message.place(x=40, y=200, width=600, height=100)
                    break
    def change_entry(self, availability):
        """
        Se schimba last name in fisierele user si order si mesaj
        :param lastname: entry_new_lname
        """
        for i in range(len(self.rez.lcamera)):
            if self.room.lnumber[i] == self.rez.lcamera[i]:
                self.poz = i

        self.room.lavailability[self.poz] = availability
        write_file_room()


class ShowBookings:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.guest = Guest
        self.rez = Reservation
        self.room = Room
        self.master.config(bg='#A093C4')
        self.master.title("Total order")

        t = Text(self.frame)
        for i in range(len(self.rez.llname)):
            t.insert(END, "Name: " + self.rez.llname[i] + ' ' + self.rez.lfname[i] +', Room: ' + self.rez.lcamera[i] +', Check-in: ' + self.rez.lcheckin[i] +', Check-out: ' + self.rez.lcheckout[i] + '\n')
        t.grid()

        self.backButton = Button(self.frame, text="Back", font=(None, 12), command=self.close_window)
        self.backButton.grid(row=8, sticky=SE)

    def close_window(self):
        self.master.destroy()


class FilterByPrice:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.room = Room
        self.master.geometry('600x500')
        self.master.config(bg='#A093C4')
        self.master.title("Filter rooms by price")

        self.price_label = Label(self.master, text="Price", bg='#A093C4', fg="#020007", font=('times new roman', 16)).place(
            x=40, y=40)

        self.entry_price = Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
        self.entry_price.place(x=150, y=43)

        self.filter_price_button = Button(self.master, text="Filter", bg='#7F6CB1', fg='#020007', font=(None, 12), command=lambda: self.search(self.entry_price.get()))
        self.filter_price_button.place(x=400, y=41)

        self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                 command=self.close_window).place(x=530, y=440)

    def close_window(self):
        self.master.destroy()

    def search(self, price):
        """
        Se cauta camerele cu rating-ul mai mare decat entry_rating
        Mesaj dc nu sunt filme cu rating mai mare decat entry_rating
        :param rating: entry_rating
        """
        self.price = price
        room_found = False
        list_rooms = []
        for i in range(len(self.room.lprice)):
            if float(self.room.lprice[i]) < float(self.price):
                list_rooms.append(self.room.lnumber[i])
                room_found = True
        if room_found:
            t = Text(self.master, bg='#A093C4', fg='#020007', font=('times new roman', 15))
            for i in range(len(list_rooms)):
                with open("rooms.txt", "r") as f:
                    for line in f:
                        if line[0] == list_rooms[i]:
                            t.insert(END, line + '\n')
            t.place(x=40, y=110)

            self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                     command=self.close_window).place(x=530, y=440)

        else:
            t = Text(self.master, bg='#A093C4', fg='red', font=('times new roman', 18))
            t.insert(END, "Sorry, but there's no room with a price less than " + str(self.price) + " :(")
            t.place(x=40, y=110)

            self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                     command=self.close_window).place(x=530, y=440)


class FilterByView:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.room = Room
        self.master.geometry('600x500')
        self.master.config(bg='#A093C4')
        self.master.title("Filter room by view")

        self.view_label = Label(self.master, text="Sea view ", bg='#A093C4', fg="#020007", font=('times new roman', 16)).place(
            x=40, y=40)

        self.entry_view = Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
        self.entry_view.place(x=150, y=43)

        self.filter_button = Button(self.master, text="Filter", bg='#7F6CB1', fg='#020007', font=(None, 12), command=lambda: self.search(self.entry_view.get()))
        self.filter_button.place(x=400, y=41)

        self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                 command=self.close_window).place(x=530, y=440)

    def close_window(self):
        self.master.destroy()

    def search(self, seaview):
        """
        Se cauta entry_actor in lista cu actori, dc nu se gseste, mesaj
        :param actor: entry_actor
        """
        self.seaview = seaview
        room_found = False
        list_rooms = []
        for i in range(len(self.room.lseaview)):
            if self.room.lseaview[i] == self.seaview:
                list_rooms.append(self.room.lnumber[i])
                room_found = True
        if room_found:
            t = Text(self.master, bg='#A093C4', fg='#020007', font=('times new roman', 15))
            for i in range(len(list_rooms)):
                with open("rooms.txt", "r") as f:
                    for line in f:
                        if line[0] == list_rooms[i]:
                            t.insert(END, line + '\n')
            t.place(x=40, y=110)

            self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                     command=self.close_window).place(x=530, y=440)

        else:
            t = Text(self.master, bg='#A093C4', fg='red', font=('times new roman', 18))
            t.insert(END, "Sorry, but there's no room with sea view " + self.seaview + " :(")
            t.place(x=40, y=110)

            self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                     command=self.close_window).place(x=530, y=440)


class FilterByBoth:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.room = Room
        self.master.geometry('600x500')
        self.master.config(bg='#A093C4')
        self.master.title("Filter room by price & view")

        self.price_label = Label(self.master, text="Price ", bg='#A093C4', fg="#020007", font=('times new roman', 16)).place(
            x=40, y=40)

        self.entry_price = Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
        self.entry_price.place(x=150, y=43)

        self.view_label = Label(self.master, text="Sea view ", bg='#A093C4', fg="#020007",
                                font=('times new roman', 16)).place(
            x=40, y=80)

        self.entry_view = Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
        self.entry_view.place(x=150, y=83)

        self.filter_button = Button(self.master, text="Filter", bg='#7F6CB1', fg='#020007', font=(None, 12), command=lambda: self.search(self.entry_price.get(), self.entry_view.get()))
        self.filter_button.place(x=400, y=41)

        self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                 command=self.close_window).place(x=530, y=440)

    def close_window(self):
        self.master.destroy()

    def search(self, price, seaview):
        """
        Se cauta entry_actor in lista cu actori, dc nu se gseste, mesaj
        :param actor: entry_actor
        """
        self.price = price
        self.seaview = seaview
        room_found = False
        list_rooms = []
        for i in range(len(self.room.lprice)):
            if float(self.room.lprice[i]) < float(self.price):
                if self.room.lseaview[i] == self.seaview:
                    list_rooms.append(self.room.lnumber[i])
                    room_found = True
        if room_found:
            t = Text(self.master, bg='#A093C4', fg='#020007', font=('times new roman', 15))
            for i in range(len(list_rooms)):
                with open("rooms.txt", "r") as f:
                    for line in f:
                        if line[0] == list_rooms[i]:
                            t.insert(END, line + '\n')
            t.place(x=40, y=110)

            self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                     command=self.close_window).place(x=530, y=440)

        else:
            t = Text(self.master, bg='#A093C4', fg='red', font=('times new roman', 18))
            t.insert(END, "Sorry, but there's no room with this specifications :(")
            t.place(x=40, y=110)

            self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                     command=self.close_window).place(x=530, y=440)


class Help:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.geometry('645x130')
        self.master.title("Help")

        t = Text(self.master, bg='#C1B7DB', fg='black')
        t.insert(END, "If you want to book a room, choose BOOK A ROOM" + '\n' +
                 "If you want to see all of the bookings, choose SHOW BOOKINGS" + '\n' +
                 "If you want to see the rooms with a price less than ..., choose FILTER BY PRICE" + '\n' +
                 "If you want to see the rooms with or without sea view, choose FILTER BY VIEW" + '\n' +
                 "If you want to see the rooms with a price less than ..., with or without" + '\n' + "sea view, choose FILTER BY BOTH")
        t.grid()

        self.backButton = Button(self.master, text="Back", font=(None, 10), command=self.close_window)
        self.backButton.place(x=600, y=100)

    def close_window(self):
        self.master.destroy()
