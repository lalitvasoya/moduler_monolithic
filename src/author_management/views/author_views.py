from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from common.dependency_injection import obj_graph
from src.author_management.services.author_services.author_service import AuthorService


class CreateAuthorApiView(ViewSet):

    def __init__(self, *args, **kwargs):
        super(ViewSet, self).__init__(*args, **kwargs)
        self.author_service = obj_graph.provide(AuthorService)

    def retrieve(self, request, pk: int):
        author = self.author_service.get_author_by_id(pk)
        return Response(author.data)

    def create(self, request):
        author = self.author_service.create_author(request.data)
        return Response(author.data)

    def list(self, request):
        authors = self.author_service.get_all_authors()
        return Response(authors.data)

    def update(self, request, pk: int):
        author = self.author_service.update_author(request.data, pk)
        return Response(author.data)

    def delete(self, request, pk: int):
        author = self.author_service.delete_author(pk)
        return Response(author.data)
