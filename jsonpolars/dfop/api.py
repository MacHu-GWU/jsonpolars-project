# -*- coding: utf-8 -*-

import typing as T

from .manipulation_dfop import Select
from .manipulation_dfop import Rename
from .manipulation_dfop import Drop

T_DFOP = T.Union[
    Select,
    Rename,
    Drop,
]
