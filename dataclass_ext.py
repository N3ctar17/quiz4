from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    price : float

    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nPrice: ${self.price:.2f}")
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

    print("Book 1:")
    books[0].display_info()

    print("\nBook 2:")
    books[1].display_info()

    print("\nBook 3:")
    books[2].display_info()

    print("\nBook 4:")
    books[3].display_info()
    
if __name__ == "__main__":
    main()