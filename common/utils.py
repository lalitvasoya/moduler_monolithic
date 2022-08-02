

def get_list_of_dto_from_queryset(queryset, dto):
    return [dto.from_orm(obj).dict() for obj in queryset]
