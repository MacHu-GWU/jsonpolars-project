# -*- coding: utf-8 -*-

import polars as pl

from jsonpolars.expr import api as expr
from jsonpolars.tests.expr_case import Case


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


def test():
    print("")

    case_concat_str.run_with_columns_test()
    case_concat_list.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.function", preview=False)
