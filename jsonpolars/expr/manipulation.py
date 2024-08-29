# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr
from ..utils_expr import str_to_polars_dtype_mapping

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR


@dataclasses.dataclass
class Cast(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.cast.html
    """

    type: str = dataclasses.field(default=ExprEnum.cast.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    dtype: str = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            dtype=dct["dtype"],
        )

    def to_polars(self) -> pl.Expr:
        return self.expr.to_polars().cast(str_to_polars_dtype_mapping[self.dtype])


expr_enum_to_klass_mapping[ExprEnum.cast.value] = Cast
