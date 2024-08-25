# -*- coding: utf-8 -*-

"""
Module for type hints.

See https://github.com/pola-rs/polars/blob/main/py-polars/polars/_typing.py
"""

try:
    import typing_extensions as T
except ImportError:  # pragma: no cover
    import typing as T

if T.TYPE_CHECKING:
    from datetime import date, datetime, time, timedelta
    from decimal import Decimal

    from .expr.api import T_EXPR
    from .dfop.api import T_DFOP

# fmt: off

NumericLiteral: T.TypeAlias = T.Union[int, float, "Decimal"]
TemporalLiteral: T.TypeAlias = T.Union["date", "time", "datetime", "timedelta"]
NonNestedLiteral: T.TypeAlias = T.Union[NumericLiteral, TemporalLiteral, str, bool, bytes]
# Python literal types (can convert into a `lit` expression)
PythonLiteral: T.TypeAlias = T.Union[NonNestedLiteral, T.List[T.Any]]
# Inputs that can convert into a `col` expression
IntoExprColumn: T.TypeAlias = T.Union["T_EXPR", str]
# Inputs that can convert into an expression
IntoExpr: T.TypeAlias = T.Union[PythonLiteral, "T_EXPR", None]
# Inputs that can be interactive with +, -, *, /, etc.
OtherExpr: T.TypeAlias = T.Union[PythonLiteral, "T_EXPR"]

# selector type, and related collection/sequence
ColumnNameOrSelector: T.TypeAlias = T.Union[str, "T_EXPR"]

# fmt: on
