from datetime import date, timedelta


class User:

    def __init__(self, username, password, user, address, mobile):
        self.username = username
        self.password = password
        self.user = user
        self.address = address
        self.mobile = mobile


class Member(User):
    def __init__(self, username, password, user, memberid, address, mobile):
        super().__init__(username, password, user, address, mobile)
        self.memberid = memberid
        self.maxbookcount = {}
        self.bookdict = {}

    def countbook(self, user, book):
        if user not in self.maxbookcount:
            self.maxbookcount[user] = [book]
            return len(self.maxbookcount[user])
        else:
            if len(self.maxbookcount[user]) <= 3:
                self.maxbookcount[user].apend(book)
                return len(self.maxbookcount[user])
            else:
                return len(self.maxbookcount[user])
#The member can only rent 3 books. Also they cannot rent same book more than one.
#If the quantity of book is 0 they cannot rent book
    def lendbook(self, library, book, user):
        if book in library.countbookdict.keys():
            if library.countbookdict[book][0] >= 1:
                if (book, user) not in self.bookdict.keys():
                    if self.countbook(user, book) <= 3:
                        lend_date = date.today()
                        return_date = date.today() + timedelta(days=14)
                        self.bookdict.update({(book, user): return_date})
                        library.countbookdict[book][0] -= 1
                        for value in self.bookdict.keys():
                            if value == (book, user):
                                print("'{}' was rented by '{}' on '{}'.\n"
                                  "You have 2 weeks to return the book.\n"
                                  "Please return the book in time otherwise you will be charged 1€ per day".format(value[0], value[1], lend_date))
                                print(self.maxbookcount)
                    else:
                        print("You can rent maximum 3 books.")
                else:
                    print("You already rented this book.\n"
                      "You are not allowed to rent same book more than one.")
            else:
                print("The book you have been looking is currently not available in our library.")
        else:
            print("Sorry. We do not have this book in our Library.")
#The member must retun the book in 2 weeks otherwise they will be chanrged 1€ per day.
#If you want to test it you have to change 'current_date' more than 2 week later from today.
    def checkpreviousfine(self, book, user):
        current_date = date.today()
        for key,value in self.bookdict.items():
            if key[1] == user:
                return_date = self.bookdict[key]
                if current_date > return_date:
                    delay_days = (current_date - return_date).days
                    total_fine = delay_days * 1
                    return total_fine
                else:
                    return 0

    def returnbook(self, library, book, user):
        if (book, user) in self.bookdict.keys():
            return_date = self.bookdict[(book, user)]
            current_date = date.today()
            if current_date > return_date:
                delay_days = (current_date - return_date).days
                total_fine = delay_days * 1
                print("You must pay {}€ fine for returning the book {} days later.".format(total_fine, delay_days))
                self.payment(library, book, user)
            else:
                self.maxbookcount[user].remove(book)
                self.bookdict.pop((book, user))
                library.countbookdict[book][0] += 1
                print("The book successfully returned.")
        else:
            print("Please check your input again.")

    def payment(self,library, book, user):
        print("Please enter your process.")
        choice = input("Yes / No : ")
        if choice == "Yes":
            print("Payment Successfully Processed")
            self.maxbookcount[user].remove(book)
            self.bookdict.pop((book, user))
            library.countbookdict[book][0] += 1
        else:
            print("You are being redirected to the homepage.")

    def checkfine(self, library, book, user):
        if (book, user) in self.bookdict.keys():
            return_date = self.bookdict[(book, user)]
            current_date = date.today()
            if current_date > return_date:
                delay_days = (current_date - return_date).days
                total_fine = delay_days * 1
                print("You must pay {}€ fine for returning the book {} days later.".format(total_fine, delay_days))
                print("Do you want to pay the fine now?")
                choice = input("Yes / No : ")
                if choice == "Yes":
                    self.payment(library, book, user)
                else:
                    print("You are being redirected to the homepage.")
            else:
                print("You do not have fine.")
        else:
            print("Please check your input again.")


