def display_menu():
    print("\n===== Library Management Menu =====")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Remove Book")
    print("6. Search Book")
    print("7. Exit")

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    with open("books.txt", "a") as f:
        f.write(f"{book_id},{title},{author},Available\n")
    print("Book added successfully!")

def display_books():
    try:
        with open("books.txt", "r") as f:
            print("\nBookID | Title | Author | Status")
            for line in f:
                print(" | ".join(line.strip().split(",")))
    except FileNotFoundError:
        print("No books found.")

def borrow_book():
    book_id = input("Enter Book ID to borrow: ")
    found = False
    updated_lines = []
    with open("books.txt", "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == book_id and parts[3] == "Available":
                parts[3] = "Borrowed"
                found = True
            updated_lines.append(",".join(parts))
    
    with open("books.txt", "w") as f:
        for line in updated_lines:
            f.write(line + "\n")
    
    if found:
        print("Book borrowed successfully!")
    else:
        print("Book not found or already borrowed.")

def return_book():
    book_id = input("Enter Book ID to return: ")
    found = False
    updated_lines = []
    with open("books.txt", "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == book_id and parts[3] == "Borrowed":
                parts[3] = "Available"
                found = True
            updated_lines.append(",".join(parts))

    with open("books.txt", "w") as f:
        for line in updated_lines:
            f.write(line + "\n")
    
    if found:
        print("Book returned successfully!")
    else:
        print("Book not found or already available.")

def remove_book():
    book_id = input("Enter Book ID to remove: ")
    removed = False
    with open("books.txt", "r") as f:
        lines = f.readlines()
    
    with open("books.txt", "w") as f:
        for line in lines:
            if line.split(",")[0] != book_id:
                f.write(line)
            else:
                removed = True

    if removed:
        print("Book removed.")
    else:
        print("Book not found.")

def search_book():
    keyword = input("Enter keyword to search (Title or Author): ").lower()
    with open("books.txt", "r") as f:
        print("\nSearch Results:")
        found = False
        for line in f:
            if keyword in line.lower():
                print(" | ".join(line.strip().split(",")))
                found = True
        if not found:
            print("No matching books found.")

# Main program
while True:
    display_menu()
    choice = input("Enter choice (1-7): ")
    
    if choice == '1':
        add_book()
    elif choice == '2':
        display_books()
    elif choice == '3':
        borrow_book()
    elif choice == '4':
        return_book()
    elif choice == '5':
        remove_book()
    elif choice == '6':
        search_book()
    elif choice == '7':
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
