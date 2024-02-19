class Library:
    def __init__(self, filename='books.txt'):
        # Opens the 'books.txt' file with using 'a+' method
        self.filename = filename
        self.file = open(self.filename, 'a+')

    def __del__(self):
        # Closes the file when the object is deleted
        self.file.close()

    def list_books(self):
        #list_books provides information about books in the library
        self.file.seek(0)
        books = self.file.read().splitlines()
        if books:
            print("Book list for library:")
            for book in books:
                title, author, release_date, num_pages = book.split(',')
                print(f"Title: {title}, Author: {author}, Release Date: {release_date}, Pages: {num_pages}")
        else:
            print("There is any book in the library")

    def add_book(self):
        # add_book allows the user to add a new book to the library
        title = input("Please enter the book title: ")
        author = input("Please enter the book author: ")
        release_date = input("Please enter the release date: ")
        num_pages = input("Please enter the number of pages: ")

        book_info = f"{title},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print(f"New book added: {title}")

    def remove_book(self):
        # remove_book provides the user to remove a book from the library
        title_to_remove = input("Please enter the title of the book to remove: ")
        books = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()

        found = False
        for book in books:
            if title_to_remove not in book:
                self.file.write(book)
            else:
                found = True

        if found:
            print(f"Book removed: {title_to_remove}")
        else:
            print(f"Book not found: {title_to_remove}")

#This is object name which call "lib" with "Library" class
lib = Library()

#This is menu for user
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Please enter your choice (1-4): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
