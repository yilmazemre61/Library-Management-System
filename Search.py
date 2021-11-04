import sys


class Search:

    def searchbook(self, library, bookname):
        for key, value in library.countbookdict.items():
            if bookname in library.countbookdict.keys():
                print("Book Name: {} \n"
                      "Information: {}".format(bookname, library.countbookdict[bookname]))
                print("Do you want to rent this book?")
                choice = input("Yes / No : ")
                if choice == "Yes":
                    break
                else:
                    print("You are exiting from system.")
                    sys.exit()
            else:
                print(
                    "The Book You Have Been Looking Is Not Currently Available In Our Library or Please Check Your Book Name Again.")
                break
