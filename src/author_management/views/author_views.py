from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from common.provider import Provider
from common.dependency_injection import obj_graph
from src.author_management.dto.author_dtos import AuthorDTO


class CreateAuthorApiView(ViewSet):

    def __init__(self, *args, **kwargs):
        super(ViewSet, self).__init__(*args, **kwargs)
        obj = obj_graph.provide(Provider)
        self.author_service = obj.author_service

    def retrieve(self, request, pk: int):
        author = self.author_service.get_author_by_id(pk)
        return Response(author.dict())

    def create(self, request):
        author_dto = AuthorDTO(**request.data)
        author = self.author_service.create_author(author_dto)
        return Response(author.dict())

    def list(self, request):
        authors = self.author_service.get_all_authors()
        return Response(authors.dict().get('__root__'))

    def update(self, request, pk: int):
        author_dto = AuthorDTO(**request.data, exclude_unset=True)
        author = self.author_service.update_author(author_dto, pk)
        return Response(author.dict())

    def delete(self, request, pk: int):
        author = self.author_service.delete_author(pk)
        return Response(author.dict())
