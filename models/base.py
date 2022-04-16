import json
from dataclasses import Field, dataclass, field, fields
from os.path import isfile
from typing import List, Optional
from uuid import uuid4

from flask import Request

from models.privacystate import Privacy


def form_field(_type: Optional[str] = "text", **kwargs):
    """Creates a Model field that should appear on forms."""
    metadata = {"form": True, "type": _type}
    return field(metadata=metadata, **kwargs)


def select_form_field(
    options: List[str], multiple: Optional[bool] = False, **kwargs
):
    """Creates a Model field that should appear on forms as a selection."""
    metadata = {
        "form": True,
        "type": "multiple" if multiple else "select",
        "options": options,
    }
    return field(metadata=metadata, **kwargs)


@dataclass
class BaseModel:
    """Base class for LNX Calendar and Event model objects.

    Defines attributes/methods that all objects contain.
    """

    name: str = form_field()
    locale: str = form_field()
    tags: List[str] = form_field("textarea")
    privacy: Privacy = select_form_field(options=[e.value for e in Privacy])

    def __init__(self, *args, **kwargs):
        """Init Hack!

        We want to be able to declare unique ID's in the base class.

        But unique ID's are a "default" attribute.

        Dataclasses require all "default" attributes go last, otherwise they
        raise an error.

        To avoid the error, we will call the dataclass init first and
        _then_ set the unique id, so we force it to be last, even if subclasses
        had extra attributes
        """
        super().__init__(*args, **kwargs)
        self._uid: str = field(
            default_factory=uuid4, metadata={"private": True}
        )

    @classmethod
    @property
    def form_fields(cls):
        return {
            field.name: field.metadata
            for field in fields(cls)
            if field.metadata.get("form")
        }

    @classmethod
    @property
    def fields(cls) -> List[Field]:
        return fields(cls)

    @classmethod
    def save_from_form_data(cls, request: Request):
        storage_file = f"db/storage/{cls.__name__.lower()}.json"
        if not isfile(storage_file):
            with open(storage_file, "w") as fp:
                fp.write("[]\n")
        with open(storage_file, "r") as fp:
            data = json.load(fp)
        data.append(request.form.to_dict())
        with open(storage_file, "w") as fp:
            json.dump(data, fp)
    
############### Additions  ###################### 
    @classmethod
    def get(cls):
        storage_file = f"db/storage/{cls.__name__.lower()}.json"
        with open (storage_file, "r") as fp:
            things = json.load(fp)
            for a_dict  in things:
                for key, value in a_dict.items():
                    if val == value and key ==key:
                        return cls
                return"key doesnt exist"
    
    @classmethod
    def all(cls):
        storage_file = f"db/storage/{cls.__name__.lower()}.json"
        with open (storage_file, "r") as fp:
            return [cls(value) for value in json.load(fp)]