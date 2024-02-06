from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    price : float

def main():
    books = [
        Book("The Great Gatsby", "F. Scott Fitzgerald", 15.99),
        Book("To Kill a Mockingbird", "Harper Lee", 12.50),
        Book("1984", "George Orwell", 10.75)
    ]
    books.append(Book("The Hunger Games", "Suzanne Collins", 14.25))

    print(books[1])

    expensive_book = max(books, key=lambda p:p.price)
    print(f"The most expensive book is {expensive_book.title}")

    books[0].price += 2
    print(f"Updated price is ${books[0].price:.2f}")

if __name__ == "__main__":
    main()