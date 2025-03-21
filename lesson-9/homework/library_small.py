class Book:
    def __init__(self, title, author, is_borrowed: bool):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    
    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Is it borrowed: {self.is_borrowed}'

class BookNotFoundException(Exception):
    def __init__(self, title):
        self.title = title
    
    def __str__(self):
        return f'The book named {self.title} was not found!'

class BookAlreadyBorrowedException(Exception):
    def __init__(self, title):
        self.name = title
    
    def __str__(self):
        return f'The book named {self.name} was already borrowed!'

class MemberLimitExceededException(Exception):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'You already borrowed three books. No more allowed!'

class Member:
    def __init__(self, name, borrowed_books: int = 0):
        self.name = name
        self.borrowed_books = borrowed_books

    def __str__(self):
        return f'Member: {self.name}, Number of books borrowed so far: {self.borrowed_books}'

class Library:
    books = []
    members = []
    borrowed_books = []
    
    @staticmethod
    def add_book(title, author, is_borrowed):
        book = Book(title, author, is_borrowed.lower() == 'true')
        Library.books.append(book)
    
    @staticmethod
    def add_member(name):
        Library.members.append(Member(name))
    
    @staticmethod
    def borrow(title):
        try:
            all_titles = [book.title for book in Library.books]
            all_bor = [book.title for book in Library.borrowed_books]
            
            if title not in all_titles and title not in all_bor:
                raise BookNotFoundException(title)
            elif title in all_bor:
                raise BookAlreadyBorrowedException(title)
                
            name = input("Enter your name: ")
            for member in Library.members:
                if member.name == name:
                    if member.borrowed_books < 3:
                        print("The book is found! Here you go!")
                        book_index = all_titles.index(title)
                        Library.borrowed_books.append(Library.books[book_index])
                        del Library.books[book_index]
                        member.borrowed_books += 1
                        return
                    else:
                        raise MemberLimitExceededException(name)
            print("Member not found. Please register first.")
        except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
            print(e)
    
    @staticmethod
    def return_book(name, title):
        member = next((m for m in Library.members if m.name == name), None)
        if member:
            book = next((b for b in Library.borrowed_books if b.title == title), None)
            if book:
                Library.books.append(book)
                Library.borrowed_books.remove(book)
                member.borrowed_books -= 1
                print("Successfully returned!")
            else:
                print("Wrong title!")
        else:
            print("Member Not Found!")

    @staticmethod
    def run():
        while True:
            try:
                s = int(input("Choose what you want to do:\n1. Add a book\n2. Add a member\n3. Borrow a book\n4. Return a book\n5. Exit the library\n"))
                if s == 1:
                    a, b, c = input("Enter in the following format: title, author, is_borrowed (True or False): ").split(", ")
                    Library.add_book(a, b, c)
                elif s == 2:
                    a = input("Enter your name: ")
                    Library.add_member(a)
                elif s == 3:
                    title = input("Enter the title of the book: ")
                    Library.borrow(title)
                elif s == 4:
                    name, title = input("Enter your name and the title of the book in the following format: Name, Title: ").split(", ")
                    Library.return_book(name, title)
                elif s == 5:
                    print("Exiting the program. Thank you...")
                    break
                else:
                    print("Invalid number!")
            except ValueError:
                print("Invalid input! Please enter a number.")

Library.run()
