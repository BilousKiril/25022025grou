import pytest
from models import Person, Bank, BankAccount, Library, Book


@pytest.fixture(scope="session")
def person() -> Person:
    oleg = Person('Oleg')
    return oleg


@pytest.fixture(scope="session")
def another_person() -> Person:
    oleg = Person('Oleg')
    return oleg


@pytest.fixture(scope="session")
def bank():
    b = Bank('Mono')
    return b


@pytest.fixture(scope="session")
def bank2():
    b = Bank('Privat')
    return b

@pytest.fixture(scope="session")
def bank_account(bank, person) -> BankAccount:
    account = bank.open_account(person)
    return account

@pytest.fixture(scope="session")
def bank_account2(bank, another_person) -> BankAccount:
    account = bank.open_account(another_person)
    return account

@pytest.fixture
def library():
    return Library("Ukranian")

@pytest.fixture
def another_library():
    return Library("Foreign Books")

@pytest.fixture
def first_book():
    return Book("Book One", "Author One")

@pytest.fixture
def another_book():
    return Book("Book Two", "Author Two")
