#!/usr/bin/env python3

"""Base class for all models in the application."""

from datetime import datetime
from typing import TypeVar, List, Iterable
from os import path
import json
import uuid


TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S"

# Dictionary to store data
DATA = {}


class Base:
    """Base class for all models in the application."""

    def __init__(self, *args: list, **kwargs: dict):
        """Constructor method for Base class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        s_class = str(self.__class__.__name__)
        if DATA.get(s_class) is None:
            DATA[s_class] = {}

        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = datetime.strptime(
            kwargs.get('created_at', datetime.utcnow().strftime
                       (TIMESTAMP_FORMAT)),
            TIMESTAMP_FORMAT
        )
        self.updated_at = datetime.strptime(
            kwargs.get('updated_at', datetime.utcnow().strftime
                       (TIMESTAMP_FORMAT)),
            TIMESTAMP_FORMAT
        )

    def __eq__(self, other: TypeVar('Base')) -> bool:
        """Check if two objects are equal.

        Args:
            other: Object to compare with.

        Returns:
            True if the objects are equal, False otherwise.
        """
        if not isinstance(other, Base):
            return False
        return self.id == other.id

    def to_json(self, for_serialization: bool = False) -> dict:
        """Convert object to JSON format.

        Args:
            for_serialization: Flag to indicate if the object is being
                               serialized.

        Returns:
            Dictionary representation of the object.
        """
        result = {}
        for key, value in self.__dict__.items():
            if not for_serialization and key[0] == '_':
                continue
            if isinstance(value, datetime):
                result[key] = value.strftime(TIMESTAMP_FORMAT)
            else:
                result[key] = value
        return result

    @classmethod
    def load_from_file(cls):
        """Load data from file."""
        s_class = cls.__name__
        file_path = f".db_{s_class}.json"
        DATA[s_class] = {}
        if not path.exists(file_path):
            return

        with open(file_path, 'r') as f:
            objs_json = json.load(f)
            for obj_id, obj_json in objs_json.items():
                DATA[s_class][obj_id] = cls(**obj_json)

    @classmethod
    def save_to_file(cls):
        """Save data to file."""
        s_class = cls.__name__
        file_path = f".db_{s_class}.json"
        objs_json = {obj_id: obj.to_json(True) for obj_id,
                     obj in DATA[s_class].items()}

        with open(file_path, 'w') as f:
            json.dump(objs_json, f)

    def save(self):
        """Save object to data store."""
        s_class = self.__class__.__name__
        self.updated_at = datetime.utcnow()
        DATA[s_class][self.id] = self
        self.__class__.save_to_file()

    def remove(self):
        """Remove object from data store."""
        s_class = self.__class__.__name__
        if self.id in DATA[s_class]:
            del DATA[s_class][self.id]
            self.__class__.save_to_file()

    @classmethod
    def count(cls) -> int:
        """Get count of objects in data store.

        Returns:
            Count of objects in data store.
        """
        s_class = cls.__name__
        return len(DATA[s_class])

    @classmethod
    def all(cls) -> Iterable[TypeVar('Base')]:
        """Get all objects in data store.

        Returns:
            Iterable of objects in data store.
        """
        return cls.search()

    @classmethod
    def get(cls, id: str) -> TypeVar('Base'):
        """Get object with given id from data store.

        Args:
            id: Id of the object to retrieve.

        Returns:
            Object with given id, or None if not found.
        """
        s_class = cls.__name__
        return DATA[s_class].get(id)

    @classmethod
    def search(cls, attributes: dict = {}) -> List[TypeVar('Base')]:
        """Search objects in data store based on attributes.

        Args:
            attributes: Dictionary of attributes to match.

        Returns:
            List of objects matching the attributes.
        """
        s_class = cls.__name__

        def _search(obj):
            if not attributes:
                return True
            for k, v in attributes.items():
                if getattr(obj, k) != v:
                    return False
            return True

        return list(filter(_search, DATA[s_class].values()))
