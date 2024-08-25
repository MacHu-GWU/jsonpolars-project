# -*- coding: utf-8 -*-

import typing as T
import polars as pl

from .base_expr import BaseExpr, parse_expr
from .base_dfop import BaseDfop, parse_dfop
from .typehint import IntoExpr


if T.TYPE_CHECKING:  # pragma: no cover
    from .expr.api import T_EXPR
    from .dfop.api import T_DFOP
