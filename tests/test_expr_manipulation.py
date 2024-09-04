# -*- coding: utf-8 -*-

from datetime import datetime

import polars as pl
from jsonpolars.expr import api as expr
from jsonpolars.utils_expr import PolarsTypeNameEnum
from jsonpolars.tests.expr_case import Case

case_cast_1 = Case(
    input_records=[
        {"time": "2024-08-01T12:30:45"},
    ],
    expr=expr.Cast(
        expr=expr.Column(name="time"),
        dtype=PolarsTypeNameEnum.Datetime,
    ),
    expected_output_records=[
        {"time": datetime(2024, 8, 1, 12, 30, 45)},
    ],
)
case_cast_2 = Case(
    input_records=[
        {"time": "2024-08-01T12:30:45"},
    ],
    expr=expr.Cast(
        expr=expr.Column(name="time"),
        dtype=pl.Datetime,
    ),
    expected_output_records=[
        {"time": datetime(2024, 8, 1, 12, 30, 45)},
    ],
)
case_cast_3 = Case(
    input_records=[
        {"time": "2024-08-01T12:30:45"},
    ],
    expr=expr.Cast(
        expr=expr.Column(name="time"),
        dtype=pl.Datetime(),
    ),
    expected_output_records=[
        {"time": datetime(2024, 8, 1, 12, 30, 45)},
    ],
)


def test():
    print("")

    case_cast_1.run_with_columns_test()
    case_cast_2.run_with_columns_test()
    case_cast_3.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.manipulation", preview=False)
