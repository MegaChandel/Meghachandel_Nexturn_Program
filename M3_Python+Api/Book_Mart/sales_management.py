from book_management import books

sales = [
    {"customer_name": "Ramesh Kumar", "book_title": "Python 101", "quantity_sold": 2},
    {"customer_name": "Shivam", "book_title": "The Art of Programming", "quantity_sold": 1},
]

def sell_book(customer_name, book_title, quantity_sold):
    for book in books:
        if book["title"].lower() == book_title.lower():
            if book["quantity"] >= quantity_sold:
                book["quantity"] -= quantity_sold
                sale = {"customer_name": customer_name, "book_title": book_title, "quantity_sold": quantity_sold}
                sales.append(sale)
                return f"Sale successful! Remaining quantity: {book['quantity']}"
            else:
                return f"Error: Only {book['quantity']} copies available. Sale cannot be completed."
    return "Book not found."

def view_sales():
    if not sales:
        return "No sales records."
    return sales
