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
