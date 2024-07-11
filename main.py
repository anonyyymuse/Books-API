from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    bookTitle: str
    bookDesc: str
    bookReview: int

# Define books as instances of the Book model
books = {
    1: Book(
        bookTitle="The Whispering Woods",
        bookDesc="A thrilling fantasy novel set in a mystical forest where secrets and danger lurk in every shadow.",
        bookReview=4
    ),
    2: Book(
        bookTitle="Echoes of Eternity",
        bookDesc="An epic science fiction saga spanning galaxies, exploring the consequences of time travel and parallel dimensions.",
        bookReview=5
    ),
    3: Book(
        bookTitle="The Silent Observer",
        bookDesc="A psychological thriller that delves into the mind of a detective chasing a cunning serial killer in a bustling city.",
        bookReview=4
    ),
    4: Book(
        bookTitle="Whispers in the Dark",
        bookDesc="A chilling horror novel about a haunted mansion where past sins return to haunt unsuspecting guests.",
        bookReview=4
    ),
    5: Book(
        bookTitle="Beyond the Horizon",
        bookDesc="A heartwarming romance novel set against the backdrop of a small coastal town, where love and second chances collide.",
        bookReview=5
    ),
    6: Book(
        bookTitle="The Lost Chronicles",
        bookDesc="An archaeological adventure uncovering ancient artifacts that hold the key to a forgotten civilization's secrets.",
        bookReview=4
    ),
    7: Book(
        bookTitle="Voices from the Abyss",
        bookDesc="A collection of short stories exploring the depths of human emotion, from despair to resilience and everything in between.",
        bookReview=4
    ),
    8: Book(
        bookTitle="Threads of Destiny",
        bookDesc="A gripping historical fiction novel tracing the lives of interconnected characters across generations, amidst wars and revolutions.",
        bookReview=5
    ),
    9: Book(
        bookTitle="The Enigma Code",
        bookDesc="A pulse-pounding espionage thriller where an elite team races against time to decode a cryptic message that could change the course of history.",
        bookReview=4
    ),
    10: Book(
        bookTitle="Whispers of the Soul",
        bookDesc="A poignant collection of poems and reflections on life, love, and the human spirit, offering solace and inspiration.",
        bookReview=5
    )
}

class UpdateBook(BaseModel):
    bookTitle: Optional[str] = None
    bookDesc: Optional[str] = None
    bookReview: Optional[int] = None

@app.get('/')
def index():
    return books

@app.get('/get-book/{bookId}')
def getBook(bookId: int):
    if bookId not in books:
        return {'Error': 'Book not found.'}
    return books[bookId]

@app.post('/create-book/{bookId}')
def createBook(bookId: int, book: Book):
    if bookId in books:
        return {"Error": "Book already exists."}
    
    # Store the book as an instance of Book
    books[bookId] = book
    return books[bookId]

@app.put('/update-book/{bookId}')
def updateBook(bookId: int, book: UpdateBook):
    if bookId not in books:
        return {'Error': 'Book not found.'}
    
    # Update attributes if they are provided
    if book.bookTitle is not None:
        books[bookId].bookTitle = book.bookTitle
    
    if book.bookDesc is not None:
        books[bookId].bookDesc = book.bookDesc
    
    if book.bookReview is not None:
        books[bookId].bookReview = book.bookReview

    return books[bookId]


@app.delete('/delete/{bookId}')
def deleteBook(bookId: int):
    if bookId not in books:
        return {'Error': 'Book not found.'}

    del books[bookId]
    return {"Success":"Successfully deleted book."}