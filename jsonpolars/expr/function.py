# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR
    from ..typehint import OtherExpr


@dataclasses.dataclass
class Lit(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.lit.value)
    value: T.Any = dataclasses.field(default=REQUIRED)

    def to_polars(self) -> pl.Expr:
        return pl.lit(self.value)


expr_enum_to_klass_mapping[ExprEnum.lit.value] = Lit


def _other_expr_to_polars(other_expr: "OtherExpr"):
    """
    Convert jsonpolars expression to polars expression.

    Example

    >>> _other_expr_to_polars(1)
    1
    >>> _other_expr_to_polars("hello")
    'hello'
    >>> _other_expr_to_polars(Column("col_1"))
    pl.col("col_1")
    """
    if isinstance(other_expr, BaseExpr):
        return other_expr.to_polars()
    else:
        return other_expr


def _parse_other_expr(value) -> "OtherExpr":
    if isinstance(value, dict):
        return parse_expr(value)
    else:
        return value


@dataclasses.dataclass
class Plus(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.plus.value)
    left: "OtherExpr" = dataclasses.field(default=REQUIRED)
    right: "OtherExpr" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=_parse_other_expr(dct["left"]),
            right=_parse_other_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return _other_expr_to_polars(self.left) + _other_expr_to_polars(self.right)


expr_enum_to_klass_mapping[ExprEnum.plus.value] = Plus


@dataclasses.dataclass
class Minus(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.minus.value)
    left: "OtherExpr" = dataclasses.field(default=REQUIRED)
    right: "OtherExpr" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=_parse_other_expr(dct["left"]),
            right=_parse_other_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return _other_expr_to_polars(self.left) - _other_expr_to_polars(self.right)


expr_enum_to_klass_mapping[ExprEnum.minus.value] = Minus
