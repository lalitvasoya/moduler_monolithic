from pinject import BindingSpec, new_object_graph
from src.book_management.services.book_services.book_service import BookService
from src.author_management.services.author_services.author_service import AuthorService


class Dependencies(BindingSpec):

    def configure(self, bind):

        bind("author_service", to_class=AuthorService)
        bind("book_service", to_class=BookService)


obj_graph = new_object_graph(modules=None, binding_specs=[Dependencies()])
