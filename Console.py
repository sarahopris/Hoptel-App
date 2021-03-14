from tkinter import *
import Guest_Menu, guest
import Room_Menu, room
import Booking_Menu, Reservierung

rcont = Room_Menu
gcont = Guest_Menu
bcont = Booking_Menu
room_menu = rcont.RoomMenu
guest_menu = gcont.GuestMenu
booking_menu = bcont.BookingMenu
guest.read_file_guest()
Reservierung.read_file_rez()
room.read_file_room()


class Main:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.title("HOTEL")

        self.title = Label(self.master, text="WELCOME!", bg='#A093C4', fg="#4F3A85", font=('times new roman bold', 30)).place(x=300,
                                                                                                               y=40)

        self.subtitle = Label(self.master, text="What do you want to do...", bg='#A093C4', fg="#624D9A",
                              font=('times new roman', 23)).place(x=260, y=110)

        self.button_guest_menu = Button(self.master, text="GUEST MENU", bg='#7F6CB1', fg="#020007", width=15, height=1,
                                       font=('times new roman', 15), command=self.guest_window).place(x=65, y=240)

        self.button_booking_menu = Button(self.master, text="BOOKING MENU", bg='#7F6CB1', fg="#020007", width=15, height=1,
                                       font=('times new roman', 15), command=self.booking_window).place(x=325, y=240)

        self.button_room_menu = Button(self.master, text="ROOM MENU", bg='#7F6CB1', fg="#020007", width=15, height=1,
                                        font=('times new roman', 15), command=self.room_window).place(x=585, y=240)

        self.quit_button = Button(self.master, text="QUIT", bg='#7F6CB1', fg='#020007', font=(None, 12),
                                  command=self.close_window).place(x=730, y=450)

    def close_window(self):
        self.master.destroy()

    def guest_window(self):
        self.guest_window = Toplevel(self.frame)
        app = guest_menu(self.guest_window)

    def booking_window(self):
        self.booking_window = Toplevel(self.frame)
        app = booking_menu(self.booking_window)

    def room_window(self):
        self.room_window = Toplevel(self.frame)
        app = room_menu(self.room_window)

root = Tk()
root.config(bg='#A093C4')
root.geometry("800x500")
main = Main(root)
root.mainloop()
