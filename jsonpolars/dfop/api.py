# -*- coding: utf-8 -*-

import typing as T

from .manipulation import Select
from .manipulation import Rename
from .manipulation import Drop
from .manipulation import WithColumns

T_DFOP = T.Union[
    Select,
    Rename,
    Drop,
    WithColumns,
]
