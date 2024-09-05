# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..arg import REQ, NA, rm_na, T_KWARGS
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
    expr: "T_EXPR" = dataclasses.field(default=REQ)

    @classmethod
    def from_dict(cls, dct: T_KWARGS):
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
    name: T.Union[str, T.List[str]] = dataclasses.field(default=REQ)
    more_names: T.List[str] = dataclasses.field(default_factory=list)

    @classmethod
    def from_dict(cls, dct: T_KWARGS):
        kwargs = dict(
            name=dct["name"],
            more_names=dct.get("more_names", []),
        )
        expr = dct["expr"]
        if expr is not None:
            kwargs["expr"] = to_jsonpolars_other_expr(dct["expr"])
        return cls(**kwargs)

    def to_polars(self) -> pl.Expr:
        if self.expr is None:
            if isinstance(self.name, str):
                return pl.field(self.name, *self.more_names)
            else:  # pragma: no cover
                raise TypeError("name must be a string if expr is None")
        else:
            expr = ensure_struct(self.expr)

        return expr.field(self.name, *self.more_names)


expr_enum_to_klass_mapping[ExprEnum.struct_field.value] = StructField


@dataclasses.dataclass
class StructRenameFields(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.struct.rename_fields.html
    """

    type: str = dataclasses.field(default=ExprEnum.struct_rename_fields.value)
    expr: "T_EXPR" = dataclasses.field(default=REQ)
    names: T.List[str] = dataclasses.field(default=REQ)

    @classmethod
    def from_dict(cls, dct: T_KWARGS):
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
    expr: "T_EXPR" = dataclasses.field(default=REQ)
    exprs: T.List["IntoExpr"] = dataclasses.field(default_factory=list)
    named_exprs: T.Dict[str, "IntoExpr"] = dataclasses.field(default_factory=dict)

    @classmethod
    def from_dict(cls, dct: T_KWARGS):
        return cls(
            expr=parse_expr(dct["expr"]),
            exprs=batch_to_jsonpolars_into_exprs(dct.get("exprs", list())),
            named_exprs=batch_to_jsonpolars_named_into_exprs(
                dct.get("named_exprs", dict())
            ),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_struct(self.expr).with_fields(
            *batch_to_polars_into_exprs(self.exprs),
            **batch_to_polars_named_into_exprs(self.named_exprs),
        )


expr_enum_to_klass_mapping[ExprEnum.struct_with_fields.value] = StructWithFields
