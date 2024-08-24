# -*- coding: utf-8 -*-

import typing as T
import polars as pl

from ..base_expr import BaseExpr, parse_expr
from ..typehint import IntoExpr


if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR


def to_jsonpolars_into_expr(expr_like: T.Union[str, dict, "T_EXPR"]) -> IntoExpr:
    if isinstance(expr_like, str):
        return expr_like
    elif isinstance(expr_like, dict):
        return parse_expr(expr_like)
    elif isinstance(expr_like, BaseExpr):
        return expr_like
    else:  # pragma: no cover
        raise NotImplementedError(f"Unsupported type: {type(expr_like)}")


def to_polars_into_expr(expr_like: T.Union[T.Any, "T_EXPR"]):
    if isinstance(expr_like, BaseExpr):
        return expr_like.to_polars()
    else:  # pragma: no cover
        return expr_like
