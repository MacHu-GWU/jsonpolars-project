# -*- coding: utf-8 -*-

import polars as pl

from jsonpolars.expr import api as expr
from jsonpolars.tests.expr_case import Case


case_list_get_1 = Case(
    input_records=[
        {"lst": [1, 2]},
    ],
    expr=expr.ListGet(
        expr=expr.Column(name="lst"),
        index=0,
        # index=expr.Lit(value=1),
    ),
    expected_output_records=[
        {"lst": 1},
    ],
)

case_list_get_2 = Case(
    input_records=[
        {"lst": [1, 2]},
    ],
    expr=expr.ListGet(
        expr=expr.List(expr=expr.Column(name="lst")),
        index=expr.Lit(value=1),
    ),
    expected_output_records=[
        {"lst": 2},
    ],
)


def test():
    print("")

    case_list_get_1.run_with_columns_test()
    case_list_get_2.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.list", preview=False)
