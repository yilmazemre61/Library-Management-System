from User import User


class Librarian(User):
    def __init__(self, username, password, name, mobile, address, librarianid, startingdate):
        super().__init__(username, password, name, mobile, address)
        self.librarianid = librarianid
        self.startingdate = startingdate
#To add a new book in the Library
    def addingbooks(self, library, bookname, quantity, author, title, isbn):
        if quantity > 0:
            if bookname in library.countbookdict.keys():
                library.countbookdict[bookname][0] += quantity
            else:
                library.countbookdict.update({bookname: [quantity, author, title, isbn]})
                print("The '{}' has been added to Library".format(bookname))
        else:
            print("Please Enter Positive Integer Number")
#We can  reduce the quantitiy of book.
#If the quantity is 0 the book will remain in the Library and If someone asks the book system will desplay a message
    def removebooks(self, library, bookname, quantity):
        if quantity > 0:
            if bookname in library.countbookdict.keys():
                if library.countbookdict[bookname][0] >= 1:
                    library.countbookdict[bookname][0] -= quantity
                    if library.countbookdict[bookname][0] < 0:
                        library.countbookdict[bookname][0] += quantity
                        print("Please Enter correct quantity number. We have only {} books of '{}'.".format(library.countbookdict[bookname][0], bookname))
                    else:
                        print("Book is removed from the Library.")
                else:
                    library.countbookdict.pop(bookname)
                    print("Sorry!! We do not have a book named '{}' in our Library.".format(bookname))
            else:
                print("Please Enter correct name or quantity.")
        else:
            print("Please Enter Positive Integer Number")
