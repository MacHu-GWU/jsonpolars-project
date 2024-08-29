# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL, resolve_kwargs
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr
from ..utils_expr import to_jsonpolars_other_expr, to_polars_other_expr

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
            **resolve_kwargs(
                expr=parse_expr(dct["expr"]),
            )
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
            **resolve_kwargs(
                by=dct.get("by", NOTHING),
                inclusive=dct.get("inclusive", NOTHING),
            ),
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
            **resolve_kwargs(
                delimiter=dct.get("delimiter", NOTHING),
                ignore_nulls=dct.get("ignore_nulls", NOTHING),
            ),
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
            pattern=to_jsonpolars_other_expr(dct["pattern"]),
            **resolve_kwargs(
                literal=dct.get("literal", NOTHING),
                strict=dct.get("strict", NOTHING),
            ),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).contains(
            pattern=to_polars_other_expr(self.pattern),
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
            **resolve_kwargs(
                strict=dct.get("strict", NOTHING),
            ),
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
            prefix=to_jsonpolars_other_expr(dct["prefix"]),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).starts_with(
            prefix=to_polars_other_expr(self.prefix)
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
            suffix=to_jsonpolars_other_expr(dct["suffix"]),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).ends_with(
            suffix=to_polars_other_expr(self.suffix)
        )


expr_enum_to_klass_mapping[ExprEnum.str_ends_with.value] = StrEndsWith


@dataclasses.dataclass
class StrToDatetime(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.to_datetime.html
    """

    type: str = dataclasses.field(default=ExprEnum.str_to_datetime.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    format: T.Optional[str] = dataclasses.field(default=None)
    time_unit: T.Optional[str] = dataclasses.field(default=None)
    time_zone: T.Optional[str] = dataclasses.field(default=None)
    strict: bool = dataclasses.field(default=True)
    exact: bool = dataclasses.field(default=True)
    cache: bool = dataclasses.field(default=True)
    ambiguous: str = dataclasses.field(default="raise")

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            **resolve_kwargs(
                format=dct.get("format", NOTHING),
                time_unit=dct.get("time_unit", NOTHING),
                time_zone=dct.get("time_zone", NOTHING),
                strict=dct.get("strict", NOTHING),
                exact=dct.get("exact", NOTHING),
                cache=dct.get("cache", NOTHING),
                ambiguous=dct.get("ambiguous", NOTHING),
            ),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).to_datetime(
            format=self.format,
            time_unit=self.time_unit,
            time_zone=self.time_zone,
            strict=self.strict,
            exact=self.exact,
            cache=self.cache,
            ambiguous=self.ambiguous,
        )


expr_enum_to_klass_mapping[ExprEnum.str_to_datetime.value] = StrToDatetime


@dataclasses.dataclass
class StrToDate(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.to_date.html
    """

    type: str = dataclasses.field(default=ExprEnum.str_to_date.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    format: T.Optional[str] = dataclasses.field(default=None)
    strict: bool = dataclasses.field(default=True)
    exact: bool = dataclasses.field(default=True)
    cache: bool = dataclasses.field(default=True)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            **resolve_kwargs(
                format=dct.get("format", NOTHING),
                strict=dct.get("strict", NOTHING),
                exact=dct.get("exact", NOTHING),
                cache=dct.get("cache", NOTHING),
            ),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).to_date(
            format=self.format,
            strict=self.strict,
            exact=self.exact,
            cache=self.cache,
        )


expr_enum_to_klass_mapping[ExprEnum.str_to_date.value] = StrToDate


@dataclasses.dataclass
class StrZfill(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.zfill.html
    """

    type: str = dataclasses.field(default=ExprEnum.str_zfill.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    length: int = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            length=dct["length"],
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).zfill(length=self.length)


expr_enum_to_klass_mapping[ExprEnum.str_zfill.value] = StrZfill


@dataclasses.dataclass
class StrPadStart(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.pad_start.html
    """

    type: str = dataclasses.field(default=ExprEnum.str_pad_start.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    length: int = dataclasses.field(default=REQUIRED)
    fill_char: str = dataclasses.field(default=" ")

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            length=dct["length"],
            **resolve_kwargs(
                fill_char=dct.get("fill_char", NOTHING),
            ),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).pad_start(
            length=self.length,
            fill_char=self.fill_char,
        )


expr_enum_to_klass_mapping[ExprEnum.str_pad_start.value] = StrPadStart


@dataclasses.dataclass
class StrPadEnd(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.pad_end.html
    """

    type: str = dataclasses.field(default=ExprEnum.str_pad_end.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    length: int = dataclasses.field(default=REQUIRED)
    fill_char: str = dataclasses.field(default=" ")

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            length=dct["length"],
            **resolve_kwargs(
                fill_char=dct.get("fill_char", NOTHING),
            ),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).pad_end(
            length=self.length,
            fill_char=self.fill_char,
        )


expr_enum_to_klass_mapping[ExprEnum.str_pad_end.value] = StrPadEnd


@dataclasses.dataclass
class StrToLowerCase(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.to_lowercase.html
    """

    type: str = dataclasses.field(default=ExprEnum.str_to_lowercase.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).to_lowercase()


expr_enum_to_klass_mapping[ExprEnum.str_to_lowercase.value] = StrToLowerCase


@dataclasses.dataclass
class StrToUpperCase(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.to_uppercase.html
    """

    type: str = dataclasses.field(default=ExprEnum.str_to_uppercase.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).to_uppercase()


expr_enum_to_klass_mapping[ExprEnum.str_to_uppercase.value] = StrToUpperCase


@dataclasses.dataclass
class StrToTitleCase(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.to_titlecase.html
    """

    type: str = dataclasses.field(default=ExprEnum.str_to_titlecase.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).to_titlecase()


expr_enum_to_klass_mapping[ExprEnum.str_to_titlecase.value] = StrToTitleCase


@dataclasses.dataclass
class StrHead(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.head.html
    """

    type: str = dataclasses.field(default=ExprEnum.str_head.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    n: int = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            n=dct["n"],
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).head(n=self.n)


expr_enum_to_klass_mapping[ExprEnum.str_head.value] = StrHead


@dataclasses.dataclass
class StrTail(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.tail.html
    """

    type: str = dataclasses.field(default=ExprEnum.str_tail.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    n: int = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            n=dct["n"],
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).tail(n=self.n)


expr_enum_to_klass_mapping[ExprEnum.str_tail.value] = StrTail


@dataclasses.dataclass
class StrSlice(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.slice.html
    """

    type: str = dataclasses.field(default=ExprEnum.str_slice.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    offset: int = dataclasses.field(default=REQUIRED)
    length: int = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            offset=dct["offset"],
            length=dct["length"],
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).slice(
            offset=self.offset,
            length=self.length,
        )


expr_enum_to_klass_mapping[ExprEnum.str_slice.value] = StrSlice


@dataclasses.dataclass
class StrReplace(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.replace.html
    """

    type: str = dataclasses.field(default=ExprEnum.str_replace.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    pattern: T.Union[str, "T_EXPR"] = dataclasses.field(default=REQUIRED)
    value: T.Union[str, "T_EXPR"] = dataclasses.field(default=REQUIRED)
    literal: bool = dataclasses.field(default=False)
    n: int = dataclasses.field(default=1)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            pattern=to_jsonpolars_other_expr(dct["pattern"]),
            value=to_jsonpolars_other_expr(dct["value"]),
            **resolve_kwargs(
                literal=dct.get("literal", NOTHING),
                n=dct.get("n", NOTHING),
            ),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).replace(
            pattern=to_polars_other_expr(self.pattern),
            value=to_polars_other_expr(self.value),
            literal=self.literal,
            n=self.n,
        )


expr_enum_to_klass_mapping[ExprEnum.str_replace.value] = StrReplace


@dataclasses.dataclass
class StrReplaceAll(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.replace_all.html
    """

    type: str = dataclasses.field(default=ExprEnum.str_replace_all.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    pattern: T.Union[str, "T_EXPR"] = dataclasses.field(default=REQUIRED)
    value: T.Union[str, "T_EXPR"] = dataclasses.field(default=REQUIRED)
    literal: bool = dataclasses.field(default=False)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            pattern=to_jsonpolars_other_expr(dct["pattern"]),
            value=to_jsonpolars_other_expr(dct["value"]),
            **resolve_kwargs(
                literal=dct.get("literal", NOTHING),
            ),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr).replace_all(
            pattern=to_polars_other_expr(self.pattern),
            value=to_polars_other_expr(self.value),
            literal=self.literal,
        )


expr_enum_to_klass_mapping[ExprEnum.str_replace_all.value] = StrReplaceAll
