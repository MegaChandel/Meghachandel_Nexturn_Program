from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect("database.db")

@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    title = data.get("title")
    author = data.get("author")
    published_year = data.get("published_year")
    genre = data.get("genre")

    if not title or not author or not published_year or not genre:
        return jsonify({"error": "Invalid data", "message": "All fields are required"}), 400

    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO books (title, author, published_year, genre)
        VALUES (?, ?, ?, ?)
    ''', (title, author, published_year, genre))
    connection.commit()
    book_id = cursor.lastrowid
    connection.close()

    return jsonify({"message": "Book added successfully", "book_id": book_id}), 201

@app.route("/books", methods=["GET"])
def get_books():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    connection.close()

    if not books:
        return jsonify([])

    result = []
    for book in books:
        result.append({
            "id": book[0],
            "title": book[1],
            "author": book[2],
            "published_year": book[3],
            "genre": book[4]
        })
    return jsonify(result)

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book_by_id(book_id):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    book = cursor.fetchone()
    connection.close()

    if not book:
        return jsonify({"error": "Book not found", "message": "No book exists with the provided ID"}), 404

    return jsonify({
        "id": book[0],
        "title": book[1],
        "author": book[2],
        "published_year": book[3],
        "genre": book[4]
    })

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()
    title = data.get("title")
    author = data.get("author")
    published_year = data.get("published_year")
    genre = data.get("genre")

    if not title or not author or not published_year or not genre:
        return jsonify({"error": "Invalid data", "message": "All fields are required"}), 400

    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    book = cursor.fetchone()

    if not book:
        connection.close()
        return jsonify({"error": "Book not found", "message": "No book exists with the provided ID"}), 404

    cursor.execute('''
        UPDATE books
        SET title = ?, author = ?, published_year = ?, genre = ?
        WHERE id = ?
    ''', (title, author, published_year, genre, book_id))
    connection.commit()
    connection.close()

    return jsonify({"message": "Book updated successfully"})

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    book = cursor.fetchone()

    if not book:
        connection.close()
        return jsonify({"error": "Book not found", "message": "No book exists with the provided ID"}), 404

    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    connection.commit()
    connection.close()

    return jsonify({"message": "Book deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)
