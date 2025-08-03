from pydantic import BaseModel


def is_empty(model: BaseModel) -> bool:
    """
    Check if all values in given model are NoneType.
    """
    return not any(value is not None for value in model.model_dump().values())


def dump_non_null_fields(model: BaseModel) -> dict:
    """
    Dump all fieds from given model which are not NoneType.
    """
    return {
            key: value for key, value in model.model_dump().items() if value is not None
        }
