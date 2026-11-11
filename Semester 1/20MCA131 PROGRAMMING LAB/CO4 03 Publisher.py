# Base Class (Level 1)
class Publisher:
    """Represents the publishing house."""
    def __init__(self, name):
        # Initialize the publisher name
        self.name = name

    def display(self):
        print(f"Publisher: {self.name}")

# Intermediate Child Class (Level 2)
class Book(Publisher):
    """Represents a specific title published by the Publisher."""
    def __init__(self, name, title, author):
        # 1. Base class constructor invocation
        super().__init__(name)
        self.title = title
        self.author = author
    
    # Method Overriding: Overrides Publisher's display
    def display(self):
        # Call the immediate parent's display (Publisher.display)
        super().display()
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

# Final Child Class (Level 3)
class Python(Book):
    """Represents the Python Book instance with specific details."""
    def __init__(self, name, title, author, price, no_of_pages):
        # Call the Book's constructor (which handles the Publisher's constructor implicitly)
        super().__init__(name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages
    
    # Final Method Overriding: Prints all details
    def display(self):
        print("\n--- Python Book Details ---")
        # Call the immediate parent's display (Book.display)
        super().display() 
        print(f"Price: ${self.price:.2f}")
        print(f"Number of Pages: {self.no_of_pages}")


# --- Usage Example ---
book = Python(
    name="CET Publications", 
    title="Introduction to Python", 
    author="G. Ross", 
    price=29.99, 
    no_of_pages=249
)

# 1. Calling the object's display method (runs Python's display, which calls Book's, which calls Publisher's)
book.display() 

# 2. Demonstration: Calling specific parent methods (optional, for viva clarity)
# print("\n--- Demo: Calling Parent Class Methods Directly ---")
# Book.display(book)       # This will print Book and Publisher details
# Publisher.display(book)  # This will print only the Publisher detail