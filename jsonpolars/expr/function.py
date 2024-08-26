# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr
from ..utils_expr import (
    batch_to_jsonpolars_into_exprs,
    batch_to_jsonpolars_named_into_exprs,
    batch_to_polars_into_exprs,
    batch_to_polars_named_into_exprs,
)
from ..vendor.better_dataclasses import T_DATA_LIKE

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR
    from ..typehint import IntoExpr


@dataclasses.dataclass
class Lit(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.lit.html
    """

    type: str = dataclasses.field(default=ExprEnum.func_lit.value)
    value: T.Any = dataclasses.field(default=REQUIRED)
    dtype: T.Optional["pl.DataType"] = dataclasses.field(default=None)
    allow_object: bool = dataclasses.field(default=False)

    def to_polars(self) -> pl.Expr:
        return pl.lit(
            value=self.value,
            dtype=self.dtype,
            allow_object=self.allow_object,
        )


expr_enum_to_klass_mapping[ExprEnum.func_lit.value] = Lit


@dataclasses.dataclass
class ConcatStr(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.concat_str.html
    """

    type: str = dataclasses.field(default=ExprEnum.func_concat_str.value)
    exprs: T.List["IntoExpr"] = dataclasses.field(default_factory=list)
    separator: str = dataclasses.field(default=" ")
    ignore_nulls: bool = dataclasses.field(default=False)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            exprs=batch_to_jsonpolars_into_exprs(dct["exprs"]),
            separator=dct["separator"],
            ignore_nulls=dct["ignore_nulls"],
        )

    def to_polars(self) -> pl.Expr:
        return pl.concat_str(
            exprs=batch_to_polars_into_exprs(self.exprs),
            separator=self.separator,
            ignore_nulls=self.ignore_nulls,
        )


expr_enum_to_klass_mapping[ExprEnum.func_concat_str.value] = ConcatStr


@dataclasses.dataclass
class ConcatList(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.concat_list.html
    """

    type: str = dataclasses.field(default=ExprEnum.func_concat_list.value)
    exprs: T.List["IntoExpr"] = dataclasses.field(default_factory=list)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            exprs=batch_to_jsonpolars_into_exprs(dct["exprs"]),
        )

    def to_polars(self) -> pl.Expr:
        return pl.concat_list(
            exprs=batch_to_polars_into_exprs(self.exprs),
        )


expr_enum_to_klass_mapping[ExprEnum.func_concat_list.value] = ConcatList
