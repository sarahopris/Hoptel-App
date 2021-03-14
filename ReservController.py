from ReservierungRepo import ReservierungRepo


class ReservController:

    def __init__(self):
        self.reservRepo = ReservierungRepo()

    """
    This method returns the booking list
    """
    def list_of_bookings(self):
        return self.reservRepo.list_of_bookings()

    """
    This method adds a booking to the list
    input:a given booking
    output:the list with the booking added
    """
    def reservation(self, booking):
        self.reservRepo.reservation(booking)

    """
    This method updates the text file "bookings.txt"
    """
    def storeToFile(self):
        self.reservRepo.storeToFile()


