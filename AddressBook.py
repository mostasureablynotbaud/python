import pickle
import os.path


SAVE_FILENAME = 'address book.pickle'
INSRUCTIONS = """Welcome
Press:
a to add entry
d to display existing entries
i to print these instructions again
q to quit """

CON_QUITmsg = 'Are you  sure Y/n'
SUM_TEMPLATE = "%s %s DOB: %s email: %s"


class Addressbook(object):
    def __init__(self):
        self.people = []

    def add_entry(self, new_entry):
        self.people.append(new_entry)

    def save(self):
        with open(SAVE_FILENAME, 'w') as file_object:
            pickle.dump(self, file_object)

class Addressentry(object):
    def __init__(self):
        self.first = first_name
        self.family = family_name
        self.email = email
        self.dob = dob

    def __repr__(self):
        template = "Addressentry(first_name='%s', "+\
            " family_name='%s' ,"+\
            " email='%s' "+\
            ", dob='%s')"
        return template%(self.first, self.family, self.email, self.dob)

class Controller(object):
    def __init__(self):
        self.addressbook = self.load()
        if self.addressbook is None:
            self.addressbook = Addressbook()
        self.runinterface()

        def load(self):
            if os.path.exists(SAVE_FILENAME):
                with open(SAVE_FILENAME, 'r') as file_object:
                    addressbook = pickle.load(file_object)
                    return addressbook
            else:
                return None
        def runinterface(self):
            print(INSRUCTIONS):
            while True:
                command = input('Awaiting input')
                if command == 'a':
                    self.addentry()
                elif command == 'q':
                    if conquit():
                        print('Saving')

