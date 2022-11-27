# Implement a student library system using Oops where students can borrow a book from the list of books crate a separate library and student class. Your program must be menu driven. You are free to choose methods and attributes of your choice to implement this functionality
class Library():
    def __init__(self,listbooks):
        self.books = listbooks

    def DisplayAvailableBooks(self):
        print("The books Availabe in this library are: ")
        for book in self.books:
            print("\t *",book)
    
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued this {bookName} book. Please keep it safe and return it within 30 days from now")
            self.books.remove(bookName)
        else:
            print(f"Sorry, {bookName} book is not available or someone else taken this book. Please wait some time until this book is available!")

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this book. Hope you enjoyed reading it. Have a great day ahead!")

class Student():
    def requestBook(self):
        self.reqbook = input("Enter the book you want to borrow: ")
        return f"This {self.reqbook} will available immediately! Thanks for giving the suggestion"

if __name__ == "__main__":
    CentralLibrary = Library(["Python", "Object Oriented programming", "Algorithm", "Chsl preparation", "Matric Topper Notes","Django"])
    while(True):
        print('''======= Welcome in this Central Library =======
        Please choose an option given below:-
        Press 1: To display books in library
        Press 2: For Borrow Book
        press 3: For Return Book
        Press 4: For exit this library''')
        b = int(input("Enter your choice from 1 to 4 : "))
        if b == 1:
            CentralLibrary.DisplayAvailableBooks()
        elif b == 2:
            c = input("Enter the book you want to borrow: ")
            CentralLibrary.borrowBook(c) 
        elif b ==3:
            d = input("Enter the book you want to return: ")
            CentralLibrary.returnBook(d)
        elif b==4:
            print("Thanks for choosing Central Library! Have a great day.")
            exit()
        else:
            print("Invalid Choice!")