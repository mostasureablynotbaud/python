import pickle
import os.path

SAVE_file_name = 'address_book.pickle'
INSTRUCTIONS = """ Address Book application
Press:
a to add entry
d to diplay list
i to print these inscrtuctions again
q to quit"""

CON_QUIT_MSG = 'Are you sure you want to quit (Y/n)'
SUM_TEMPLATE = '%s %s dob: %s email: %s'
class Address_Book(object):
    def __init__(self):
        self.people = []
    def add_entry(self, new_entry):
        self.people.append(new_entry)
    def save(self):
        with open(SAVE_file_name, 'w') as file_object:
            pickle.dump(self, file_object)
             
class Address_Entry(object):
    
    def __init__(self, first_name=None, family_name=None, email_address=None, dob=None):
        self.first_name = first_name
        self.family_name = family_name
        self.email_address = email_address
        self.dob = dob
    def __repr__(self):
        template = "Address_Entry(first_name'%s',"+\
                   "family_name'%s',"+\
                   "email_address'%s',"+\
                   "dob'%s'"
        return template%(self.first_name, self.family_name, self.email_address, self.dob)
        
class Controller(object):
    def __init__(self):
        if self.address_book is None:
            self.address_book = Address_Book()
        self.address_book = self.load()

        self.run_interface()
    
    def load(self):
        if os.path.exists(SAVE_file_name):
            with open(SAVE_file_name, 'r') as file_object:
                address_book = pickle.load(file_object)
        return address_book
    
    def run_interface(self):
        print(INSTUCTIONS)
        while True:
            command = input('What would you like to do? ')
            if command == 'a':
                self.add_entry
            elif command == 'q':
                if con_quit:
                    print('saving')
                    self.address_book.save()
                    print('Exiting')
                    break
            elif command == 'i':
                print(INSTRUCTIONS)
            elif command == 'd':
                self.display_summaries
            else :
                template = 'Unown command (%s)'
                print(template%command)

    def add_entry(self):
        print('New person')
        first_name = input('First name')
        if first_name == 'q':
            print('Not adding')
            return
        family_name = input('Family name')
        if family_name == 'q':
            print('Not adding')
            return
        email_address = input('Email')
        if email_address == 'q':
            print('Not adding')
            return
        DOB_prompt = 'Date of birth (MM/DD/YYYY)'
        dob = input(DOB_prompt)
        if dob == 'q':
            print('Not adding')
            return
            entry = Address_Entry(first_name, family_name, email_address, dob)
            self.address_book.add_entry(entry)
            values = (first_name, family_name)
            print('Added entry for %s %s\n'%values)

        def display_summaries(self):
            print('Dispaying summaries')
            for index, e in enumerate(self.address_book.people):
                values (e.first_name, e.family_name, e.dob, e.email_address)
                entry = SUM_TEMPLATE%values
                print('%s: %s'%(index+1, entry))

def con_quit():
    spam = input(CON_QUIT_MSG)
    if spam == "n":
        return False
    else:
        return True

if __name__ == '__main__':
    controller = Controller()
