books = [
    {"title": "Python 101", "author": "John Doe", "price": 500, "quantity": 10},
    {"title": "The Art of Programming", "author": "Donald Knuth", "price": 1200, "quantity": 5},
    {"title": "Learn Python the Hard Way", "author": "Zed Shaw", "price": 700, "quantity": 7},
]

def add_book(title, author, price, quantity):
    book = {"title": title, "author": author, "price": price, "quantity": quantity}
    books.append(book)
    return "Book added successfully!"

def view_books():
    if not books:
        return "No books available."
    return books

def search_book(keyword):
    result = [book for book in books if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower()]
    if not result:
        return "Book not found."
    return result

