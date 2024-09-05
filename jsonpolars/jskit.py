# -*- coding: utf-8 -*-

"""
JSON kits, a collection of syntax sugar utilities functions.
"""

import typing as T

from .expr import api as expr
from .chain import chain, PRE

if T.TYPE_CHECKING:  # pragma: no cover
    from .expr.api import T_EXPR


def dot_field(
    col: str,
    nodes: T.List[str] = None,
    alias: str = None,
) -> "T_EXPR":
    ex = expr.Column(name=col)
    if nodes is None:
        nodes = []
    for node in nodes:
        ex = expr.StructField(expr=ex, name=node)
    if alias is not None:
        ex = expr.Alias(expr=ex, name=alias)
    return ex
