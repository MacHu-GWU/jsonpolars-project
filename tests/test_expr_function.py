# -*- coding: utf-8 -*-

import polars as pl
from datetime import date, datetime

from simpletype.api import Integer, Struct
from jsonpolars.expr import api as expr
from jsonpolars.chain import chain, PRE
from jsonpolars.utils_expr import PolarsTypeNameEnum
from jsonpolars.tests.expr_case import Case


case_lit_1 = Case(
    input_records=[
        {"a": 1},
    ],
    expr=expr.Alias(
        expr=expr.Lit(
            value=111,
        ),
        name="a",
    ),
    expected_output_records=[
        {"a": 111},
    ],
)
case_lit_2 = Case(
    input_records=[
        {"a": 1},
    ],
    expr=expr.Alias(
        expr=expr.Lit(
            value=111,
            dtype=PolarsTypeNameEnum.Int8,
        ),
        name="a",
    ),
    expected_output_records=[
        {"a": 111},
    ],
)
case_lit_3 = Case(
    input_records=[
        {"a": 1},
    ],
    expr=expr.Alias(
        expr=expr.Lit(
            value=222,
            dtype=pl.Int32,
        ),
        name="a",
    ),
    expected_output_records=[
        {"a": 222},
    ],
)
case_lit_4 = Case(
    input_records=[
        {"a": 1},
    ],
    expr=expr.Alias(
        expr=expr.Lit(
            value=333,
            dtype=pl.Int64(),
        ),
        name="a",
    ),
    expected_output_records=[
        {"a": 333},
    ],
)
case_concat_str = Case(
    input_records=[
        {"col_1": "a", "col_2": "b"},
    ],
    expr=expr.Alias(
        expr=expr.ConcatStr(
            exprs=[
                "col_1",
                expr.Column(name="col_2"),
            ],
            separator="-",
        ),
        name="col_3",
    ),
    expected_output_records=[
        {"col_1": "a", "col_2": "b", "col_3": "a-b"},
    ],
)
case_concat_list = Case(
    input_records=[
        {"col_1": [1, 2], "col_2": [3, 4]},
    ],
    expr=expr.Alias(
        expr=expr.ConcatList(
            exprs=[
                "col_1",
                expr.Column(name="col_2"),
            ],
        ),
        name="col_3",
    ),
    expected_output_records=[
        {"col_1": [1, 2], "col_2": [3, 4], "col_3": [1, 2, 3, 4]},
    ],
)
case_func_struct_1 = Case(
    input_records=[
        {
            "a": 1,
            "b": 2,
            "c": 3,
        },
    ],
    expr=expr.Alias(
        expr=expr.FuncStruct(
            exprs=["a", "b"],
        ),
        name="data",
    ),
    expected_output_records=[
        {"a": 1, "b": 2, "c": 3, "data": {"a": 1, "b": 2}},
    ],
)
case_func_struct_2 = Case(
    input_records=[
        {
            "a": 1,
            "b": 2,
            "c": 3,
        },
    ],
    expr=expr.Alias(
        expr=expr.FuncStruct(
            exprs=[
                expr.Alias(expr=expr.Column(name="a"), name="x"),
                expr.Alias(expr=expr.Column(name="b"), name="y"),
            ],
        ),
        name="data",
    ),
    expected_output_records=[
        {"a": 1, "b": 2, "c": 3, "data": {"x": 1, "y": 2}},
    ],
)
case_func_struct_3 = Case(
    input_records=[
        {
            "a": 1,
            "b": 2,
            "c": 3,
        },
    ],
    expr=expr.Alias(
        expr=expr.FuncStruct(
            named_exprs=dict(
                x=expr.Column(name="a"),
                y=expr.Column(name="b"),
            ),
        ),
        name="data",
    ),
    expected_output_records=[
        {"a": 1, "b": 2, "c": 3, "data": {"x": 1, "y": 2}},
    ],
)
case_func_struct_4 = Case(
    input_records=[
        {"data": {"a": 1, "b": 2, "c": 3}},
    ],
    expr=expr.Alias(
        expr=expr.FuncStruct(
            named_exprs=dict(
                x=expr.StructField(expr=expr.Column(name="data"), name="a"),
                y=expr.StructField(expr=expr.Column(name="data"), name="b"),
            ),
        ),
        name="res",
    ),
    expected_output_records=[
        {"data": {"a": 1, "b": 2, "c": 3}, "res": {"x": 1, "y": 2}},
    ],
)
case_func_struct_5 = Case(
    input_records=[
        {"data": {"a": 1, "b": 2, "c": 3}},
    ],
    expr=expr.Alias(
        expr=expr.FuncStruct(
            exprs=[
                expr.StructField(
                    expr=expr.Column(name="data"),
                    name="a",
                    more_names=["b"],
                )
            ]
        ),
        name="res",
    ),
    expected_output_records=[
        {"data": {"a": 1, "b": 2, "c": 3}, "res": {"a": 1, "b": 2}},
    ],
)
case_func_struct_6 = Case(
    input_records=[
        {
            "a": 1,
            "b": 2,
            "c": 3,
        },
    ],
    expr=expr.Alias(
        expr=expr.FuncStruct(
            exprs=["a", "b"],
            schema={
                "a": Integer().to_dict(),
                "b": Integer().to_dict(),
            },
        ),
        name="data",
    ),
    expected_output_records=[
        {"a": 1, "b": 2, "c": 3, "data": {"a": 1, "b": 2}},
    ],
)
case_func_struct_7 = Case(
    input_records=[
        {
            "a": 1,
            "b": 2,
            "struct1": {
                "c": 3,
                "d": 4,
                "struct2": {
                    "e": 5,
                    "f": 6,
                },
            },
        },
    ],
    expr=expr.Alias(
        expr=expr.FuncStruct(
            named_exprs=dict(
                c=expr.StructField(
                    expr=expr.Column(name="struct1"),
                    name="c",
                ),
                struct2=expr.FuncStruct(
                    named_exprs=dict(
                        e=expr.StructField(
                            expr=expr.StructField(
                                expr=expr.Column(name="struct1"),
                                name="struct2",
                            ),
                            name="e",
                        ),
                    )
                ),
            )
        ),
        name="struct1",
    ),
    expected_output_records=[
        {
            "a": 1,
            "b": 2,
            "struct1": {
                "c": 3,
                "struct2": {
                    "e": 5,
                },
            },
        },
    ],
)
case_func_struct_8 = Case(
    input_records=[
        {
            "a": 1,
            "b": 2,
            "struct1": {
                "c": 3,
                "d": 4,
                "struct2": {
                    "e": 5,
                    "f": 6,
                },
            },
        },
    ],
    expr=chain(
        expr.FuncStruct(
            named_exprs=dict(
                c=expr.StructField(
                    expr=expr.Column(name="struct1"),
                    name="c",
                ),
                struct2=expr.FuncStruct(
                    named_exprs=dict(
                        e=chain(
                            expr.Column(name="struct1"),
                            expr.StructField(expr=PRE, name="struct2"),
                            expr.StructField(expr=PRE, name="e"),
                        )
                    ),
                ),
            ),
        ),
        expr.Alias(expr=PRE, name="struct1"),
    ),
    expected_output_records=[
        {
            "a": 1,
            "b": 2,
            "struct1": {
                "c": 3,
                "struct2": {
                    "e": 5,
                },
            },
        },
    ],
)
case_format = Case(
    input_records=[
        {"col_1": "a", "col_2": 1},
    ],
    expr=expr.Alias(
        expr=expr.Format(
            f_string="{}-{}",
            exprs=[
                "col_1",
                expr.Column(name="col_2"),
            ],
        ),
        name="col_3",
    ),
    expected_output_records=[
        {"col_1": "a", "col_2": 1, "col_3": "a-1"},
    ],
)
case_date_1 = Case(
    input_records=[
        {"year": 2015, "month": 1, "day": 15},
    ],
    expr=expr.Alias(
        expr=expr.FuncDate(
            year=2008,
            month=7,
            day=23,
        ),
        name="date",
    ),
    expected_output_records=[
        {"year": 2015, "month": 1, "day": 15, "date": date(2008, 7, 23)},
    ],
)
case_date_2 = Case(
    input_records=[
        {"year": 2015, "month": 1, "day": 15},
    ],
    expr=expr.Alias(
        expr=expr.FuncDate(
            year="year",
            month="month",
            day="day",
        ),
        name="date",
    ),
    expected_output_records=[
        {"year": 2015, "month": 1, "day": 15, "date": date(2015, 1, 15)},
    ],
)
case_datetime_2 = Case(
    input_records=[
        {"year": 2015, "month": 1, "day": 15},
    ],
    expr=expr.Alias(
        expr=expr.FuncDatetime(
            year=2008,
            month=7,
            day=23,
        ),
        name="date",
    ),
    expected_output_records=[
        {"year": 2015, "month": 1, "day": 15, "date": datetime(2008, 7, 23)},
    ],
)


def test():
    print("")

    case_lit_1.run_with_columns_test()
    case_lit_2.run_with_columns_test()
    case_lit_3.run_with_columns_test()
    case_lit_4.run_with_columns_test()
    case_concat_str.run_with_columns_test()
    case_concat_list.run_with_columns_test()
    case_func_struct_1.run_with_columns_test()
    case_func_struct_2.run_with_columns_test()
    case_func_struct_3.run_with_columns_test()
    case_func_struct_4.run_with_columns_test()
    case_func_struct_5.run_with_columns_test()
    case_func_struct_6.run_with_columns_test()
    case_func_struct_7.run_with_columns_test()
    case_func_struct_8.run_with_columns_test()
    case_format.run_with_columns_test()
    case_date_1.run_with_columns_test()
    case_date_2.run_with_columns_test()
    case_datetime_2.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.function", preview=False)
