import pytest

from l_space.models import Book


@pytest.fixture
@pytest.mark.django_db
def book():
    book = Book.objects.create(title="test_title", author="test_author")
    yield book


@pytest.mark.django_db
def test_book_view_displays_book(client, book):
    response = client.get("/")
    assert book.title in response.content.decode()
