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
case_multiply = Case(
    input_records=[
        {"id": 1},
    ],
    expr=expr.Multiply(
        left=expr.Column(name="id"),
        right=5,
    ),
    expected_output_records=[
        {"id": 5},
    ],
)
case_truediv = Case(
    input_records=[
        {"id": 6},
    ],
    expr=expr.TrueDiv(
        left=expr.Column(name="id"),
        right=2,
    ),
    expected_output_records=[
        {"id": 3},
    ],
)
case_floordiv = Case(
    input_records=[
        {"id": 10},
    ],
    expr=expr.FloorDiv(
        left=expr.Column(name="id"),
        right=4,
    ),
    expected_output_records=[
        {"id": 2},
    ],
)
case_neg = Case(
    input_records=[
        {"id": 1},
    ],
    expr=expr.Negative(
        expr=expr.Column(name="id"),
    ),
    expected_output_records=[
        {"id": -1},
    ],
)
case_pow = Case(
    input_records=[
        {"id": 2},
    ],
    expr=expr.Pow(
        left=expr.Column(name="id"),
        right=4,
    ),
    expected_output_records=[
        {"id": 16},
    ],
)
case_equal = Case(
    input_records=[
        {"id": 1},
    ],
    expr=expr.Equal(
        left=expr.Column(name="id"),
        right=1,
    ),
    expected_output_records=[
        {"id": True},
    ],
)
case_notequal = Case(
    input_records=[
        {"id": 1},
    ],
    expr=expr.NotEqual(
        left=expr.Column(name="id"),
        right=1,
    ),
    expected_output_records=[
        {"id": False},
    ],
)
case_gt_1 = Case(
    input_records=[
        {"id": 1},
    ],
    expr=expr.GreatThan(
        left=expr.Column(name="id"),
        right=0,
    ),
    expected_output_records=[
        {"id": True},
    ],
)
case_gt_2 = Case(
    input_records=[
        {"id": 1},
    ],
    expr=expr.GreatThan(
        left=expr.Column(name="id"),
        right=1,
    ),
    expected_output_records=[
        {"id": False},
    ],
)
case_ge_1 = Case(
    input_records=[
        {"id": 1},
    ],
    expr=expr.GreatThanOrEqual(
        left=expr.Column(name="id"),
        right=0,
    ),
    expected_output_records=[
        {"id": True},
    ],
)
case_ge_2 = Case(
    input_records=[
        {"id": 1},
    ],
    expr=expr.GreatThanOrEqual(
        left=expr.Column(name="id"),
        right=1,
    ),
    expected_output_records=[
        {"id": True},
    ],
)
case_lt_1 = Case(
    input_records=[
        {"id": 1},
    ],
    expr=expr.LessThan(left=expr.Column(name="id"), right=2.0),
    expected_output_records=[
        {"id": True},
    ],
)
case_lt_2 = Case(
    input_records=[
        {"id": 1},
    ],
    expr=expr.LessThan(
        left=expr.Column(name="id"),
        right=1,
    ),
    expected_output_records=[
        {"id": False},
    ],
)
case_le_1 = Case(
    input_records=[
        {"id": 1},
    ],
    expr=expr.LessThanOrEqual(left=expr.Column(name="id"), right=2.0),
    expected_output_records=[
        {"id": True},
    ],
)
case_le_2 = Case(
    input_records=[
        {"id": 1},
    ],
    expr=expr.LessThanOrEqual(
        left=expr.Column(name="id"),
        right=1,
    ),
    expected_output_records=[
        {"id": True},
    ],
)
case_and_1 = Case(
    input_records=[
        {"flag": True},
    ],
    expr=expr.LogicalAnd(
        left=expr.Column(name="flag"),
        right=True,
    ),
    expected_output_records=[
        {"flag": True},
    ],
)
case_and_2 = Case(
    input_records=[
        {"flag": True},
    ],
    expr=expr.LogicalAnd(
        left=expr.Column(name="flag"),
        right=False,
    ),
    expected_output_records=[
        {"flag": False},
    ],
)
case_or_1 = Case(
    input_records=[
        {"flag": False},
    ],
    expr=expr.LogicalOr(
        left=expr.Column(name="flag"),
        right=False,
    ),
    expected_output_records=[
        {"flag": False},
    ],
)
case_or_2 = Case(
    input_records=[
        {"flag": False},
    ],
    expr=expr.LogicalOr(
        left=expr.Column(name="flag"),
        right=True,
    ),
    expected_output_records=[
        {"flag": True},
    ],
)


def test():
    print("")

    case_plus_1.run_with_columns_test()
    case_plus_2.run_with_columns_test()
    case_minus_1.run_with_columns_test()
    case_minus_2.run_with_columns_test()
    case_multiply.run_with_columns_test()
    case_truediv.run_with_columns_test()
    case_floordiv.run_with_columns_test()
    case_neg.run_with_columns_test()
    case_pow.run_with_columns_test()
    case_equal.run_with_columns_test()
    case_notequal.run_with_columns_test()
    case_gt_1.run_with_columns_test()
    case_gt_2.run_with_columns_test()
    case_ge_1.run_with_columns_test()
    case_ge_2.run_with_columns_test()
    case_lt_1.run_with_columns_test()
    case_lt_2.run_with_columns_test()
    case_le_1.run_with_columns_test()
    case_le_2.run_with_columns_test()
    case_and_1.run_with_columns_test()
    case_and_2.run_with_columns_test()
    case_or_1.run_with_columns_test()
    case_or_2.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.operator", preview=False)
