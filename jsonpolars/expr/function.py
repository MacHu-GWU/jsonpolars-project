# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl
from simpletype.api import json_type_to_simple_type

from ..arg import REQ, NA, rm_na, T_KWARGS
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr
from ..utils_expr import (
    batch_to_jsonpolars_into_exprs,
    batch_to_jsonpolars_named_into_exprs,
    batch_to_polars_into_exprs,
    batch_to_polars_named_into_exprs,
    to_jsonpolars_other_expr,
    str_to_polars_dtype_mapping,
    polars_dtype_to_str_mapping,
)

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR
    from ..typehint import IntoExpr, DatetimeElementExpr


@dataclasses.dataclass
class Lit(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.lit.html
    """

    type: str = dataclasses.field(default=ExprEnum.func_lit.value)
    value: T.Any = dataclasses.field(default=REQ)
    dtype: T.Union[str, "pl.DataType", T.Type["pl.DataType"]] = dataclasses.field(
        default=NA
    )
    allow_object: bool = dataclasses.field(default=NA)

    def to_dict(self) -> T_KWARGS:
        dct = super().to_dict()
        if "dtype" in dct:
            if isinstance(self.dtype, str):
                dtype = self.dtype
            else:
                try:
                    dtype = polars_dtype_to_str_mapping[type(self.dtype)]
                except KeyError:
                    dtype = polars_dtype_to_str_mapping[self.dtype]
            dct["dtype"] = dtype
        return dct

    def to_polars(self) -> pl.Expr:
        if isinstance(self.dtype, str):
            dtype = str_to_polars_dtype_mapping[self.dtype]
        else:
            dtype = self.dtype
        return pl.lit(
            value=self.value,
            **rm_na(
                dtype=dtype,
                allow_object=self.allow_object,
            ),
        )


expr_enum_to_klass_mapping[ExprEnum.func_lit.value] = Lit


@dataclasses.dataclass
class ConcatStr(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.concat_str.html
    """

    type: str = dataclasses.field(default=ExprEnum.func_concat_str.value)
    exprs: T.List["IntoExpr"] = dataclasses.field(default_factory=list)
    separator: str = dataclasses.field(default=NA)
    ignore_nulls: bool = dataclasses.field(default=NA)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        req_kwargs, opt_kwargs = cls._split_req_opt(dct)
        opt_kwargs["exprs"] = batch_to_jsonpolars_into_exprs(
            opt_kwargs.get("exprs", [])
        )
        return cls(**req_kwargs, **rm_na(**opt_kwargs))

    def to_polars(self) -> pl.Expr:
        return pl.concat_str(
            exprs=batch_to_polars_into_exprs(self.exprs),
            **rm_na(
                separator=self.separator,
                ignore_nulls=self.ignore_nulls,
            ),
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
            exprs=batch_to_jsonpolars_into_exprs(dct.get("exprs", list())),
        )

    def to_polars(self) -> pl.Expr:
        return pl.concat_list(
            exprs=batch_to_polars_into_exprs(self.exprs),
        )


expr_enum_to_klass_mapping[ExprEnum.func_concat_list.value] = ConcatList


@dataclasses.dataclass
class FuncStruct(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.struct.html
    """

    type: str = dataclasses.field(default=ExprEnum.func_struct.value)
    exprs: T.List["IntoExpr"] = dataclasses.field(default_factory=list)
    named_exprs: T.Dict[str, "IntoExpr"] = dataclasses.field(default_factory=dict)
    schema: T.Optional[T.Dict[str, T.Dict[str, T.Any]]] = dataclasses.field(default=NA)
    eager: bool = dataclasses.field(default=NA)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        req_kwargs, opt_kwargs = cls._split_req_opt(dct)
        opt_kwargs["exprs"] = batch_to_jsonpolars_into_exprs(
            opt_kwargs.get("exprs", [])
        )
        opt_kwargs["named_exprs"] = batch_to_jsonpolars_named_into_exprs(
            opt_kwargs.get("named_exprs", {})
        )
        return cls(**req_kwargs, **rm_na(**opt_kwargs))

    def to_polars(self) -> pl.Expr:
        kwargs = {}
        if isinstance(self.schema, dict):
            kwargs["schema"] = {
                k: json_type_to_simple_type(v).to_polars()
                for k, v in self.schema.items()
            }
        return pl.struct(
            *batch_to_polars_into_exprs(self.exprs),
            **batch_to_polars_named_into_exprs(self.named_exprs),
            **rm_na(eager=self.eager, **kwargs),
        )


expr_enum_to_klass_mapping[ExprEnum.func_struct.value] = FuncStruct


@dataclasses.dataclass
class Format(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.format.html
    """

    type: str = dataclasses.field(default=ExprEnum.func_format.value)
    f_string: str = dataclasses.field(default=REQ)
    exprs: T.List["IntoExpr"] = dataclasses.field(default_factory=list)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        req_kwargs, opt_kwargs = cls._split_req_opt(dct)
        opt_kwargs["exprs"] = batch_to_jsonpolars_into_exprs(
            opt_kwargs.get("exprs", [])
        )
        return cls(**req_kwargs, **rm_na(**opt_kwargs))

    def to_polars(self) -> pl.Expr:
        return pl.format(
            self.f_string,
            *batch_to_polars_into_exprs(self.exprs),
        )


expr_enum_to_klass_mapping[ExprEnum.func_format.value] = Format


@dataclasses.dataclass
class FuncDate(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.date.html
    """

    type: str = dataclasses.field(default=ExprEnum.func_date.value)
    year: "DatetimeElementExpr" = dataclasses.field(default=REQ)
    month: "DatetimeElementExpr" = dataclasses.field(default=REQ)
    day: "DatetimeElementExpr" = dataclasses.field(default=REQ)

    def to_polars(self) -> pl.Expr:
        return pl.date(
            year=self.year,
            month=self.month,
            day=self.day,
        )


expr_enum_to_klass_mapping[ExprEnum.func_date.value] = FuncDate


@dataclasses.dataclass
class FuncDatetime(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.datetime.html
    """

    type: str = dataclasses.field(default=ExprEnum.func_datetime.value)
    year: "DatetimeElementExpr" = dataclasses.field(default=REQ)
    month: "DatetimeElementExpr" = dataclasses.field(default=REQ)
    day: "DatetimeElementExpr" = dataclasses.field(default=REQ)
    hour: "DatetimeElementExpr" = dataclasses.field(default=NA)
    minute: "DatetimeElementExpr" = dataclasses.field(default=NA)
    second: "DatetimeElementExpr" = dataclasses.field(default=NA)
    microsecond: "DatetimeElementExpr" = dataclasses.field(default=NA)
    time_unit: str = dataclasses.field(default=NA)
    time_zone: T.Optional[str] = dataclasses.field(default=NA)
    ambiguous: str = dataclasses.field(default=NA)

    def to_polars(self) -> pl.Expr:
        return pl.datetime(
            year=self.year,
            month=self.month,
            day=self.day,
            **rm_na(
                hour=self.hour,
                minute=self.minute,
                second=self.second,
                microsecond=self.microsecond,
                time_unit=self.time_unit,
                time_zone=self.time_zone,
                ambiguous=self.ambiguous,
            ),
        )


expr_enum_to_klass_mapping[ExprEnum.func_datetime.value] = FuncDatetime


@dataclasses.dataclass
class Element(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.element.html
    """

    type: str = dataclasses.field(default=ExprEnum.func_element.value)

    def to_polars(self) -> pl.Expr:
        return pl.element()


expr_enum_to_klass_mapping[ExprEnum.func_element.value] = Element
