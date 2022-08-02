from pinject import copy_args_to_public_fields


class Provider:

    @copy_args_to_public_fields
    def __init__(self, book_service, author_service):
        pass
