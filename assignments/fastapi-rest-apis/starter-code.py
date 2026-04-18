from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book API")


class Book(BaseModel):
    id: int
    title: str
    author: str


books = []


@app.get("/books")
def list_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def create_book(book: Book):
    books.append(book.model_dump())
    return {"message": "Book created", "book": book}


# TODO: Add PUT /books/{book_id}
# TODO: Add DELETE /books/{book_id}
