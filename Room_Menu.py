from tkinter import *
from room import *


class RoomMenu:

    def __init__(self, master):
        self.room = Room
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.geometry("800x500")
        self.master.config(bg='#A093C4')
        self.master.title("Room menu")

        self.title = Label(self.master, text="ROOM MENU", bg='#A093C4', fg="#4F3A85",
                           font=('times new roman bold', 28)).place(x=300, y=40)

        self.add_room_button = Button(self.master, text="Add room", bg='#7F6CB1', fg="#020007", width=15, height=1,
                                       font=('times new roman', 15), command=self.add_room_window).place(x=110, y=200)

        self.chg_price_button = Button(self.master, text="Change price", bg='#7F6CB1', fg="#020007", width=15, height=1,
                                       font=('times new roman', 15), command=self.change_price_window).place(x=110,
                                                                                                             y=300)

        self.delete_button = Button(self.master, text="Delete room", bg='#7F6CB1', fg="#020007", width=15, height=1,
                                       font=('times new roman', 15), command=self.delete_room_window).place(x=540,
                                                                                                             y=200)

        self.room_list_button = Button(self.master, text="Show rooms", bg='#7F6CB1', fg="#020007", width=15, height=1,
                                        font=('times new roman', 15), command=self.show_room_window).place(x=540,
                                                                                                             y=300)

        self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                 command=self.close_window).place(x=730, y=450)

        self.quitButton = Button(self.master, text="Quit", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                 command=self.frame.quit).place(x=70, y=450)

        self.helpButton = Button(self.master, text="Help", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                 command=self.help_window).place(x=20, y=450)

    def close_window(self):
        self.master.destroy()

    def help_window(self):
        self.help = Toplevel(self.frame)
        app = Help(self.help)

    def add_room_window(self):
        self.add_room = Toplevel(self.frame)
        app = AddRoom(self.add_room)

    def change_price_window(self):
        self.change_price = Toplevel(self.frame)
        app = ChangePrice(self.change_price)

    def delete_room_window(self):
        self.delete_room = Toplevel(self.frame)
        app = DeleteRoom(self.delete_room)

    def show_room_window(self):
        self.show_room = Toplevel(self.frame)
        app = ShowRooms(self.show_room)


class AddRoom:

    def __init__(self, master):
        self.room = Room
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.geometry('600x300')
        self.master.config(bg='#A093C4')
        self.master.title("Add room")

        self.number = Label(self.master, text="Number", bg='#A093C4', fg="#020007", font=('times new roman', 16)).place(
            x=40, y=40)

        self.entry_number = Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
        self.entry_number.place(x=150, y=43)

        self.add_button = Button(self.master, text="Add", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                 command=lambda: self.verify(self.entry_number.get()))
        self.add_button.place(x=400, y=41)

        self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                 command=self.close_window).place(x=530, y=240)

    def close_window(self):
        self.master.destroy()

    def verify(self, number):
        """
        Se cauta movie in lista cu filme, dc nu se gaseste se formeaza entry_*proprietati film*, add_actors_button
        pt a adauga actori
        Dc se gaseste, mesaj
        :param movie: entry_title
        """
        if number in self.room.lnumber:
            self.message = Label(self.master, text="Sorry, the room already exists :( ", bg='#A093C4', fg="red",
                                 font=('times new roman', 20))
            self.message.place(x=40, y=120)

        if number not in self.room.lnumber:
            self.msg = Label(self.master, bg='#A093C4', font=(None, 20))
            self.msg.place(x=40, y=120, width=400, height=200)

            self.capacity = Label(self.master, text="Capacity", bg='#A093C4', fg="#020007", font=('times new roman', 16)).place(
                x=40, y=90)
            self.entry_capacity = Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
            self.entry_capacity.place(x=150, y=93)

            self.price = Label(self.master, text="Price", bg='#A093C4', fg="#020007",
                                font=('times new roman', 16)).place(x=40, y=140)
            self.entry_price = Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
            self.entry_price.place(x=150, y=139)

            self.color = Label(self.master, text="Color", bg='#A093C4', fg="#020007", font=('times new roman', 16)).place(
                x=40, y=185)
            self.entry_color = Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
            self.entry_color.place(x=150, y=187)

            self.seaview = Label(self.master, text="Sea view", bg='#A093C4', fg="#020007",
                                font=('times new roman', 16)).place(x=40, y=235)

            self.entry_seaview = Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
            self.entry_seaview.place(x=150, y=238)

            self.add_button.configure(
                command=lambda: self.add_entry(self.entry_number.get(), self.entry_capacity.get(), self.entry_price.get(),
                                               self.entry_color.get(), self.entry_seaview.get()))

    def add_entry(self, number, capacity, price, color, seaview):
        """
        se adauga *propr. film* la liste si la fisier, mesaj
        :param movie: entry_title
        :param year: entry_year
        :param rating: entry_rating
        :param price: entry_price
        """
        self.room.lnumber.append(number)
        self.room.lcapacity.append(capacity)
        self.room.lprice.append(price)
        self.room.lcolor.append(color)
        self.room.lseaview.append(seaview)
        availability = 'available'
        self.room.lavailability.append(availability)
        append_file_room()
        self.message = Label(self.master, text="Room added successfully! ", bg='#A093C4', fg="#020007",
                             font=('times new roman', 14))
        self.message.place(x=360, y=138)

class ChangePrice:
    def __init__(self, master):
        self.room = Room
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.geometry('600x300')
        self.master.config(bg='#A093C4')
        self.master.title("Change price")

        self.number = Label(self.master, text="Number", bg='#A093C4', fg="#020007", font=('times new roman', 16)).place(
            x=40, y=40)

        self.entry_number = Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
        self.entry_number.place(x=150, y=43)

        self.enter_button = Button(self.master, text="Enter", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                   command=lambda: self.verify(self.entry_number.get()))
        self.enter_button.place(x=400, y=41)

        self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                 command=self.close_window).place(x=530, y=240)

    def close_window(self):
        self.master.destroy()

    def verify(self, number):
        """
        Se cauta movie in lista cu filme
        Dc se gaseste se creeaza entry_new_price
        Dc nu se gaseste, mesaj
        :param number: entry_number
        :return:
        """
        found = False
        for i in range(len(self.room.lnumber)):
            if number == self.room.lnumber[i]:
                self.msg = Label(self.master, bg='#A093C4', font=(None, 20))
                self.msg.place(x=40, y=120, width=400, height=200)

                self.poz = i
                self.new_price = Label(self.master, text="New price", bg='#A093C4', fg="#020007",
                                       font=('times new roman', 16)).place(x=40, y=90)
                self.entry_new_price = Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
                self.entry_new_price.place(x=150, y=93)

                self.change_button = Button(self.master, text="Change", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                            command=lambda: self.change_entry(self.entry_new_price.get()))
                self.change_button.place(x=400, y=93)

                found = True

        if not found:
            self.msg = Label(self.master, bg='#A093C4', font=(None, 20))
            self.msg.place(x=40, y=93, width=600, height=400)

            self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                     command=self.close_window).place(x=530, y=240)

            self.message = Label(self.master, text="Sorry, the room is not in the list :( ", bg='#A093C4', fg="red",
                                 font=('times new roman', 20))
            self.message.place(x=40, y=180)

    def change_entry(self, price):
        """
        Se inlocuieste pretul vechi cu cel nou in fisier si liste
        :param price: entry_new_price
        """
        self.room.lprice[self.poz] = price
        write_file_room()

        self.message = Label(self.master, text="Price changed successfully! ", bg='#A093C4', fg="#020007",
                                     font=('times new roman', 20))
        self.message.place(x=40, y=180)


class DeleteRoom:
    def __init__(self, master):
        self.room= Room
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.geometry('600x300')
        self.master.config(bg='#A093C4')
        self.master.title("Delete room")

        self.number = Label(self.master, text="Number", bg='#A093C4', fg="#020007", font=('times new roman', 16)).place(
            x=40, y=40)

        self.entry_number= Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
        self.entry_number.place(x=150, y=43)


        self.delete_button = Button(self.master, text="Delete", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                    command=lambda: self.verify(self.entry_number.get()))
        self.delete_button.place(x=400, y=91)

        self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                 command=self.close_window).place(x=530, y=240)

    def close_window(self):
        self.master.destroy()

    def verify(self,number):
        """
        Se cauta lname si fname in lista cu user, dc se gaseste se sterge si se cauta si in lista de order
        Dc se gaseste se sterge si din order
        Dc nu se gaseste un user, mesaj
        :param lname: entry_lname
        :param fname: entry_fname
        """
        found = False
        for i in range(len(self.room.lnumber)):
            if self.room.lnumber[i] == number :
                found = True
                self.room.lnumber.pop(i)
                self.room.lcapacity.pop(i)
                self.room.lprice.pop(i)
                self.room.lcolor.pop(i)
                self.room.lseaview.pop(i)
                self.room.lavailability.pop(i)
                self.delete_button.config(command=write_file_room)
                break
        if found:
            self.msg = Label(self.master, bg='#A093C4', font=(None, 20))
            self.msg.place(x=20, y=130, width=400, height=200)

            self.message = Label(self.master, text="Room deleted successfully! ", bg='#A093C4', fg="#020007",
                                 font=('times new roman', 20))
            self.message.place(x=40, y=150)

        if not found:
            self.msg = Label(self.master, bg='#A093C4', font=(None, 20))
            self.msg.place(x=20, y=130, width=400, height=200)

            self.message = Label(self.master, text="Sorry, the room is not in the list :(", bg='#A093C4', fg="red",
                                 font=('times new roman', 20))
            self.message.place(x=40, y=150)


class ShowRooms:
    def __init__(self, master):
        self.room = Room
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.title("Room list")

        t = Text(self.frame)
        for i in range(len(self.room.lnumber)):
            t.insert(END, 'Number: ' + self.room.lnumber[i] + ', Capacity: ' + self.room.lcapacity[i] + ", Price: " + self.room.lprice[i] + ", Color: " +
                     self.room.lcolor[i] +
                     ", Seaview: " + self.room.lseaview[i] +", " + self.room.lavailability[i] + '\n')
        t.grid()

        self.backButton = Button(self.frame, text="Back", font=(None, 12), command=self.close_window)
        self.backButton.grid(row=8, sticky=SE)

    def close_window(self):
        self.master.destroy()


class Help:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.geometry('530x100')
        self.master.config(bg='#A093C4')
        self.master.title("Help")

        t = Text(self.master, bg='#C1B7DB', fg='black')
        t.insert(END,
                 "If you want to add a room, choose ADD ROOM" + '\n' +
                 "If you want to change the price to a room, choose CHANGE PRICE" + '\n' +
                 "If you want to delete a room, choose DELETE ROOM" + '\n' +
                 "If you want to see the list of rooms, choose SHOW ROOMS")

        t.grid()
        self.backButton = Button(self.master, text="Back", font=(None, 10), command=self.close_window)
        self.backButton.place(x=480, y=65)

    def close_window(self):
        self.master.destroy()