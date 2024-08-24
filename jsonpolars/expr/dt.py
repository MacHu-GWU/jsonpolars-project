# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR


@dataclasses.dataclass
class Datetime(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.dt.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]))

    def to_polars(self) -> pl.Expr:
        return self.expr.to_polars().dt


expr_enum_to_klass_mapping[ExprEnum.dt.value] = Datetime


@dataclasses.dataclass
class DatetimeToString(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.dt_to_string.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    format: str = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=expr_enum_to_klass_mapping[dct["expr"]["type"]].from_dict(dct["expr"]),
            format=dct["format"],
        )

    def to_polars(self) -> pl.Expr:
        return self.expr.to_polars().to_string(format=self.format)


expr_enum_to_klass_mapping[ExprEnum.dt_to_string.value] = DatetimeToString


# @dataclasses.dataclass
# class DatetimeYear(BaseExpr):
#     type: str = dataclasses.field(default=ExprEnum.dt_year.value)
#     expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
#
#     @classmethod
#     def from_dict(cls, dct: T.Dict[str, T.Any]):
#         return cls(
#             expr=parse_expr(dct["expr"]),
#         )
#
#     def to_polars(self) -> pl.Expr:
#         expr = self.expr.to_polars()
#         return self.expr.to_polars().month()
#
#
# expr_enum_to_klass_mapping[ExprEnum.dt_year.value] = DatetimeYear
