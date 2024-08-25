# -*- coding: utf-8 -*-

from datetime import datetime

import polars as pl

from jsonpolars.expr import api as expr
from jsonpolars.tests.expr_case import Case

case_cast = Case(
    input_records=[
        {"time": "2024-08-01T12:30:45"},
    ],
    expr=expr.Cast(
        dtype=pl.Datetime(),
        expr=expr.Column(name="time"),
    ),
    expected_output_records=[
        {"time": datetime(2024, 8, 1, 12, 30, 45)},
    ],
)


def test():
    print("")

    case_cast.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.manipulation", preview=False)
