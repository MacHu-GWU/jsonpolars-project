# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR


@dataclasses.dataclass
class String(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.string.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
        )

    def to_polars(self) -> pl.Expr:
        return self.expr.to_polars().str


expr_enum_to_klass_mapping[ExprEnum.string.value] = String


@dataclasses.dataclass
class Split(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.str_split.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    by: str = dataclasses.field(default=REQUIRED)
    inclusive: bool = dataclasses.field(default=False)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            by=dct["by"],
            inclusive=dct["inclusive"],
        )

    def to_polars(self) -> pl.Expr:
        if isinstance(self.expr, String):
            expr = self.expr.to_polars()
        else:
            expr = self.expr.to_polars().str
        return expr.split(by=self.by, inclusive=self.inclusive)


expr_enum_to_klass_mapping[ExprEnum.str_split.value] = Split


@dataclasses.dataclass
class StrJoin(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.str_join.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    delimiter: str = dataclasses.field(default="")
    ignore_nulls: bool = dataclasses.field(default=True)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            delimiter=dct.get("delimiter", ""),
            ignore_nulls=dct.get("ignore_nulls", True),
        )

    def to_polars(self) -> pl.Expr:
        return self.expr.to_polars().str.join(
            delimiter=self.delimiter, ignore_nulls=self.ignore_nulls
        )


# Add this class to the expr_enum_to_klass_mapping
expr_enum_to_klass_mapping[ExprEnum.str_join.value] = StrJoin
