from fastapi import FastAPI
import time

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books")
def read_all_books():
    return BOOKS

@app.get("/books/{dynamic_param}")
def read_all_boocks(dynamic_param: str):
    for book in BOOKS:
        if book.get('title').casefold() == dynamic_param.casefold():
            return book

@app.get("/books/")
def category_getter(category: str):
    category_books = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            category_books.append(book)
    
    return category_books
