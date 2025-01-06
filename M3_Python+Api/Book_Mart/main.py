from book_management import add_book, view_books, search_book
from customer_management import add_customer, view_customers
from sales_management import sell_book, view_sales

def main_menu():
    while True:
        print("\nWelcome to BookMart!")
        print("1. Book Management")
        print("2. Customer Management")
        print("3. Sales Management")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nBook Management")
            print("1. Add Book")
            print("2. View Books")
            print("3. Search Book")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                title = input("Title: ")
                author = input("Author: ")
                price = int(input("Price: "))
                quantity = int(input("Quantity: "))
                if price > 0 and quantity > 0:
                    print(add_book(title, author, price, quantity))
                else:
                    print("Invalid input! Price and quantity must be positive.")
            elif sub_choice == "2":
                books = view_books()
                if isinstance(books, str):
                    print(books)
                else:
                    for book in books:
                        print(book)
            elif sub_choice == "3":
                keyword = input("Enter title or author: ")
                results = search_book(keyword)
                if isinstance(results, str):
                    print(results)
                else:
                    for book in results:
                        print(book)
        elif choice == "2":
            print("\nCustomer Management")
            print("1. Add Customer")
            print("2. View Customers")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                name = input("Name: ")
                email = input("Email: ")
                phone = input("Phone: ")
                print(add_customer(name, email, phone))
            elif sub_choice == "2":
                customers = view_customers()
                if isinstance(customers, str):
                    print(customers)
                else:
                    for customer in customers:
                        print(customer)
        elif choice == "3":
            print("\nSales Management")
            print("1. Sell Book")
            print("2. View Sales Records")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                customer_name = input("Customer Name: ")
                book_title = input("Book Title: ")
                quantity_sold = int(input("Quantity: "))
                print(sell_book(customer_name, book_title, quantity_sold))
            elif sub_choice == "2":
                sales = view_sales()
                if isinstance(sales, str):
                    print(sales)
                else:
                    for sale in sales:
                        print(sale)
        elif choice == "4":
            print("Exiting")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
