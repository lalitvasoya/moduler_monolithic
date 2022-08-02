from rest_framework import status
from rest_framework.exceptions import APIException, ValidationError, NotFound


class EntityDoesNotExistsException(NotFound):
    pass

class EntityUpdateFailed(APIException):
    status_code = status.HTTP_424_FAILED_DEPENDENCY
