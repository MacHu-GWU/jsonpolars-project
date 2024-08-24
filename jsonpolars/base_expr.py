# -*- coding: utf-8 -*-

import typing as T
import enum
import dataclasses

from .vendor.better_dataclasses import DataClass

from .sentinel import NOTHING, REQUIRED, OPTIONAL

if T.TYPE_CHECKING:  # pragma: no cover
    from .expr.api import T_EXPR


class ExprEnum(str, enum.Enum):
    # Aggregation
    # Array
    # Binary
    binary = "binary"
    # Boolean
    # Categories
    # Columns / names
    column = "column"
    alias = "alias"
    # Computation
    # Functions
    lit = "lit"
    plus = "plus"
    minus = "minus"
    multiple = "multiple"
    divide = "divide"
    # List
    list = "list"
    list_get = "list_get"
    # Manipulation / selection
    cast = "cast"
    # Meta
    # Miscellaneous
    # Name
    # Operators
    # String
    string = "string"
    split = "split"
    # Struct
    struct = "struct"
    # Temporal
    dt = "datetime"
    dt_to_string = "dt_to_string"
    # Window


@dataclasses.dataclass
class BaseExpr(DataClass):
    type: str = dataclasses.field(default=REQUIRED)

    def _validate(self):
        for k, v in dataclasses.asdict(self).items():
            if v is REQUIRED:  # pragma: no cover
                raise ValueError(f"Field {k!r} is required for {self.__class__}.")

    def __post_init__(self):
        self._validate()

    def to_polars(self):
        raise NotImplementedError()


expr_enum_to_klass_mapping: T.Dict[str, T.Type["T_EXPR"]] = dict()


def parse_expr(dct: T.Dict[str, T.Any]) -> "T_EXPR":
    """
    Note: you have to import everything in the :mod:`jsonpolars.expr` module
    to make this work.
    """
    return expr_enum_to_klass_mapping[dct["type"]].from_dict(dct)
