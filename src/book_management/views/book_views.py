from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from common.provider import Provider
from common.dependency_injection import obj_graph
from src.book_management.dto.book_dtos import BookDTO


class CreateBookApiView(ViewSet):

    def __init__(self, *args, **kwargs):
        super(ViewSet, self).__init__(*args, **kwargs)
        obj = obj_graph.provide(Provider)
        self.book_service = obj.book_service

    def retrieve(self, request, pk: int):
        book = self.book_service.get_book_by_id(pk)
        return Response(book.dict())

    def create(self, request):
        book_dto = BookDTO(**request.data)
        book = self.book_service.create_book(book_dto)
        return Response(book.dict())

    def list(self, request):
        books = self.book_service.get_all_books()
        return Response(books.dict().get('__root__'))

    def update(self, request, pk: int):
        book_dto = BookDTO(**request.data, exclude_unset=True)
        book = self.book_service.update_book(book_dto, pk)
        return Response(book.dict())

    def delete(self, request, pk: int):
        book = self.book_service.delete_book(pk)
        return Response(book.dict())
