from core.models.book_management.book_models import Book
from src.book_management.dto.book_dtos import BookDTO, BookListDTO
from common.utils import get_list_of_dto_from_queryset

from common.execeptions import EntityDoesNotExistsException, EntityUpdateFailed


class BookService:

    def __init__(self, author_service):
        self.author_service = author_service

    def get_book_by_id(self, id: int):
        """ Get book by filtering by id """
        book = Book.objects.get(id=id)
        return BookDTO.from_orm(book)

    def is_book_exist(self, id: int):
        """ Check is book exist in the DB """
        books = Book.objects.filter(id=id)
        if not books.exists():
            return False
        return books

    def create_book(self, book: BookDTO):
        if not self.author_service.is_author_exist(book.author_id):
            raise EntityDoesNotExistsException
        book = Book.objects.create(**book.dict())
        return BookDTO.from_orm(book)

    def get_all_books(self):
        books = get_list_of_dto_from_queryset(queryset=Book.objects.all(), dto=BookDTO)
        return BookListDTO.from_orm(books)

    def update_book(self, book_dto: BookDTO, pk):
        # validate the book and author
        books = self.is_book_exist(pk)
        authors = self.author_service.is_author_exist(book_dto.author_id)
        if not (books and authors):
            raise EntityDoesNotExistsException

        # update the book
        data = book_dto.dict()
        data.pop('id')
        update_count = books.update(**data)
        if not update_count:
            raise EntityUpdateFailed
        return BookDTO.from_orm(books.first())

    def delete_book(self, pk: int):
        # validate the book
        books = self.is_book_exist(pk)
        if not books:
            raise EntityDoesNotExistsException

        # delete the book
        book = books.first()
        books.delete()
        return BookDTO.from_orm(book)
