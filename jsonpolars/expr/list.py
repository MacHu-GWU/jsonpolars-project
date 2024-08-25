# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR


def ensure_list(expr: "T_EXPR") -> pl.Expr:
    if isinstance(expr, List):
        return expr.to_polars()
    else:
        return expr.to_polars().list


@dataclasses.dataclass
class List(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/list.html
    """
    type: str = dataclasses.field(default=ExprEnum.list.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_list(self.expr)


expr_enum_to_klass_mapping[ExprEnum.list.value] = List


@dataclasses.dataclass
class ListGet(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.list.get.html#polars.Expr.list.get
    """
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
            index = parse_expr(index)
        else:  # pragma: no cover
            raise ValueError(f"Unknown index type: {index}")
        return cls(
            expr=parse_expr(dct["expr"]),
            index=index,
            null_on_oob=dct["null_on_oob"],
        )

    def to_polars(self) -> pl.Expr:
        expr = ensure_list(self.expr)
        if isinstance(self.index, int):
            index = self.index
        elif isinstance(self.index, BaseExpr):
            index = self.index.to_polars()
        return expr.get(index=index, null_on_oob=self.null_on_oob)


expr_enum_to_klass_mapping[ExprEnum.list_get.value] = ListGet
