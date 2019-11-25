
import pickle
import os.path
 
 
raw_input = input
SAVE_FILE_NAME = "address_book.pickle"
INSTRUCTIONS = """Welcome

Press:
a to add an entry
d to display a list of all entries in summary form.
i to print these instructions again
q to quit.
"""
CONFIRM_QUIT_MESSAGE = 'Are you sure you want to quit (Y/n)? '
SUMMARY_TEMPLATE = "%s %s DOB: %s email: %s"
 

class AddressBook(object):
   
    def __init__(self):
        
        self.people = []
         
    def add_entry(self, new_entry):
        
        self.people.append(new_entry)
         
    def save(self):
       
        with open(SAVE_FILE_NAME, 'wb') as file_object:
              pickle.dump(self, file_object)
               
               
class AddressEntry(object):

    def __init__(self, first_name=None, family_name=None,
                    email_address=None, date_of_birth=None):
        
        self.first_name = first_name
        self.family_name = family_name
        self.email_address = email_address
        self.date_of_birth = date_of_birth
         
    def __repr__(self):
      
        template = "AddressEntry(first_name='%s', "+\
                      "family_name='%s',"+\
                      " email_address='%s', "+\
                      "date_of_birth='%s')"
        return template%(self.first_name, self.family_name,
                          self.email_address, self.date_of_birth)
                             
                             
class Controller(object):
 
    def __init__(self):

        self.address_book = self.load()
        if self.address_book is None:
            self.address_book = AddressBook()
        self.run_interface()
         
    def load(self):

        if os.path.exists(SAVE_FILE_NAME):
            with open(SAVE_FILE_NAME, 'rb') as file_object:
                address_book = pickle.load(file_object)
            return address_book
        else:
            return None
             
    def run_interface(self):

        print(INSTRUCTIONS)
        while True:
            command = raw_input("Awaiting input ")
            if command == "a":
                self.add_entry()
            elif command == "q":
                if confirm_quit():
                    print("Saving")
                    self.address_book.save()
                    print("Exiting")
                    break
            elif command == "i":
                print(INSTRUCTIONS)
            elif command == "d":
                self.display_summaries()
            else:
                print('Unknown input')
                 
    def add_entry(self):

        print("Adding person")
        print("Input persons:")
        first_name = raw_input("First Name ")
        if first_name == "q":
            print("Not Adding")
            return
        family_name = raw_input("Family Name ")
        if family_name == "q":
            print("Not Adding")
            return
        email_address = raw_input("Email Address ")
        if email_address == "q":
            print("Not Adding")
            return
        DOB_PROMPT = "Date of Birth (Month day, year) "
        date_of_birth = raw_input(DOB_PROMPT)
        if date_of_birth == "q":
            print("Not Adding ")
            return
        entry = AddressEntry(first_name, family_name,
                             email_address, date_of_birth)
        self.address_book.add_entry(entry)
        values = (first_name, family_name)
        print("Added address entry for %s %s\n"%values)
             
    def display_summaries(self):

        print("Displaying Summaries")
        for index, e in enumerate(self.address_book.people):
            values = (e.first_name, e.family_name,
                      e.date_of_birth, e.email_address)
            entry = SUMMARY_TEMPLATE%values
            print("%s: %s"%(index+1, entry))
            
            
def confirm_quit():

    spam = raw_input(CONFIRM_QUIT_MESSAGE)
    if spam == 'n':
        return False
    else:
        return True
         
         
if __name__ == "__main__":
    controller = Controller()
