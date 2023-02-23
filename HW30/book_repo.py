import sqlite3
from ctypes import Union

from base_repo import BaseRepository


class Book:

    def __init__(self, title, author, publish_year):
        self.title = title
        self.author = author
        self.publish_year = publish_year

    def __repr__(self):
        return f'{self.title}, {self.author},{self.publish_year}'

class BookRepository(BaseRepository):

    def __init__(self):
        super().__init__()
        self._cursor.execute('CREATE TABLE IF NOT EXISTS Book(book_id INTEGER PRIMARY KEY, title TEXT, author TEXT, publish_year INTEGER);')

    def get_all_books(self):
        self._cursor.execute('select title,author,publish_year from Book;')
        data = self._cursor.fetchall()
        return [self.row2object(row) for row in data]

    def add_books(self, *books):
        for book in books:
            self._cursor.execute ("INSERT INTO Book(title,author,publish_year) VALUES(?,?,?);", (book.title,book.author,book.publish_year))

    def update_publish_year(self,new_year:int,old_year:int, title):
        self._cursor.execute ("UPDATE Book SET publish_year = ? where publish_year = ? and title = ?;", (new_year,old_year,title))

    def select_all_books_of_specific_publish_year(self,year:int):
        self._cursor.execute ("select title,author,publish_year from Book where publish_year = ?;", (year,))
        data = self._cursor.fetchall()
        return [self.row2object(row) for row in data]

    def select_all_books_of_specific_author(self,author):
        self._cursor.execute ("select title,author,publish_year from Book where author = ?;",(author,))
        data = self._cursor.fetchall()
        return [self.row2object(row) for row in data]

    def delete_all_books_of_specific_author(self,author):
        self._cursor.execute ("delete from Book where author = ?;", (author,))

    def row2object(self,row):
        return Book(row[0],row[1],row[2])



book_repository = BookRepository()
print(book_repository.get_all_books())


book1 = Book('1984','George Orwell',1949)
book_repository.get_all_books()

book2 = Book('The Laws','Plato',1979)
book3 = Book('A Brief History Of Time','Steven Hawking',2020)
book4 = Book('The Republic','Plato',2020)
book5 = Book('Animal Farm','George Orwell',2020)
#
book_repository.add_books(book1)

print(book_repository.get_all_books())

book_repository.add_books(book2,book3, book4, book5)
print(book_repository.get_all_books())
#
print(book_repository.select_all_books_of_specific_publish_year(2020))
print(book_repository.select_all_books_of_specific_author('George Orwell'))
book_repository.update_publish_year(1950,1949,'1984')
print(book_repository.get_all_books())
book_repository.delete_all_books_of_specific_author('Plato')
print(book_repository.get_all_books())

