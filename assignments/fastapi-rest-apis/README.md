# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI that supports creating, reading, updating, and deleting items. You will learn API routing, request validation, response handling, and local testing with interactive API docs.

## 📝 Tasks

### 🛠️ Build Core API Endpoints

#### Description
Create a FastAPI app that manages a simple in-memory collection of books. Implement endpoints that allow users to create a new book and retrieve one or all books.

#### Requirements
Completed program should:

- Define a FastAPI application in `starter-code.py`.
- Create a `Book` model using Pydantic with fields for `id`, `title`, and `author`.
- Implement `GET /books` to return all books.
- Implement `GET /books/{book_id}` to return one book by ID.
- Implement `POST /books` to add a new book with request body validation.


### 🛠️ Add Update/Delete and Error Handling

#### Description
Extend your API so records can be edited and removed. Add clear error responses when a requested book does not exist, and verify behavior using FastAPI docs.

#### Requirements
Completed program should:

- Implement `PUT /books/{book_id}` to update an existing book.
- Implement `DELETE /books/{book_id}` to remove a book.
- Return an appropriate error response (for example, 404) for missing book IDs.
- Return JSON responses for successful update/delete operations.
- Run the app locally and test all endpoints in `/docs`.
