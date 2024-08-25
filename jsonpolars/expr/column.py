# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR


@dataclasses.dataclass
class Column(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/col.html
    """
    type: str = dataclasses.field(default=ExprEnum.column.value)
    name: str = dataclasses.field(default=REQUIRED)

    def to_polars(self) -> pl.Expr:
        return pl.col(self.name)


expr_enum_to_klass_mapping[ExprEnum.column.value] = Column


@dataclasses.dataclass
class Alias(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.alias.html
    """
    type: str = dataclasses.field(default=ExprEnum.alias.value)
    name: str = dataclasses.field(default=REQUIRED)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            name=dct["name"],
            expr=parse_expr(dct["expr"]),
        )

    def to_polars(self) -> pl.Expr:
        return self.expr.to_polars().alias(self.name)


expr_enum_to_klass_mapping[ExprEnum.alias.value] = Alias
