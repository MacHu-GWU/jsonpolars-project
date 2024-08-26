# -*- coding: utf-8 -*-

import typing as T
from .manipulation import Cast
from .list import List
from .list import ListGet
from .dt import Datetime
from .dt import DtToString
from .dt import DtYear
from .dt import DtQuarter
from .dt import DtMonth
from .dt import DtDay
from .dt import DtHour
from .dt import DtMinute
from .dt import DtSecond
from .dt import DtNanoSecond
from .dt import DtEpoch
from .dt import DtTimestamp
from .dt import DtTotalDays
from .dt import DtTotalHours
from .dt import DtTotalMinutes
from .dt import DtTotalSeconds
from .dt import DtTotalMilliSeconds
from .dt import DtTotalMicroSeconds
from .dt import DtTotalNanoSeconds
from .dt import DtTruncate
from .operator import Plus
from .operator import Minus
from .operator import Multiply
from .operator import TrueDiv
from .operator import FloorDiv
from .operator import Negative
from .operator import Pow
from .operator import Equal
from .operator import NotEqual
from .operator import GreatThan
from .operator import GreatThanOrEqual
from .operator import LessThan
from .operator import LessThanOrEqual
from .operator import LogicalAnd
from .operator import LogicalOr
from .string import String
from .string import Split
from .string import StrJoin
from .string import StrContains
from .string import StrDecode
from .string import StrEncode
from .string import StrStartsWith
from .string import StrEndsWith
from .string import StrToDatetime
from .string import StrToDate
from .string import StrZfill
from .string import StrPadStart
from .string import StrPadEnd
from .string import StrToLowerCase
from .string import StrToUpperCase
from .string import StrToTitleCase
from .string import StrHead
from .string import StrTail
from .string import StrSlice
from .string import StrReplace
from .string import StrReplaceAll
from .function import Lit
from .function import ConcatStr
from .function import ConcatList
from .column import Column
from .column import Alias
from .struct import Struct
from .struct import StructField
from .struct import StructRenameFields
from .struct import StructWithFields

T_EXPR = T.Union[
    Cast,
    List,
    ListGet,
    Datetime,
    DtToString,
    DtYear,
    DtQuarter,
    DtMonth,
    DtDay,
    DtHour,
    DtMinute,
    DtSecond,
    DtNanoSecond,
    DtEpoch,
    DtTimestamp,
    DtTotalDays,
    DtTotalHours,
    DtTotalMinutes,
    DtTotalSeconds,
    DtTotalMilliSeconds,
    DtTotalMicroSeconds,
    DtTotalNanoSeconds,
    DtTruncate,
    Plus,
    Minus,
    Multiply,
    TrueDiv,
    FloorDiv,
    Negative,
    Pow,
    Equal,
    NotEqual,
    GreatThan,
    GreatThanOrEqual,
    LessThan,
    LessThanOrEqual,
    LogicalAnd,
    LogicalOr,
    String,
    Split,
    StrJoin,
    StrContains,
    StrDecode,
    StrEncode,
    StrStartsWith,
    StrEndsWith,
    StrToDatetime,
    StrToDate,
    StrZfill,
    StrPadStart,
    StrPadEnd,
    StrToLowerCase,
    StrToUpperCase,
    StrToTitleCase,
    StrHead,
    StrTail,
    StrSlice,
    StrReplace,
    StrReplaceAll,
    Lit,
    ConcatStr,
    ConcatList,
    Column,
    Alias,
    Struct,
    StructField,
    StructRenameFields,
    StructWithFields,
]
