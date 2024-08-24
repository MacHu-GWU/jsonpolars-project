# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR


@dataclasses.dataclass
class List(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.list.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=expr_enum_to_klass_mapping[dct["expr"]["type"]].from_dict(dct["expr"]),
        )

    def to_polars(self):
        return self.expr.to_polars().list


expr_enum_to_klass_mapping[ExprEnum.list.value] = List


@dataclasses.dataclass
class ListGet(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.list_get.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    index: T.Union[int, "T_EXPR"] = dataclasses.field(default=REQUIRED)
    null_on_oob: bool = dataclasses.field(default=False)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        index = dct["index"]
        if isinstance(index, int):
            pass
        elif isinstance(index, dict):
            index = expr_enum_to_klass_mapping[index["type"]].from_dict(index)
        else:  # pragma: no cover
            raise ValueError(f"Unknown index type: {index}")
        return cls(
            expr=expr_enum_to_klass_mapping[dct["expr"]["type"]].from_dict(dct["expr"]),
            index=index,
            null_on_oob=dct["null_on_oob"],
        )

    def to_polars(self):
        if isinstance(self.index, int):
            index = self.index
        elif isinstance(self.index, BaseExpr):
            index = self.index.to_polars()

        return self.expr.to_polars().get(index=index, null_on_oob=self.null_on_oob)


expr_enum_to_klass_mapping[ExprEnum.list_get.value] = ListGet
