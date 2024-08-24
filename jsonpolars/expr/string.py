# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR


@dataclasses.dataclass
class String(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.string.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=expr_enum_to_klass_mapping[dct["expr"]["type"]].from_dict(dct["expr"]),
        )

    def to_polars(self) -> pl.Expr:
        return self.expr.to_polars().str


expr_enum_to_klass_mapping[ExprEnum.string.value] = String


@dataclasses.dataclass
class Split(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.split.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    by: str = dataclasses.field(default=REQUIRED)
    inclusive: bool = dataclasses.field(default=False)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=expr_enum_to_klass_mapping[dct["expr"]["type"]].from_dict(dct["expr"]),
            by=dct["by"],
            inclusive=dct["inclusive"],
        )

    def to_polars(self) -> pl.Expr:
        return self.expr.to_polars().split(by=self.by, inclusive=self.inclusive)


expr_enum_to_klass_mapping[ExprEnum.split.value] = Split
