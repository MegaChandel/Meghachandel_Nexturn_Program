import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    published_year INTEGER NOT NULL,
    genre TEXT NOT NULL
)
''')

sample_data = [
    ("The Guide", "R. K. Narayan", 1958, "Fiction"),
    ("Malgudi Days", "R. K. Narayan", 1943, "Short Stories"),
    ("Train to Pakistan", "Khushwant Singh", 1956, "Historical Fiction"),
]

cursor.executemany('''
INSERT INTO books (title, author, published_year, genre)
VALUES (?, ?, ?, ?)
''', sample_data)

connection.commit()
connection.close()

print("Database initialized with sample data.")
