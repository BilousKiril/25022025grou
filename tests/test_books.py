import uuid
class TestBook:
    def test_book_creation(self, first_book):
        assert first_book.name == "Book One"
        assert first_book.author == "Author One"
        assert isinstance(first_book.inn, uuid.UUID)

    def test_book_str_representation(self, first_book):
        book_str = str(first_book)
        assert "Book One" in book_str
        assert "Author One" in book_str
        assert str(first_book.inn) in book_str