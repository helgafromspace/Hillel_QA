import sqlite3

from base_repo import BaseRepository


class Book:

    def __init__(self, book_id, title, author:str, publish_year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publish_year = publish_year

    def __repr__(self):
        return f'Book: {self.book_id}, {self.title},{self.author},{self.publish_year}'

class BookRepository(BaseRepository):

    def __init__(self):
        super().__init__()
        self._cursor.execute('CREATE TABLE IF NOT EXISTS Book(book_id INTEGER PRIMARY KEY, title TEXT, author TEXT, publish_year INTEGER);')

    def get_all_books(self):
        self._cursor.execute('select * from Book;')
        data = self._cursor.fetchall()
        return data

    def add_book(self, *books):
        for book in books:
            self._cursor.execute ("INSERT INTO Book VALUES(?,?,?,?);", (book.book_id,book.title,book.author,book.publish_year))


book_repository = BookRepository()
print(book_repository.get_all_books())

book1 = Book(1,'1984','George Orwell',1949)
book2 = Book(2,'Law','PLato',1979)
book3 = Book(3,'A Brief History Of Time','Steven Hawking',2020)
book_repository.add_book(book1)
print(book_repository.get_all_books())
book_repository.add_book(book2,book3)
print(book_repository.get_all_books())


