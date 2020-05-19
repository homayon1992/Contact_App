class Contact:
    conter = 1
    def __init__(self, name, lastname, phone, email, address):
        self._id = Contact.conter
        Contact.conter += 1
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return "name: {}\nlastname: {}\nphone: {}\nemail: {}\naddress: {}" \
            .format(self.name, self.lastname, self.phone, self.email, self.address)


class Panel:

    def __init__(self):
        self.repo = ListRepository()

    def add_new_contact(self):
        name = input("Enter Name... ")
        lastname = input("Enter LastName... ")
        phone = input("Enter Phone... ")
        email = input("Enter E-mail... ")
        address = input("Enter Address... ")
        contact = Contact(name, lastname, phone, email, address)
        self.repo.save(contact)

    def show_all_contact(self):
        contacts = self.repo.find_all()
        for contact in contacts:
            print(contact)
            print("="*30)

    def search_contact(self):
        name = input("Enter Name... ")
        contacts = self.repo.serch_by_name(name)
        for contact in contacts:
            print(contact)
            print("="*30)


    def delete_contact(self):
        name = input("Enter Name... ")
        contacts = self.repo.serch_by_name(name)
        for contact in contacts:
            print(contact)
            print("=" * 30)
            choice = input("Do You Want To Delete Contact? [Y/N]... ")
            if choice == 'Y' or choice == 'y' :
                self.repo.delete(contact._id)
                break

    def update_contact(self):
        name = input("Enter Name... ")
        contacts = self.repo.serch_by_name(name)
        for contact in contacts:
            print(contact)
            print("=" * 30)
            choice = input("Do You Want To Update Contact? [Y/N]... ")
            if choice == 'Y' or choice == 'y':
                name = input("Enter Name... ")
                lastname = input("Enter LastName... ")
                phone = input("Enter Phone... ")
                email = input("Enter E-mail... ")
                address = input("Enter Address... ")
                name = contact.name if name == '' else name
                lastname = contact.lastname if lastname == '' else lastname
                phone = contact.phone if phone == '' else phone
                email = contact.email if email == '' else email
                address = contact.address if address == '' else address
                new_contact = Contact(name, lastname, phone, email, address)
                new_contact._id = contact._id
                self.repo.update(new_contact)

    def show_menu(self):
        print("1-Add New Contact")
        print("2-Show All Contact")
        print("3-Search Contact By Name")
        print("4-Delete Contact")
        print("5-Update Contact")
        print("6-Exit")


    def start_app(self):
        while True:
            self.show_menu()
            option = int(input("What Should I Do? [Number]... "))
            if option == 1:
                self.add_new_contact()
            elif option == 2:
                self.show_all_contact()
            elif option == 3:
                self.search_contact()
            elif option == 4:
                self.delete_contact()
            elif option == 5:
                self.update_contact()
            elif option == 6:
                exit(0)
            else:
                print("Please Enter a Number")



class ListRepository:
    def __init__(self):
        self.repositori = {}

    def save(self, contact):
        self.repositori[contact._id] = contact

    def delete(self, _id):
        del self.repositori[_id]

    def serch_by_name(self, name):
        l = []
        for contact in self.repositori.values():
            if contact.name == name:
                l.append(contact)
        return l

    def find_all(self):
        return self.repositori.values()

    def update(self, contact):
        self.save(contact)




App = Panel()
App.start_app()