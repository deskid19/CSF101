     # Initialize empty listd, set, and dictionary
books_list =[]
authors_sets = set()
books_dict = {}

# Add books
books_list.append("Python Programming")
authors_sets.add("John Smith")
books_dict["Python Programming"] = "John Smith"

books_list.append("Data Structures and Algorithms")
authors_sets.add("Jane Doe")
books_dict["Data Structures and Algorithms"] = "Jane Doe"

books_list.append("Machine Learning Basics")
authors_sets.add("Alice Johnson")
books_dict["Machine Learning Basics"] = "Alice Johnson"

# Search for a book
search_title = input("Enter the title of the book to search: ")
if search_title in books_list:
    print(f"Book found! Author: {books_dict[search_title]}")
else:
    print("Book not found")

# Display all books
print("List of Books:")
for book in books_list:
    print(book)

# Remove a book
remove_title = input("Enter the title of the book to remove or else enter to skip: ")
if remove_title in books_list:
    remove_author = books_dict[remove_title]
    books_list.remove(remove_title)
    authors_sets.remove(remove_author)
    del books_dict[remove_title]
    print("Book removed successfully!")
    print("Books available: ", books_list)

else:
    print("Book not found!")