from django.shortcuts import get_object_or_404

from core.models.author_management.author_models import Author
from core.serializers.author_serializers.author_serializers import AuthorModelSerializer


class AuthorService:

    def get_author_by_id(self, id: int):
        """ Get author by filtering by id """
        author = Author.objects.get(id=id)
        return AuthorModelSerializer(instance=author)

    def create_author(self, data: dict):
        author_serializer = AuthorModelSerializer(data=data)
        if not author_serializer.is_valid():
            return author_serializer.errors
        author_serializer.save()
        return author_serializer

    def get_all_authors(self):
        queryset = Author.objects.all()
        author_serializer = AuthorModelSerializer(queryset, many=True)
        return author_serializer

    def update_author(self, data: dict, pk):
        author = get_object_or_404(Author, pk=pk)
        author_serializer = AuthorModelSerializer(author, data, partial=True)
        if author_serializer.is_valid(raise_exception=True):
            author_serializer.save()
        return author_serializer

    def delete_author(self, pk: int):
        author = get_object_or_404(Author, pk=pk)
        author.delete()
        author_serializer = AuthorModelSerializer(author)
        return author_serializer
