# -*- coding: utf-8 -*-

from jsonpolars import api


def test():
    _ = api
    _ = api.ExprEnum
    _ = api.parse_expr
    _ = api.PolarsTypeNameEnum
    _ = api.T_EXPR
    _ = api.expr
    _ = api.DfopEnum
    _ = api.parse_dfop
    _ = api.T_DFOP
    _ = api.dfop
    _ = api.chain
    _ = api.PRE

    # --- expr ---
    _ = api.expr.Cast
    _ = api.expr.List
    _ = api.expr.ListGet
    _ = api.expr.ListEval
    _ = api.expr.Datetime
    _ = api.expr.DtToString
    _ = api.expr.DtYear
    _ = api.expr.DtQuarter
    _ = api.expr.DtMonth
    _ = api.expr.DtDay
    _ = api.expr.DtHour
    _ = api.expr.DtMinute
    _ = api.expr.DtSecond
    _ = api.expr.DtNanoSecond
    _ = api.expr.DtEpoch
    _ = api.expr.DtTimestamp
    _ = api.expr.DtTotalDays
    _ = api.expr.DtTotalHours
    _ = api.expr.DtTotalMinutes
    _ = api.expr.DtTotalSeconds
    _ = api.expr.DtTotalMilliSeconds
    _ = api.expr.DtTotalMicroSeconds
    _ = api.expr.DtTotalNanoSeconds
    _ = api.expr.DtTruncate
    _ = api.expr.Plus
    _ = api.expr.Minus
    _ = api.expr.Multiply
    _ = api.expr.TrueDiv
    _ = api.expr.FloorDiv
    _ = api.expr.Negative
    _ = api.expr.Pow
    _ = api.expr.Equal
    _ = api.expr.NotEqual
    _ = api.expr.GreatThan
    _ = api.expr.GreatThanOrEqual
    _ = api.expr.LessThan
    _ = api.expr.LessThanOrEqual
    _ = api.expr.LogicalAnd
    _ = api.expr.LogicalOr
    _ = api.expr.String
    _ = api.expr.Split
    _ = api.expr.StrJoin
    _ = api.expr.StrContains
    _ = api.expr.StrDecode
    _ = api.expr.StrEncode
    _ = api.expr.StrStartsWith
    _ = api.expr.StrEndsWith
    _ = api.expr.StrToDatetime
    _ = api.expr.StrToDate
    _ = api.expr.StrZfill
    _ = api.expr.StrPadStart
    _ = api.expr.StrPadEnd
    _ = api.expr.StrToLowerCase
    _ = api.expr.StrToUpperCase
    _ = api.expr.StrToTitleCase
    _ = api.expr.StrHead
    _ = api.expr.StrTail
    _ = api.expr.StrSlice
    _ = api.expr.StrReplace
    _ = api.expr.StrReplaceAll
    _ = api.expr.Lit
    _ = api.expr.ConcatStr
    _ = api.expr.ConcatList
    _ = api.expr.FuncStruct
    _ = api.expr.Format
    _ = api.expr.FuncDate
    _ = api.expr.FuncDatetime
    _ = api.expr.Element
    _ = api.expr.Column
    _ = api.expr.Alias
    _ = api.expr.Struct
    _ = api.expr.StructField
    _ = api.expr.StructRenameFields
    _ = api.expr.StructWithFields

    # --- dfop ---
    _ = api.dfop.Select
    _ = api.dfop.Rename
    _ = api.dfop.Drop
    _ = api.dfop.WithColumns
    _ = api.dfop.Head
    _ = api.dfop.Tail
    _ = api.dfop.Sort
    _ = api.dfop.DropNulls
    _ = api.dfop.Count


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.api", preview=False)
