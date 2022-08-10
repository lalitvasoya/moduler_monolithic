from django.shortcuts import get_object_or_404

from core.models.book_management.book_models import Book
from core.serializers.book_serializers.book_serializers import BookModelSerializer


class BookService:

    def __init__(self, author_service):
        self.author_service = author_service

    def get_book_by_id(self, id: int):
        """ Get book by filtering by id """
        book = Book.objects.get(id=id)
        return BookModelSerializer(instance=book)

    def create_book(self, data: dict):
        book_serializer = BookModelSerializer(data=data)
        if not book_serializer.is_valid():
            return book_serializer.errors
        book_serializer.save()
        return book_serializer

    def get_all_books(self):
        queryset = Book.objects.all()
        book_serializer = BookModelSerializer(queryset, many=True)
        return book_serializer

    def update_book(self, data: dict, pk):
        book = get_object_or_404(Book, pk=pk)
        book_serializer = BookModelSerializer(book, data, partial=True)
        if book_serializer.is_valid(raise_exception=True):
            book_serializer.save()
        return book_serializer

    def delete_book(self, pk: int):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        book_serializer = BookModelSerializer(book)
        return book_serializer
