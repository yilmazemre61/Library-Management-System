import sys
from Library import Library
from User import Member
from Search import Search
from Librarian import Librarian

library = Library({"Gone Girl": [6, "Gillian Flynn", "Thriller", 1000000000001],
                   "Nineteen EightyFour": [7, "George Orwell", "Fiction", 1000000000002],
                   "The Lord of The Rings": [12, "J.R.R. Tolkien", "Fantasy", 1000000000003],
                   "Born a Crime": [9, "Trevor Noah", "Autobiography", 1000000000004],
                   "In Cold Blood": [7, "Truman Capote", "Crime", 1000000000005]}, "Python Library")
m1 = Member("@member123", "member123", "member1", "member12345", "535 Howth Road", "05322347865")
Search = Search()
while True:
    print("Welcome to the {}".format(library.name))
    print("Please Enter the Number You Want to Process")
    print("1", "Display Books in Library")
    print("2", "Rent a Book")
    print("3", "Return a Book")
    print("4", "Pay the Fine")
    print("5", "Search a Book")
    print("6", "Add a Book")
    print("7", "Remove a Book")

    processnumber = input()
    if processnumber not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Please Enter a Valid Process Number!")
        continue
    else:
        processnumber = int(processnumber)
        if processnumber == 1:
            print("The Books in Library")
            library.displaybooks()
        elif processnumber == 2:
            book = input("Please Enter the Name of Book : ")
            user = input("Please Enter Your Name : ")
            m1.lendbook(library, book, user)
        elif processnumber == 3:
            book = input("Please Enter The Name of Book : ")
            user = input("Please Enter Your Name : ")
            m1.returnbook(library, book, user)
        elif processnumber == 4:
            book = input("Please Entre the Name of Book : ")
            user = input("Please Enter Your Name : ")
            m1.checkfine(library, book, user)
        elif processnumber == 5:
            bookname = input("Enter the Name of Book : ")
            Search.searchbook(library, bookname)
        elif processnumber == 6:
# The 'username' for librarian is 'emre' and 'password' is '12345'
            username = input("username: ")
            password = input("password: ")
            if username == "emre" and password == "12345":
                librarian_ = Librarian(username, password, "Librarian1", "05384263912", "Maywood Lawn", "123456",
                                   "01/01/2019")
                print("Adding Books")
                bookname = input("Please Enter the Book of Name You Want to Add : ")
                quantity = int(input("Please Enter the Quantity of Book : "))
                author = input("Please Enter the Name of Author : ")
                title = input("Please Enter the Title of Book : ")
                isbn = int(input("Please Enter the ISBN Number of Book :  "))
                librarian_.addingbooks(library, bookname, quantity, author, title, isbn)
            else:
                print("Please Enter Correct Input !!")
        elif processnumber == 7:
            username = input("username: ")
            password = input("password: ")
            if username == "emre" and password == "12345":
                librarian_ = Librarian(username, password, "Librarian1", "05384263912", "Maywood Lawn", "123456",
                                   "01/01/2019")
                print("Remove Books")
                bookname = input("Please Enter the Name of Book You Want to Remove : ")
                quantity = int(input("Please Enter the Quantity of Book : "))
                librarian_.removebooks(library, bookname, quantity)
            else:
                print("Please Enter Correct Input !!")
        else:
            print("Not a Valid Process Number")

        print("Please Choose 'q' to QUIT or 'c' to CONTINUE")
        choice = ""
        while choice != "q" and choice != "c":
            choice = input()
            if choice == "c":
                continue
            elif choice == "q":
                sys.exit()
