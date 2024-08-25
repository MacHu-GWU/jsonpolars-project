# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr
from ..utils_expr import parse_other_expr, other_expr_to_polars

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR


def ensure_string(expr: "T_EXPR") -> pl.Expr:
    if isinstance(expr, String):
        return expr.to_polars()
    else:
        return expr.to_polars().str


@dataclasses.dataclass
class String(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/string.html
    """

    type: str = dataclasses.field(default=ExprEnum.string.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr)


expr_enum_to_klass_mapping[ExprEnum.string.value] = String


@dataclasses.dataclass
class Split(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.split.html
    """

    type: str = dataclasses.field(default=ExprEnum.str_split.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    by: str = dataclasses.field(default=REQUIRED)
    inclusive: bool = dataclasses.field(default=False)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            by=dct["by"],
            inclusive=dct["inclusive"],
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).split(by=self.by, inclusive=self.inclusive)


expr_enum_to_klass_mapping[ExprEnum.str_split.value] = Split


@dataclasses.dataclass
class StrJoin(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.join.html
    """

    type: str = dataclasses.field(default=ExprEnum.str_join.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    delimiter: str = dataclasses.field(default="")
    ignore_nulls: bool = dataclasses.field(default=True)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            delimiter=dct.get("delimiter", ""),
            ignore_nulls=dct.get("ignore_nulls", True),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).join(
            delimiter=self.delimiter,
            ignore_nulls=self.ignore_nulls,
        )


expr_enum_to_klass_mapping[ExprEnum.str_join.value] = StrJoin


@dataclasses.dataclass
class StrContains(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.contains.html
    """

    type: str = dataclasses.field(default=ExprEnum.str_contains.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    pattern: T.Union[str, "T_EXPR"] = dataclasses.field(default=REQUIRED)
    literal: bool = dataclasses.field(default=False)
    strict: bool = dataclasses.field(default=True)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            pattern=parse_other_expr(dct["pattern"]),
            literal=dct["literal"],
            strict=dct["strict"],
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).contains(
            pattern=other_expr_to_polars(self.pattern),
            literal=self.literal,
            strict=self.strict,
        )


expr_enum_to_klass_mapping[ExprEnum.str_contains.value] = StrContains


@dataclasses.dataclass
class StrDecode(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.decode.html
    """

    type: str = dataclasses.field(default=ExprEnum.str_decode.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    encoding: str = dataclasses.field(default=REQUIRED)
    strict: bool = dataclasses.field(default=True)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            encoding=dct["encoding"],
            strict=dct["strict"],
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).decode(
            encoding=self.encoding,
            strict=self.strict,
        )


expr_enum_to_klass_mapping[ExprEnum.str_decode.value] = StrDecode


@dataclasses.dataclass
class StrEncode(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.encode.html
    """

    type: str = dataclasses.field(default=ExprEnum.str_encode.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    encoding: str = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            encoding=dct["encoding"],
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).encode(encoding=self.encoding)


expr_enum_to_klass_mapping[ExprEnum.str_encode.value] = StrEncode


@dataclasses.dataclass
class StrStartsWith(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.starts_with.html
    """

    type: str = dataclasses.field(default=ExprEnum.str_starts_with.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    prefix: T.Union[str, "T_EXPR"] = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            prefix=parse_other_expr(dct["prefix"]),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).starts_with(
            prefix=other_expr_to_polars(self.prefix)
        )


expr_enum_to_klass_mapping[ExprEnum.str_starts_with.value] = StrStartsWith


@dataclasses.dataclass
class StrEndsWith(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.ends_with.html
    """

    type: str = dataclasses.field(default=ExprEnum.str_ends_with.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    suffix: T.Union[str, "T_EXPR"] = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            suffix=parse_other_expr(dct["suffix"]),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).ends_with(
            suffix=other_expr_to_polars(self.suffix)
        )


expr_enum_to_klass_mapping[ExprEnum.str_ends_with.value] = StrEndsWith
