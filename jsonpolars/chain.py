# -*- coding: utf-8 -*-

import typing as T
from .arg import PRE


if T.TYPE_CHECKING:  # pragma: no cover
    from .expr.api import T_EXPR


_ = PRE


def chain(*args: "T_EXPR") -> "T_EXPR":
    ex = None
    for arg in args:
        # print(ex, arg)
        if ex is not None:
            setattr(arg, "expr", ex)
        ex = arg
    # print(ex)
    return ex
