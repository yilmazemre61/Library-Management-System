class Library:
    def __init__(self, countbook, name):
        self.countbookdict = countbook
        self.name = name
        self.bookdict = {}
        self.maxbookcount = {}
#Displays books and info currently
    def displaybooks(self):
        for books in self.countbookdict.items():
            print(books)
