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
    to_jsonpolars_other_expr,
    to_polars_other_expr,
)

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR
    from ..typehint import IntoExpr


def ensure_struct(expr: "T_EXPR") -> pl.Expr:
    if isinstance(expr, Struct):
        return expr.to_polars()
    else:
        return expr.to_polars().struct


@dataclasses.dataclass
class Struct(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/struct.html
    """

    type: str = dataclasses.field(default=ExprEnum.struct.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_struct(self.expr)


expr_enum_to_klass_mapping[ExprEnum.struct.value] = Struct


@dataclasses.dataclass
class StructField(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.struct.field.html
    """

    type: str = dataclasses.field(default=ExprEnum.struct_field.value)
    expr: T.Optional["T_EXPR"] = dataclasses.field(default=None)
    name: T.Union[str, T.List[str]] = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):

        return cls(
            expr=to_jsonpolars_other_expr(dct["expr"]),
            name=dct["name"],
        )

    def to_polars(self) -> pl.Expr:
        if self.expr is None:
            if isinstance(self.name, str):
                return pl.field(self.name)
            else:  # pragma: no cover
                raise TypeError("name must be a string if expr is None")
        else:
            expr = ensure_struct(self.expr)

        if isinstance(self.name, str):
            name = [self.name]
        else:
            name = self.name

        return expr.field(*name)


expr_enum_to_klass_mapping[ExprEnum.struct_field.value] = StructField


@dataclasses.dataclass
class StructRenameFields(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.struct.rename_fields.html
    """

    type: str = dataclasses.field(default=ExprEnum.struct_rename_fields.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    names: T.List[str] = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            names=dct["names"],
        )

    def to_polars(self) -> pl.Expr:
        return ensure_struct(self.expr).rename_fields(names=self.names)


expr_enum_to_klass_mapping[ExprEnum.struct_rename_fields.value] = StructRenameFields


@dataclasses.dataclass
class StructWithFields(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.struct.with_fields.html
    """

    type: str = dataclasses.field(default=ExprEnum.struct_with_fields.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    exprs: T.List["IntoExpr"] = dataclasses.field(default_factory=list)
    named_exprs: T.Dict[str, "IntoExpr"] = dataclasses.field(default_factory=dict)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            exprs=batch_to_jsonpolars_into_exprs(dct["exprs"]),
            named_exprs=batch_to_jsonpolars_named_into_exprs(dct["named_exprs"]),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_struct(self.expr).with_fields(
            *batch_to_polars_into_exprs(self.exprs),
            **batch_to_polars_named_into_exprs(self.named_exprs),
        )


expr_enum_to_klass_mapping[ExprEnum.struct_with_fields.value] = StructWithFields
