# -*- coding: utf-8 -*-

import polars as pl
from datetime import date, datetime

from simpletype.api import String, Struct
from jsonpolars.expr import api as expr
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
            "id": 1,
            "profile": {
                "name": "Alice",
                "address": {
                    "street": "123 Main St",
                    "zipcode": "12345",
                },
            },
        },
    ],
    expr=expr.Alias(
        expr=expr.FuncStruct(
            named_exprs={
                "address": expr.FuncStruct(
                    named_exprs={
                        "street": expr.StructField(
                            expr=expr.StructField(
                                expr=expr.Column(name="profile"),
                                name="address",
                            ),
                            name="street",
                        ),
                    },
                ),
            },
        ),
        name="profile",
    ),
    expected_output_records=[
        {"id": 1, "profile": {"address": {"street": "123 Main St"}}},
    ],
)
case_func_struct_2 = Case(
    input_records=[
        {
            "id": 1,
            "profile": {
                "name": "Alice",
                "address": {
                    "street": "123 Main St",
                    "zipcode": "12345",
                },
            },
        },
    ],
    expr=expr.Alias(
        expr=expr.FuncStruct(
            named_exprs={
                "address": expr.FuncStruct(
                    named_exprs={
                        "street": expr.StructField(
                            expr=expr.StructField(
                                expr=expr.Column(name="profile"),
                                name="address",
                            ),
                            name="street",
                        ),
                    },
                ),
            },
            schema={
                "address": Struct(fields={"street": String()}).to_dict(),
            },
        ),
        name="profile",
    ),
    expected_output_records=[
        {"id": 1, "profile": {"address": {"street": "123 Main St"}}},
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
    case_format.run_with_columns_test()
    case_date_1.run_with_columns_test()
    case_date_2.run_with_columns_test()
    case_datetime_2.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.function", preview=False)
