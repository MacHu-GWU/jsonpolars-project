# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR


@dataclasses.dataclass
class Lit(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.lit.value)
    value: T.Any = dataclasses.field(default=REQUIRED)

    def to_polars(self) -> pl.Expr:
        return pl.lit(self.value)


expr_enum_to_klass_mapping[ExprEnum.lit.value] = Lit


@dataclasses.dataclass
class Plus(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.plus.value)
    left: "T_EXPR" = dataclasses.field(default=REQUIRED)
    right: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=parse_expr(dct["left"]),
            right=parse_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return self.left.to_polars() + self.right.to_polars()


expr_enum_to_klass_mapping[ExprEnum.plus.value] = Plus


@dataclasses.dataclass
class Minus(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.minus.value)
    left: "T_EXPR" = dataclasses.field(default=REQUIRED)
    right: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=parse_expr(dct["left"]),
            right=parse_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return self.left.to_polars() - self.right.to_polars()


expr_enum_to_klass_mapping[ExprEnum.minus.value] = Minus
