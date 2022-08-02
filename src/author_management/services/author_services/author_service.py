from core.models.author_management.author_models import Author
from src.author_management.dto.author_dtos import AuthorDTO, AuthorListDTO

from common.utils import get_list_of_dto_from_queryset
from common.execeptions import EntityDoesNotExistsException, EntityUpdateFailed


class AuthorService:

    def get_author_by_id(self, id: int):
        """ Get author by filtering by id """
        author = Author.objects.get(id=id)
        return AuthorDTO.from_orm(author)

    def is_author_exist(self, id: int):
        """ Check is author exist in the DB """
        authors = Author.objects.filter(id=id)
        if not authors.exists():
            return False
        return authors

    def create_author(self, author: AuthorDTO):
        author = Author.objects.create(**author.dict())
        return AuthorDTO.from_orm(author)

    def get_all_authors(self):
        authors = get_list_of_dto_from_queryset(queryset=Author.objects.all(), dto=AuthorDTO)
        return AuthorListDTO.from_orm(authors)

    def update_author(self, author_dto: AuthorDTO, pk):
        # validate the author
        authors = self.is_author_exist(pk)
        if not (authors and authors):
            raise EntityDoesNotExistsException

        # update the author
        data = author_dto.dict()
        data.pop('id')
        update_count = authors.update(**data)
        if not update_count:
            raise EntityUpdateFailed
        return AuthorDTO.from_orm(authors.first())

    def delete_author(self, pk: int):
        # validate the author
        authors = self.is_author_exist(pk)
        if not authors:
            raise EntityDoesNotExistsException

        # delete the author
        author = authors.first()
        authors.delete()
        return AuthorDTO.from_orm(author)
