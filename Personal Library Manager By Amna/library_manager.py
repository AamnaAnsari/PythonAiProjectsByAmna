# Personal Library Manager using Python and JSON

import json

# Load data from JSON file
def load_books():
    try:
        with open("books.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save data to JSON file
def save_books(books):
    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)

# Add a new book
def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    genre = input("Enter book genre: ").strip()
    year = input("Enter publication year: ").strip()

    books.append({
        "title": title,
        "author": author,
        "genre": genre,
        "year": year
    })

    save_books(books)
    print("✅ Book added successfully!\n")

# View all books
def view_books():
    if not books:
        print("📚 No books found!\n")
    else:
        for idx, book in enumerate(books, start=1):
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}, {book['genre']})")
        print()


def search_books():
    query = input("Enter title or author to search: ").strip().lower()
    results = [book for book in books if query in book['title'].lower() or query in book['author'].lower()]

    if results:
        for idx, book in enumerate(results, start=1):
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}, {book['genre']})")
    else:
        print("❌ No matching books found.\n")

# Update a book
def update_book():
    view_books()
    try:
        choice = int(input("Enter the number of the book to update: ")) - 1
        if 0 <= choice < len(books):
            print("Leave blank to keep current value.")
            books[choice]['title'] = input(f"New title ({books[choice]['title']}): ").strip() or books[choice]['title']
            books[choice]['author'] = input(f"New author ({books[choice]['author']}): ").strip() or books[choice]['author']
            books[choice]['genre'] = input(f"New genre ({books[choice]['genre']}): ").strip() or books[choice]['genre']
            books[choice]['year'] = input(f"New year ({books[choice]['year']}): ").strip() or books[choice]['year']

            save_books(books)
            print("✅ Book updated successfully!\n")
        else:
            print("❌ Invalid choice.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

# Delete a book
def delete_book():
    view_books()
    try:
        choice = int(input("Enter the number of the book to delete: ")) - 1
        if 0 <= choice < len(books):
            deleted_book = books.pop(choice)
            save_books(books)
            print(f"✅ Deleted: {deleted_book['title']} by {deleted_book['author']}\n")
        else:
            print("❌ Invalid choice.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")


def main():
    global books
    books = load_books()

    while True:
        print("\n📚 Personal Library Manager")
        print("1. Add a Book")
        print("2. View All Books")
        print("3. Search for a Book")
        print("4. Update a Book")
        print("5. Delete a Book")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_books()
        elif choice == '4':
            update_book()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            print("👋 Exiting the Library Manager. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main()
