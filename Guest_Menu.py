from tkinter import *
from guest import *
from Reservierung import *


class GuestMenu:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.geometry("800x500")
        self.master.config(bg='#A093C4')
        self.master.title("Guest menu")

        self.title = Label(self.master, text="GUEST MENU", bg='#A093C4', fg="#4F3A85",
                           font=('times new roman bold', 28)).place(x=300, y=40)

        self.add_guest_button = Button(self.master, text="Add guest", bg='#7F6CB1', fg="#020007", width=15, height=1,
                                      font=('times new roman', 15), command=self.add_guest_window).place(x=110, y=150)

        self.chg_lname_button = Button(self.master, text="Change last name", bg='#7F6CB1', fg="#020007", width=15,
                                       height=1, font=('times new roman', 15), command=self.change_lname_window).place(
            x=110, y=250)

        self.del_guest_button = Button(self.master, text="Delete guest", bg='#7F6CB1', fg="#020007", width=15, height=1,
                                      font=('times new roman', 15), command=self.delete_guest_window).place(x=540, y=150)

        self.guest_list_button = Button(self.master, text="Show guests", bg='#7F6CB1', fg="#020007", width=15, height=1,
                                       font=('times new roman', 15), command=self.show_guest_window).place(x=540, y=250)


        self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                 command=self.close_window).place(x=730, y=450)

        self.quitButton = Button(self.master, text="Quit", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                 command=self.frame.quit).place(x=70, y=450)

        self.helpButton = Button(self.master, text="Help", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                 command=self.help_window).place(x=20, y=450)

    def add_guest_window(self):
        self.add_guest = Toplevel(self.frame)
        app = AddGuest(self.add_guest)

    def change_lname_window(self):
        self.change_lname = Toplevel(self.frame)
        app = ChangeName(self.change_lname)

    def delete_guest_window(self):
        self.delete_guest = Toplevel(self.frame)
        app = DeleteGuest(self.delete_guest)

    def show_guest_window(self):
        self.show_guests = Toplevel(self.frame)
        app = ShowGuest(self.show_guests)

    def help_window(self):
        self.help = Toplevel(self.frame)
        app = Help(self.help)

    def close_window(self):
        self.master.destroy()


class AddGuest:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.guest = Guest
        self.master.geometry('600x300')
        self.master.config(bg='#A093C4')
        self.master.title("Add guest")

        self.lname = Label(self.master, text="Last name", bg='#A093C4', fg="#020007", font=('times new roman', 16)).place(
            x=40, y=40)

        self.entry_lname = Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
        self.entry_lname.place(x=150, y=43)

        self.fname = Label(self.master, text="First name", bg='#A093C4', fg="#020007",
                           font=('times new roman', 16)).place(
            x=40, y=90)

        self.entry_fname = Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
        self.entry_fname.place(x=150, y=93)

        self.enter_button = Button(self.master, text="Enter", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                       command=lambda: self.verify(self.entry_lname.get(), self.entry_fname.get()))
        self.enter_button.place(x=400, y=91)

        self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                 command=self.close_window).place(x=530, y=240)

    def close_window(self):
        self.master.destroy()

    def verify(self, lname, fname):
        """
        Se cauta last name si first name in listele de guest
        Dc se gasesc, mesaj
        Dc nu se gasesc, se adauga in lista si mesaj
        :param lname: entry_lname
        :param fname: entry_fname
        """
        if lname in self.guest.llname and fname in self.guest.lfname:
            self.message = Label(self.master, text="Sorry, the guest is already in the list :(", bg='#A093C4', fg="red",
                                 font=('times new roman', 20))
            self.message.place(x=40, y=150)

        if lname not in self.guest.llname or fname not in self.guest.lfname:
            self.msg = Label(self.master, bg='#A093C4', font=(None, 20))
            self.msg.place(x=40, y=130, width=420, height=110)

            self.message = Label(self.master, text="Guest added successfully! ", bg='#A093C4', fg="#020007",
                                 font=('times new roman', 20))
            self.message.place(x=40, y=150)

            self.guest.llname.append(lname)
            self.guest.lfname.append(fname)

            self.enter_button.config(command=append_file_guest)


class ChangeName:
    def __init__(self, master):
        self.guest = Guest
        self.rez = Reservation
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.geometry('600x300')
        self.master.config(bg='#A093C4')
        self.master.title("Change last name")

        self.lname = Label(self.master, text="Last name", bg='#A093C4', fg="#020007", font=('times new roman', 16)).place(
            x=40, y=40)

        self.entry_lname = Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
        self.entry_lname.place(x=170, y=43)

        self.fname = Label(self.master, text="First name", bg='#A093C4', fg="#020007",
                           font=('times new roman', 16)).place(
            x=40, y=90)

        self.entry_fname = Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
        self.entry_fname.place(x=170, y=93)

        self.enter_button = Button(self.master, text="Enter", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                   command=lambda: self.verify(self.entry_lname.get(), self.entry_fname.get()))
        self.enter_button.place(x=420, y=91)

        self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                 command=self.close_window).place(x=530, y=240)

    def close_window(self):
        self.master.destroy()

    def verify(self, lname, fname):
        """
        Se cauta lname si fname in listele de user
        Dc nu se gasesc, mesaj
        Dc se gasesc, entry nou new last name si se creeaza butonul de change
        :param lname: entry_lname
        :param fname: entry_fname
        """
        self.lname = lname
        self.fname = fname
        found = False
        for i in range(len(self.guest.llname)):
            if self.guest.llname[i] == self.lname and self.guest.lfname[i] == self.fname:
                self.msg = Label(self.master, bg='#A093C4', font=(None, 20))
                self.msg.place(x=40, y=140, width=400, height=200)

                self.poz = i
                self.new_lname = Label(self.master, text="New last name", bg='#A093C4', fg="#020007",
                                       font=('times new roman', 16))
                self.new_lname.place(x=40, y=140)

                self.entry_new_lname = Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
                self.entry_new_lname.place(x=170, y=143)

                self.change_button = Button(self.master, text="Change", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                            command=lambda: self.change_entry(self.entry_new_lname.get()))
                self.change_button.place(x=420, y=141)

                found = True

        if not found:
            self.msg = Label(self.master, bg='#A093C4', font=(None, 20))
            self.msg.place(x=40, y=193, width=600, height=300)

            self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                     command=self.close_window).place(x=530, y=240)

            self.message = Label(self.master, text="Sorry, the guest is not in the list :( ", bg='#A093C4', fg="red",
                                 font=('times new roman', 20))
            self.message.place(x=40, y=180)

    def change_entry(self, lastname):
        """
        Se schimba last name in fisierele user si order si mesaj
        :param lastname: entry_new_lname
        """
        self.guest.llname[self.poz] = lastname
        write_file_guest()
        for i in range(len(self.rez.llname)):
            if self.rez.llname[i] == self.lname and self.rez.lfname[i] == self.fname:
                self.rez.llname[i] = lastname
                write_file_rez()
        self.message = Label(self.master, text="Last name changed successfully! ", bg='#A093C4', fg="#020007",
                             font=('times new roman', 20))
        self.message.place(x=40, y=220)


class DeleteGuest:
    def __init__(self, master):
        self.guest = Guest
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.geometry('600x300')
        self.master.config(bg='#A093C4')
        self.master.title("Delete guest")

        self.lname = Label(self.master, text="Last name", bg='#A093C4', fg="#020007", font=('times new roman', 16)).place(
            x=40, y=40)

        self.entry_lname = Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
        self.entry_lname.place(x=150, y=43)

        self.fname = Label(self.master, text="First name", bg='#A093C4', fg="#020007",
                           font=('times new roman', 16)).place(
            x=40, y=90)

        self.entry_fname = Entry(self.master, bg='#C1B7DB', fg='#020007', font=('times new roman', 15))
        self.entry_fname.place(x=150, y=93)

        self.delete_button = Button(self.master, text="Delete", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                    command=lambda: self.verify(self.entry_lname.get(), self.entry_fname.get()))
        self.delete_button.place(x=400, y=91)

        self.backButton = Button(self.master, text="Back", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                 command=self.close_window).place(x=530, y=240)

    def close_window(self):
        self.master.destroy()

    def verify(self, lname, fname):
        """
        Se cauta lname si fname in lista cu user, dc se gaseste se sterge si se cauta si in lista de order
        Dc se gaseste se sterge si din order
        Dc nu se gaseste un user, mesaj
        :param lname: entry_lname
        :param fname: entry_fname
        """
        found = False
        for i in range(len(self.guest.llname)):
            if self.guest.llname[i] == lname and self.guest.lfname[i] == fname:
                found = True
                self.guest.llname.pop(i)
                self.guest.lfname.pop(i)
                self.delete_button.config(command=write_file_guest)
                break
        if found:
            self.msg = Label(self.master, bg='#A093C4', font=(None, 20))
            self.msg.place(x=20, y=130, width=400, height=200)

            self.message = Label(self.master, text="Guest deleted successfully! ", bg='#A093C4', fg="#020007",
                                 font=('times new roman', 20))
            self.message.place(x=40, y=150)

        if not found:
            self.msg = Label(self.master, bg='#A093C4', font=(None, 20))
            self.msg.place(x=20, y=130, width=400, height=200)

            self.message = Label(self.master, text="Sorry, the guest is not in the list :(", bg='#A093C4', fg="red",
                                 font=('times new roman', 20))
            self.message.place(x=40, y=150)


class ShowGuest:
    def __init__(self, master):
        self.guest = Guest
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.title("User list")

        t = Text(self.frame)
        for i in range(len(self.guest.llname)):
            t.insert(END, "Last Name: " + self.guest.llname[i] + ', First Name: ' + self.guest.lfname[i] + '\n')
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
        self.master.geometry('645x110')
        self.master.title("Help")

        t = Text(self.master, bg='#C1B7DB', fg='black')
        t.insert(END, "If you want to add a guest, choose ADD GUEST" + '\n' +
                 "If you want to change the last name to a guest, choose CHANGE LAST NAME" + '\n' +
                 "If you want to delete a guest, choose DELETE GUEST" + '\n' +
                 "If you want to see the list of guests, choose SHOW GUESTS")
        t.grid()

        self.backButton = Button(self.master, text="Back", font=(None, 10), command=self.close_window)
        self.backButton.place(x=600, y=80)

    def close_window(self):
        self.master.destroy()
