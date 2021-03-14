from guest import *

class GuestRepo:

    def __init__(self):
        self.guests = []

    # Aceasta functie va adauga persoana în spatiul de stocare local.
    def add_guest(self, guest):
        if guest not in guests:
            guests.append(guest)
            print('The guest {0} {1} has been successfully added.'.format(guest['first_name'], guest['last_name']))
        else:
            print('There is already a guest with the id {0}'.format(guest['id']))

    # Aceasta functie schimba numele unei persoane
    def edit_last_name(self, guest):
        if guest is None:
            print('Unsuccessfully update!')
        else:
            print('Editing guest {0} {1}.'.format(guest['first_name'], guest['last_name']))
            last_name = input('Enter new last name: ')
            guest['last_name'] = last_name.title()
            print('Successfully updated last name of the user!')


    # Aceasta functie cauta in lista persoana care are ca id unic id-ul dat
    def find_guest_by_id(self, guest_id):
        for guest in guests:
            if guest['id'] == guest_id:
                return guest
        print('There is no guest with the id: {0}.'.format(guest_id))
        return None


    # Aceasta functie va sterge din lista persoana care contine id-ul primit daca acesta exista,
    # altfel imprima ca a fost o stergere nereusita.
    def delete_guest_by_id(self, guest_id):
        guest = self.find_guest_by_id(guest_id)
        if guest is None:
            print('Unsuccessful delete!')
        else:
            guests.remove(guest)
            print('Successfully deleted guest: {0} {1}.'.format(guest['first_name'], guest['last_name']))


    # Aceasta functie va tipari id-ul si numele complet al tuturor persoanelor din lista.
    def print_guests(self, l):
        for guest in l:
            print('ID: {0}, Name: {1} {2}'.format(guest['id'], guest['first_name'], guest['last_name']))
