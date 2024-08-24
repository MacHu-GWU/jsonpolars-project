# -*- coding: utf-8 -*-

import typing as T

from .aggregation import Count
from .manipulation import Select
from .manipulation import Rename
from .manipulation import Drop
from .manipulation import WithColumns
from .manipulation import Head
from .manipulation import Tail
from .manipulation import Sort
from .manipulation import DropNulls

T_DFOP = T.Union[
    Count,
    Select,
    Rename,
    Drop,
    WithColumns,
    Head,
    Tail,
    Sort,
    DropNulls,
]
