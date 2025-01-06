customers = [
    {"name": "Ramesh Kumar", "email": "ramesh@example.com", "phone": "1234567890"},
    {"name": "Shivam", "email": "shivam@example.com", "phone": "0987654321"},
    {"name": "Ankit", "email": "ankit@example.com", "phone": "1122334455"},
]

def add_customer(name, email, phone):
    customer = {"name": name, "email": email, "phone": phone}
    customers.append(customer)
    return "Customer added successfully!"

def view_customers():
    if not customers:
        return "No customers available."
    return customers
