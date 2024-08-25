# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr
from ..utils_expr import parse_other_expr

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR
    from ..typehint import OtherExpr


@dataclasses.dataclass
class Lit(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.lit.html
    """

    type: str = dataclasses.field(default=ExprEnum.lit.value)
    value: T.Any = dataclasses.field(default=REQUIRED)
    dtype: T.Optional["pl.DataType"] = dataclasses.field(default=None)
    allow_object: bool = dataclasses.field(default=False)

    def to_polars(self) -> pl.Expr:
        return pl.lit(
            value=self.value,
            dtype=self.dtype,
            allow_object=self.allow_object,
        )


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


@dataclasses.dataclass
class Plus(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.add.html
    """
    type: str = dataclasses.field(default=ExprEnum.plus.value)
    left: "OtherExpr" = dataclasses.field(default=REQUIRED)
    right: "OtherExpr" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=parse_other_expr(dct["left"]),
            right=parse_other_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return _other_expr_to_polars(self.left) + _other_expr_to_polars(self.right)


expr_enum_to_klass_mapping[ExprEnum.plus.value] = Plus


@dataclasses.dataclass
class Minus(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.sub.html
    """
    type: str = dataclasses.field(default=ExprEnum.minus.value)
    left: "OtherExpr" = dataclasses.field(default=REQUIRED)
    right: "OtherExpr" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=parse_other_expr(dct["left"]),
            right=parse_other_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return _other_expr_to_polars(self.left) - _other_expr_to_polars(self.right)


expr_enum_to_klass_mapping[ExprEnum.minus.value] = Minus
