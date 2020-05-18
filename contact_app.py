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



class Panel:

    def show_menu(self):
        pass

    def start_app(self):
        pass


class Repository:
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