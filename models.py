import uuid
from typing import Self

class Person:
    def __init__(self, name: str):
        self.name: str = name
        self.inn: uuid.UUID = uuid.uuid4()

    def __str__(self):
        return f'<Person {self.name} - {self.inn}>'

class Bank:
    def __init__(self, name: str):
        self.name = name
        self.accounts: list[BankAccount] = []

    def open_account(self, client: Person):
        new_account = BankAccount(client)
        self.accounts.append(new_account)
        return new_account

    @property
    def passive(self):
        pas = 0
        for account in self.accounts:
            if account.balance > 0:
                pas += account.balance
        return pas


    @property
    def active(self):
        act = 0
        for account in self.accounts:
            if account.balance < 0:

                act += account.balance
        return act

class BankAccount:
    def __init__(self, client: Person):
        self.client = client
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def transfer(self, other: Self, amount):
        self.balance -= amount
        other.balance += amount

# Class book

class Book:
    def __init__(self, name: str, author: str):
        self.name: str = name
        self.author: str = author
        self.inn: uuid.UUID = uuid.uuid4()

    def __str__(self):
        return f'<Book: {self.name}; Author: {self.author}; Inn: {self.inn}>'


# Class Library

class Library:
    def __init__(self, name: str):
        self.name = name
        self.books: list[Book] = []

    def add_book(self, Book):
        self.books.append(Book)

    def remove_book(self, inn):
        for book in self.books:
            if inn == book.inn:
                self.books.remove(book)
                break




