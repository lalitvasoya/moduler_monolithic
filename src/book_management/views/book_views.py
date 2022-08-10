from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from common.dependency_injection import obj_graph
from src.book_management.services.book_services.book_service import BookService


class CreateBookApiView(ViewSet):

    def __init__(self, *args, **kwargs):
        super(ViewSet, self).__init__(*args, **kwargs)
        self.book_service = obj_graph.provide(BookService)

    def retrieve(self, request, pk: int):
        book = self.book_service.get_book_by_id(pk)
        return Response(book.data)

    def create(self, request):
        # book_dto = BookDTO(**request.data)
        book = self.book_service.create_book(request.data)
        return Response(book.data)

    def list(self, request):
        books = self.book_service.get_all_books()
        return Response(books.data)

    def update(self, request, pk: int):
        # book_dto = BookDTO(**request.data, exclude_unset=True)
        book = self.book_service.update_book(request.data, pk)
        return Response(book.data)

    def delete(self, request, pk: int):
        book = self.book_service.delete_book(pk)
        return Response(book.data)
