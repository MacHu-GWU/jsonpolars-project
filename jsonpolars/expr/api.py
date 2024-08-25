# -*- coding: utf-8 -*-

import typing as T
from .manipulation import Cast
from .list import List
from .list import ListGet
from .dt import Datetime
from .dt import DatetimeToString
from .string import String
from .string import Split
from .string import StrJoin
from .function import Lit
from .function import Plus
from .function import Minus
from .column import Column
from .column import Alias

from .utils import to_jsonpolars_into_expr
from .utils import to_polars_into_expr

T_EXPR = T.Union[
    Cast,
    List,
    ListGet,
    Datetime,
    DatetimeToString,
    String,
    Split,
    StrJoin,
    Lit,
    Plus,
    Minus,
    Column,
    Alias,
]