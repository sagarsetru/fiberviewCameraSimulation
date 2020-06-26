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
    
    
    
    def print_contacts(self,sorted_order=False):
        """
        Print each of the contacts stored in this address book.
        If sorted is True, print them in sorted order by name.
        """
       
        def returnSortKey(contact):
            if contact.name != "":
                return contact.name
            elif contact.email != "":
                return contact.email
            elif contact.phone_number != "":
                return contact.phone_number
            elif contact.address != "":
                return contact.address
            else:
                return ""
        if sorted_order == True:
            output = sorted(self.contact_list,key=lambda z: returnSortKey(z))
        else:
            output = self.contact_list
        
        for x in output:
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
            print "Email:", self.email
        
        # if self.name == "" and self.phone_number == "" and self.address == "" and self.email == "":
            # print ""
        # elif self.name == "" and self.phone_number == "" and self.address == "":
            # print "Email:", self.email
        # elif self.phone_number == "" and self.address == "":
            # print "Name:", self.name
            # print "Email:", self.email
        # elif self.address == "":
            # print "Name:", self.name
            # print "Phone Number:", self.phone_number
            # print "Email:", self.email
        # elif self.email == "":
            # print "Name:", self.name
            # print "Phone Number:", self.phone_number
            # print "Address:", self.address
        # else:
            # print "Name:", self.name
            # print "Phone Number:", self.phone_number
            # print "Address:", self.address
            # print "Email:", self.email
    #...
 #...

newcontact2 = Contact(name="Sagar", email="sagar@yale.edu")
newcontact = Contact("John","123-4567","somehwere, USA","bill@microsoft.com")
newcontact3 = Contact(email="zanonymous@whoami.com")
newcontact4 = Contact(address="Over there, USA")
newcontact5 = Contact("Anthony","324-9842","New Haven, CT","friend@awesome.com")
newcontact6 = Contact("Bob","458-0983","New York, NY","who@what.com")
newbook = AddressBook([newcontact,newcontact2,newcontact6,newcontact3,newcontact4,newcontact5])
newbook.print_contacts(sorted_order=True)
