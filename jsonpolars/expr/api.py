# -*- coding: utf-8 -*-

import typing as T

from .column import Column
from .column import Alias
from .dt import Datetime
from .dt import DatetimeToString
from .function import Lit
from .function import Plus
from .function import Minus
from .list import List
from .list import ListGet
from .manipulation import Cast
from .string import String
from .string import Split

from .utils import to_jsonpolars_into_expr
from .utils import to_polars_into_expr

T_EXPR = T.Union[
    Column,
    Alias,
    Datetime,
    DatetimeToString,
    Lit,
    Plus,
    Minus,
    List,
    ListGet,
    Cast,
    String,
    Split,
]
