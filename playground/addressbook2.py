"""
Class to represent an address book with multiple contacts.
"""

class AddressBook:
    """This will provide you with contact information about your friends."""

    def __init__(self,contacts=[]):
        self.contact_list = contacts
    #...

    def addentry(self,name,phone_number,address,email):
        newcontact = Contact(name,phone_number,address,email)
        self.contact_list.append(newcontact)
    #...
    
    def print_contacts(self,sorted=False):
        """
        Print each of the contacts stored in this address book.
        If sorted is True, print them in sorted order by name.
        """
        for x in self.contact_list:
            print "_____________"
            x.print_entry()
    #...
#...

class Contact:
    """
    Class to store contact information for a single person.
    """

    def __init__(self,name="",phone_number="",address="",email=""):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
    #...

    def print_entry(self):
        """
        Pretty-print the entries in this contact.
        Empty values are not printed.
        """
        if self.name != "":
            print "Name:", self.name
        if self.phone_number != "":
            print "Phone Number:", self.phone_number
        if self.address != "":
            print "Address:", self.address
        if self.email != "":
            print "Email:" self.email
        print "Name:", self.name
        print "Phone Number:", self.phone_number
        print "Address:", self.address
        print "Email:", self.email
    #...
 #...
