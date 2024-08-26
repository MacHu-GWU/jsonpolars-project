# -*- coding: utf-8 -*-

"""
这个模块中有一系列的用于 serde 的函数.

- 凡是以 ``to_jsonpolars`` 开头的函数都是用于将不同的 Python 数据结构转化成类 BaseExpr 对象.
- 凡是以 ``to_polars`` 开头的函数都是用于将不同的 Python Literal 和 BaseExpr 对象转化为 polars Expr 对象.
"""

import typing as T
import polars as pl

from .base_expr import BaseExpr, parse_expr
from .typehint import (
    PythonLiteral,
    IntoExpr,
    OtherExpr,
)


if T.TYPE_CHECKING:  # pragma: no cover
    from .expr.api import T_EXPR


def to_jsonpolars_into_expr(
    expr_like: T.Union[str, dict, "T_EXPR"],
) -> "IntoExpr":
    if isinstance(expr_like, str):
        return expr_like
    elif isinstance(expr_like, dict):
        return parse_expr(expr_like)
    elif isinstance(expr_like, BaseExpr):
        return expr_like
    else:  # pragma: no cover
        raise NotImplementedError(f"Unsupported type: {type(expr_like)}")


def to_polars_into_expr(
    expr_like: T.Union[str, "T_EXPR"],
) -> T.Union[str, "pl.Expr"]:
    if isinstance(expr_like, BaseExpr):
        return expr_like.to_polars()
    else:  # pragma: no cover
        return expr_like


def batch_to_jsonpolars_into_exprs(
    exprs: T.Iterable[T.Union[str, dict, "T_EXPR"]],
) -> T.List["IntoExpr"]:
    """
    .. note::

        Intentionally not using list comprehension here. So that it tells you
        which expression is causing the error.
    """
    new_exprs = list()
    for ex in exprs:
        new_exprs.append(to_jsonpolars_into_expr(ex))
    return new_exprs


def batch_to_jsonpolars_named_into_exprs(
    named_exprs: T.Dict[str, T.Union[str, dict, "T_EXPR"]],
) -> T.Dict[str, "IntoExpr"]:
    """
    .. note::

        Intentionally not using list comprehension here. So that it tells you
        which expression is causing the error.
    """
    new_named_exprs = dict()
    for name, ex in named_exprs.items():
        new_named_exprs[name] = to_jsonpolars_into_expr(ex)
    return new_named_exprs


def batch_to_polars_into_exprs(
    exprs: T.Iterable[T.Union[str, "T_EXPR"]],
) -> T.List[T.Union[str, "pl.Expr"]]:
    """
    .. note::

        Intentionally not using list comprehension here. So that it tells you
        which expression is causing the error.
    """
    new_exprs = list()
    for ex in exprs:
        new_exprs.append(to_polars_into_expr(ex))
    return new_exprs


def batch_to_polars_named_into_exprs(
    named_exprs: T.Dict[str, T.Union[str, "T_EXPR"]],
) -> T.Dict[str, T.Union[str, "pl.Expr"]]:
    """
    .. note::

        Intentionally not using list comprehension here. So that it tells you
        which expression is causing the error.
    """
    new_named_exprs = dict()
    for name, ex in named_exprs.items():
        new_named_exprs[name] = to_polars_into_expr(ex)
    return new_named_exprs


def to_jsonpolars_other_expr(
    expr_like: T.Union["PythonLiteral", dict, "T_EXPR"]
) -> "OtherExpr":
    if isinstance(expr_like, dict):
        return parse_expr(expr_like)
    else:
        return expr_like


def to_polars_other_expr(
    expr_like: "OtherExpr",
) -> T.Union["PythonLiteral", "pl.Expr"]:
    if isinstance(expr_like, BaseExpr):
        return expr_like.to_polars()
    else:
        return expr_like
