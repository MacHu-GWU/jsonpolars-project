# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..arg import REQ, NA, rm_na, T_KWARGS
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr
from ..utils_expr import str_to_polars_dtype_mapping, polars_dtype_to_str_mapping

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR


@dataclasses.dataclass
class Cast(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.cast.html
    """

    type: str = dataclasses.field(default=ExprEnum.cast.value)
    expr: "T_EXPR" = dataclasses.field(default=REQ)
    dtype: T.Union[str, "pl.DataType", T.Type["pl.DataType"]] = dataclasses.field(
        default=REQ
    )

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

    @classmethod
    def from_dict(cls, dct: T_KWARGS):
        req_kwargs, opt_kwargs = cls._split_req_opt(dct)
        req_kwargs["expr"] = parse_expr(req_kwargs["expr"])
        return cls(**req_kwargs, **rm_na(**opt_kwargs))

    def to_polars(self) -> pl.Expr:
        if isinstance(self.dtype, str):
            dtype = str_to_polars_dtype_mapping[self.dtype]
        else:
            dtype = self.dtype
        return self.expr.to_polars().cast(dtype)


expr_enum_to_klass_mapping[ExprEnum.cast.value] = Cast
