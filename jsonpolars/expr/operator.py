# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr
from ..utils_expr import to_jsonpolars_other_expr

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR
    from ..typehint import OtherExpr


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

    type: str = dataclasses.field(default=ExprEnum.add.value)
    left: "OtherExpr" = dataclasses.field(default=REQUIRED)
    right: "OtherExpr" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=to_jsonpolars_other_expr(dct["left"]),
            right=to_jsonpolars_other_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return _other_expr_to_polars(self.left) + _other_expr_to_polars(self.right)


expr_enum_to_klass_mapping[ExprEnum.add.value] = Plus


@dataclasses.dataclass
class Minus(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.sub.html
    """

    type: str = dataclasses.field(default=ExprEnum.sub.value)
    left: "OtherExpr" = dataclasses.field(default=REQUIRED)
    right: "OtherExpr" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=to_jsonpolars_other_expr(dct["left"]),
            right=to_jsonpolars_other_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return _other_expr_to_polars(self.left) - _other_expr_to_polars(self.right)


expr_enum_to_klass_mapping[ExprEnum.sub.value] = Minus


@dataclasses.dataclass
class Multiply(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.mul.html
    """

    type: str = dataclasses.field(default=ExprEnum.mul.value)
    left: "OtherExpr" = dataclasses.field(default=REQUIRED)
    right: "OtherExpr" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=to_jsonpolars_other_expr(dct["left"]),
            right=to_jsonpolars_other_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return _other_expr_to_polars(self.left) * _other_expr_to_polars(self.right)


expr_enum_to_klass_mapping[ExprEnum.mul.value] = Multiply


@dataclasses.dataclass
class TrueDiv(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.truediv.html
    """

    type: str = dataclasses.field(default=ExprEnum.truediv.value)
    left: "OtherExpr" = dataclasses.field(default=REQUIRED)
    right: "OtherExpr" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=to_jsonpolars_other_expr(dct["left"]),
            right=to_jsonpolars_other_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return _other_expr_to_polars(self.left) / _other_expr_to_polars(self.right)


expr_enum_to_klass_mapping[ExprEnum.truediv.value] = TrueDiv


@dataclasses.dataclass
class FloorDiv(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.floordiv.html
    """

    type: str = dataclasses.field(default=ExprEnum.floordiv.value)
    left: "OtherExpr" = dataclasses.field(default=REQUIRED)
    right: "OtherExpr" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=to_jsonpolars_other_expr(dct["left"]),
            right=to_jsonpolars_other_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return _other_expr_to_polars(self.left) // _other_expr_to_polars(self.right)


expr_enum_to_klass_mapping[ExprEnum.floordiv.value] = FloorDiv


@dataclasses.dataclass
class Negative(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.neg.html
    """

    type: str = dataclasses.field(default=ExprEnum.neg.value)
    expr: "OtherExpr" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=to_jsonpolars_other_expr(dct["expr"]),
        )

    def to_polars(self) -> pl.Expr:
        return -_other_expr_to_polars(self.expr)


expr_enum_to_klass_mapping[ExprEnum.neg.value] = Negative


@dataclasses.dataclass
class Pow(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.pow.html
    """

    type: str = dataclasses.field(default=ExprEnum.pow.value)
    left: "OtherExpr" = dataclasses.field(default=REQUIRED)
    right: "OtherExpr" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=to_jsonpolars_other_expr(dct["left"]),
            right=to_jsonpolars_other_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return _other_expr_to_polars(self.left) ** _other_expr_to_polars(self.right)


expr_enum_to_klass_mapping[ExprEnum.pow.value] = Pow


@dataclasses.dataclass
class Equal(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.eq.html
    """

    type: str = dataclasses.field(default=ExprEnum.eq.value)
    left: "OtherExpr" = dataclasses.field(default=REQUIRED)
    right: "OtherExpr" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=to_jsonpolars_other_expr(dct["left"]),
            right=to_jsonpolars_other_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return _other_expr_to_polars(self.left) == _other_expr_to_polars(self.right)


expr_enum_to_klass_mapping[ExprEnum.eq.value] = Equal


@dataclasses.dataclass
class NotEqual(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.ne.html
    """

    type: str = dataclasses.field(default=ExprEnum.ne.value)
    left: "OtherExpr" = dataclasses.field(default=REQUIRED)
    right: "OtherExpr" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=to_jsonpolars_other_expr(dct["left"]),
            right=to_jsonpolars_other_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return _other_expr_to_polars(self.left) != _other_expr_to_polars(self.right)


expr_enum_to_klass_mapping[ExprEnum.ne.value] = NotEqual


@dataclasses.dataclass
class GreatThan(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.gt.html
    """

    type: str = dataclasses.field(default=ExprEnum.gt.value)
    left: "OtherExpr" = dataclasses.field(default=REQUIRED)
    right: "OtherExpr" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=to_jsonpolars_other_expr(dct["left"]),
            right=to_jsonpolars_other_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return _other_expr_to_polars(self.left) > _other_expr_to_polars(self.right)


expr_enum_to_klass_mapping[ExprEnum.gt.value] = GreatThan


@dataclasses.dataclass
class GreatThanOrEqual(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.ge.html
    """

    type: str = dataclasses.field(default=ExprEnum.ge.value)
    left: "OtherExpr" = dataclasses.field(default=REQUIRED)
    right: "OtherExpr" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=to_jsonpolars_other_expr(dct["left"]),
            right=to_jsonpolars_other_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return _other_expr_to_polars(self.left) >= _other_expr_to_polars(self.right)


expr_enum_to_klass_mapping[ExprEnum.ge.value] = GreatThanOrEqual


@dataclasses.dataclass
class LessThan(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.lt.html
    """

    type: str = dataclasses.field(default=ExprEnum.lt.value)
    left: "OtherExpr" = dataclasses.field(default=REQUIRED)
    right: "OtherExpr" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=to_jsonpolars_other_expr(dct["left"]),
            right=to_jsonpolars_other_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return _other_expr_to_polars(self.left) < _other_expr_to_polars(self.right)


expr_enum_to_klass_mapping[ExprEnum.lt.value] = LessThan


@dataclasses.dataclass
class LessThanOrEqual(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.le.html
    """

    type: str = dataclasses.field(default=ExprEnum.le.value)
    left: "OtherExpr" = dataclasses.field(default=REQUIRED)
    right: "OtherExpr" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=to_jsonpolars_other_expr(dct["left"]),
            right=to_jsonpolars_other_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return _other_expr_to_polars(self.left) <= _other_expr_to_polars(self.right)


expr_enum_to_klass_mapping[ExprEnum.le.value] = LessThanOrEqual


@dataclasses.dataclass
class LogicalAnd(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.and_.html
    """

    type: str = dataclasses.field(default=ExprEnum.and_.value)
    left: "OtherExpr" = dataclasses.field(default=REQUIRED)
    right: "OtherExpr" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=to_jsonpolars_other_expr(dct["left"]),
            right=to_jsonpolars_other_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return _other_expr_to_polars(self.left) & _other_expr_to_polars(self.right)


expr_enum_to_klass_mapping[ExprEnum.and_.value] = LogicalAnd


@dataclasses.dataclass
class LogicalOr(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.or_.html
    """

    type: str = dataclasses.field(default=ExprEnum.or_.value)
    left: "OtherExpr" = dataclasses.field(default=REQUIRED)
    right: "OtherExpr" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=to_jsonpolars_other_expr(dct["left"]),
            right=to_jsonpolars_other_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return _other_expr_to_polars(self.left) | _other_expr_to_polars(self.right)


expr_enum_to_klass_mapping[ExprEnum.or_.value] = LogicalOr
