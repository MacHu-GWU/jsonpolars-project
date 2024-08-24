# -*- coding: utf-8 -*-

"""
Improve the original dataclasses module.
"""

import typing as T
import enum
import dataclasses

__version__ = "0.1.1"


class MetadataKeyEnum(str, enum.Enum):
    CONVERTER = "_better_dataclass_converter"


T_DATA = T.Dict[str, T.Any]
T_FIELDS = T.Dict[str, dataclasses.Field]

_class_fields: T.Dict[T.Any, T_FIELDS] = {}

T_DATA_LIKE = T.Union[T_DATA, "T_DATA_CLASS", None]


class DataClass:
    """
    Enhanced dataclass that does serialization and deserialization correctly,
    even if the dataclass has nested dataclass fields.

    Usage example::

        @dataclasses.dataclass
        class Profile(DataClass):
            firstname: str = dataclasses.field()
            lastname: str = dataclasses.field()
            ssn: str = dataclasses.field()

        @dataclasses.dataclass
        class Degree(DataClass):
            name: str = dataclasses.field()
            year: int = dataclasses.field()

        @dataclasses.dataclass
        class People(DataClass):
            id: int = dataclasses.field()
            profile: T.Optional[Profile] = Profile.nested_field(default=None)
            degrees: T.Optional[T.List[Degree]] = Degree.list_of_nested_field(default_factory=list)

        people = People(
            id=1,
            profile=Profile(
                firstname="David",
                lastname="John",
                ssn="123-45-6789",
            ),
            degrees=[
                Degree(name="Bachelor", year=2004),
                Degree(name="Master", year=2006),
            ],
        )
        people_data = people.to_dict()
        people1 = People.from_dict(people_data)
    """

    @classmethod
    def get_fields(cls) -> T_FIELDS:
        """
        Get the dict view of the ``dataclasses.Field`` in this class.
        It leverages the cache to avoid the overhead of ``dataclasses.fields``
        function call.
        """
        try:
            return _class_fields[cls]
        except KeyError:
            _class_fields[cls] = {
                field.name: field for field in dataclasses.fields(cls)
            }
            return _class_fields[cls]

    def to_dict(self) -> T_DATA:
        """
        Serialize the dataclass instance to a dict.
        """
        return dataclasses.asdict(self)

    @classmethod
    def from_dict(
        cls: T.Type["T_DATA_CLASS"],
        dct_or_obj: T_DATA_LIKE,
    ) -> T.Optional["DataClass"]:
        """
        Construct an instance from dataclass-like data.
        It could be a dictionary, an instance of this class, or None.
        """
        if isinstance(dct_or_obj, dict):
            _fields = cls.get_fields()
            kwargs = {}
            for k, v in dct_or_obj.items():
                field = _fields[k]
                if MetadataKeyEnum.CONVERTER.value in field.metadata:
                    kwargs[k] = field.metadata[MetadataKeyEnum.CONVERTER](v)
                else:
                    kwargs[k] = v
            return cls(**kwargs)
        elif isinstance(dct_or_obj, cls):
            return dct_or_obj
        elif dct_or_obj is None:
            return None
        else:  # pragma: no cover
            raise TypeError

    @classmethod
    def from_list(
        cls: T.Type["T_DATA_CLASS"],
        list_of_dct_or_obj: T.Optional[T.List[T_DATA_LIKE]],
    ) -> T.Optional[T.List[T.Optional["T_DATA_CLASS"]]]:
        """
        Construct list of instance from list of dataclass-like data.
        It could be a dictionary, an instance of this class, or None.
        """
        if isinstance(list_of_dct_or_obj, list):
            return [cls.from_dict(item) for item in list_of_dct_or_obj]
        elif list_of_dct_or_obj is None:
            return None
        else:  # pragma: no cover
            raise TypeError

    @classmethod
    def _from_mapper(
        cls: T.Type["T_DATA_CLASS"],
        map_of_dct_or_obj: T.Optional[T.Dict[str, T_DATA_LIKE]],
    ) -> T.Optional[T.Dict[str, T.Optional["T_DATA_CLASS"]]]:
        """
        Construct dict of instance from dict of dataclass-like data.
        It could be a dictionary, an instance of this class, or None.
        """
        if isinstance(map_of_dct_or_obj, dict):
            return {k: cls.from_dict(v) for k, v in map_of_dct_or_obj.items()}
        elif map_of_dct_or_obj is None:
            return None
        else:  # pragma: no cover
            raise TypeError

    @classmethod
    def nested_field(
        cls,
        default=dataclasses.MISSING,
        default_factory=dataclasses.MISSING,
        init=True,
        repr=True,
        hash=None,
        compare=True,
        metadata=None,
        **kwargs,
    ):
        """
        Declare a field that is another dataclass.
        """
        if metadata is None:
            metadata = {}
        metadata[MetadataKeyEnum.CONVERTER.value] = cls.from_dict
        params = dict(
            init=init,
            repr=repr,
            hash=hash,
            compare=compare,
            metadata=metadata,
        )
        if default is not dataclasses.MISSING:
            params["default"] = default
        if default_factory is not dataclasses.MISSING:
            params["default_factory"] = default_factory
        params.update(kwargs)
        return dataclasses.field(**params)

    @classmethod
    def list_of_nested_field(
        cls,
        default=dataclasses.MISSING,
        default_factory=dataclasses.MISSING,
        init=True,
        repr=True,
        hash=None,
        compare=True,
        metadata=None,
        **kwargs,
    ):
        """
        Declare a field that is a list of other dataclass.
        """
        if metadata is None:
            metadata = {}
        metadata[MetadataKeyEnum.CONVERTER.value] = cls.from_list
        params = dict(
            init=init,
            repr=repr,
            hash=hash,
            compare=compare,
            metadata=metadata,
        )
        if default is not dataclasses.MISSING:
            params["default"] = default
        if default_factory is not dataclasses.MISSING:
            params["default_factory"] = default_factory
        params.update(kwargs)
        return dataclasses.field(**params)

    @classmethod
    def map_of_nested_field(
        cls,
        default=dataclasses.MISSING,
        default_factory=dataclasses.MISSING,
        init=True,
        repr=True,
        hash=None,
        compare=True,
        metadata=None,
        **kwargs,
    ):
        """
        Declare a field that is a list of other dataclass.
        """
        if metadata is None:
            metadata = {}
        metadata[MetadataKeyEnum.CONVERTER.value] = cls._from_mapper
        params = dict(
            init=init,
            repr=repr,
            hash=hash,
            compare=compare,
            metadata=metadata,
        )
        if default is not dataclasses.MISSING:
            params["default"] = default
        if default_factory is not dataclasses.MISSING:
            params["default_factory"] = default_factory
        params.update(kwargs)
        return dataclasses.field(**params)


T_DATA_CLASS = T.TypeVar("T_DATA_CLASS", bound=DataClass)
