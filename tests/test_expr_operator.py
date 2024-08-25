# -*- coding: utf-8 -*-

import polars as pl

from jsonpolars.expr import api as expr
from jsonpolars.tests.expr_case import Case


case_plus_1 = Case(
    input_records=[
        {"id": 1},
    ],
    expr=expr.Plus(
        left=expr.Column(name="id"),
        right=expr.Lit(value=100),
    ),
    expected_output_records=[
        {"id": 101},
    ],
)
case_plus_2 = Case(
    input_records=[
        {"id": 1},
    ],
    expr=expr.Plus(
        left=expr.Column(name="id"),
        right=100,
    ),
    expected_output_records=[
        {"id": 101},
    ],
)
case_minus_1 = Case(
    input_records=[
        {"id": 1},
    ],
    expr=expr.Minus(
        left=expr.Column(name="id"),
        right=expr.Lit(value=100),
    ),
    expected_output_records=[
        {"id": -99},
    ],
)
case_minus_2 = Case(
    input_records=[
        {"id": 1},
    ],
    expr=expr.Minus(
        left=expr.Column(name="id"),
        right=100,
    ),
    expected_output_records=[
        {"id": -99},
    ],
)


def test():
    print("")

    case_plus_1.run_with_columns_test()
    case_plus_2.run_with_columns_test()
    case_minus_1.run_with_columns_test()
    case_minus_2.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.operator", preview=False)
