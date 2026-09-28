from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925
    },
    {
        "id": 2,
        "title": "Beloved",
        "author": "Toni Morrison",
        "year": 1987
    }
]

@app.get("/books")
def get_books():
    return jsonify(books)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)