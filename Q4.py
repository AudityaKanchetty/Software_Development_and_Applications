"""Q4: Library System (Classes and Inheritance)"""

class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"{self.title} by {self.author} ({self.year})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

    def age(self, current_year: int) -> int:
        return current_year - self.year


class EBook(Book):
    def __init__(self, title: str, author: str, year: int, size_mb: float):
        super().__init__(title, author, year)
        self.size_mb = size_mb

    def __str__(self) -> str:
        return f"{self.title} by {self.author} ({self.year}) [{self.size_mb} MB]"

    def download_seconds(self, mbit_per_s: float) -> float:
        return round((self.size_mb * 8) / mbit_per_s, 1)


class Library:
    def __init__(self):
        self.books: list[Book] = []

    def add(self, book: Book):
        if book not in self.books:
            self.books.append(book)

    def find_by_author(self, author: str) -> list[Book]:
        return [b for b in self.books if b.author == author]

    def oldest(self) -> Book | None:
        if not self.books:
            return None
        return min(self.books, key=lambda b: b.year)

    def __len__(self) -> int:
        return len(self.books)


# ============================================================================
# DEMO BLOCK
# ============================================================================
if __name__ == "__main__":
    lib = Library()
    
    b1 = Book("1984", "George Orwell", 1949)
    b2 = Book("Animal Farm", "George Orwell", 1945)
    b3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    
    e1 = EBook("Dune", "Frank Herbert", 1965, 2.5)
    e2 = EBook("Foundation", "Isaac Asimov", 1951, 1.8)

    # Add books
    for book in [b1, b2, b3, e1, e2]:
        lib.add(book)

    # Duplicate add (should be ignored via __eq__)
    lib.add(Book("1984", "George Orwell", 1949))

    # Demonstrate every required method
    print("Total books in library (__len__):", len(lib))
    print("Orwell books (find_by_author):", [str(b) for b in lib.find_by_author("George Orwell")])
    print("Oldest book (oldest):", lib.oldest())
    print("Age of 1984 in 2026 (age):", b1.age(2026))
    print("Download Dune at 10 Mbit/s (download_seconds):", e1.download_seconds(10), "s")
    print("Book string representation (__str__):", b1)
    print("EBook string representation (__str__):", e1)