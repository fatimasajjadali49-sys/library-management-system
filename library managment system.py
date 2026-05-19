import csv
import os

books_file = "books.csv"
issued_file = "issued_books.csv"


# Create files if not exist
def create_files():
    if not os.path.exists(books_file):
        with open(books_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Book ID", "Book Name", "Author", "Quantity"])

    if not os.path.exists(issued_file):
        with open(issued_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Student Name", "Book ID", "Book Name"])


# Add Book
def add_book():
    print("\n--- Add New Book ---")

    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    try:
        quantity = int(input("Enter Quantity Available: "))
    except:
        print("Invalid quantity! Please enter a number.\n")
        return

    with open(books_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([book_id, book_name, author, quantity])

    print("Book added successfully!\n")


# Display Books
def display_books():
    print("\n--- Available Books ---")

    with open(books_file, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

    print()


# Issue Book
def issue_book():
    print("\n--- Issue Book ---")

    student_name = input("Enter Student Name: ")
    book_id = input("Enter Book ID to Issue: ")

    books = []
    found = False

    with open(books_file, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0] == book_id:
                if int(row[3]) > 0:
                    row[3] = str(int(row[3]) - 1)
                    found = True

                    with open(issued_file, "a", newline="") as issue:
                        writer = csv.writer(issue)
                        writer.writerow([student_name, book_id, row[1]])
            else:
                    print("Book is currently out of stock!\n")

            books.append(row)

    if found:
        with open(books_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Book ID", "Book Name", "Author", "Quantity"])
            writer.writerows(books)

        print("Book issued successfully!\n")
    else:
        print("Invalid Book ID or book not available!\n")


# Return Book
def return_book():
    print("\n--- Return Book ---")

    book_id = input("Enter Book ID to Return: ")

    books = []
    found = False

    with open(books_file, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0] == book_id:
                row[3] = str(int(row[3]) + 1)
                found = True

            books.append(row)

    if found:
        with open(books_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Book ID", "Book Name", "Author", "Quantity"])
            writer.writerows(books)

        print("Book returned successfully!\n")
    else:
        print("Invalid Book ID!\n")


# Search Book
def search_book():
    print("\n--- Search Book ---")

    search = input("Enter Book Name or Author Name: ").lower()
    found = False

    with open(books_file, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if search in row[1].lower() or search in row[2].lower():
                print(row)
                found = True

    if not found:
        print("Book not found!")

    print()


# Display Report
def display_report():
    print("\n--- Library Report ---")

    total_books = 0
    available_books = 0
    issued_books = 0

    with open(books_file, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            total_books += 1
            available_books += int(row[3])

    with open(issued_file, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            issued_books += 1

    print("Total Different Books :", total_books)
    print("Total Issued Books    :", issued_books)
    print("Available Books       :", available_books)
    print()


# Menu
def menu():
    create_files()

    while True:
        print("===================================")
        print("   Library Management System")
        print("===================================")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Display Report")
        print("7. Exit")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            search_book()
        elif choice == "6":
            display_report()
        elif choice == "7":
            print("Program exited successfully!")
            break
        else:
            print("Invalid choice! Please try again.\n")


# Run Program
menu()
