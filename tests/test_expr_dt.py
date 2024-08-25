# -*- coding: utf-8 -*-

from datetime import datetime

import polars as pl

from jsonpolars.expr import api as expr
from jsonpolars.tests.expr_case import Case

case_datetime_to_string_1 = Case(
    input_records=[
        {"time": datetime(2024, 8, 1, 12, 30, 45)},
    ],
    expr=expr.DatetimeToString(
        expr=expr.Datetime(expr=expr.Column(name="time")),
        format="%m/%d/%Y %H:%M:%S",
    ),
    output_records=[
        {"time": "08/01/2024 12:30:45"},
    ],
)
case_datetime_to_string_2 = Case(
    input_records=[
        {"time": datetime(2024, 8, 1, 12, 30, 45)},
    ],
    expr=expr.DatetimeToString(
        expr=expr.Column(name="time"),
        format="%m/%d/%Y %H:%M:%S",
    ),
    output_records=[
        {"time": "08/01/2024 12:30:45"},
    ],
)


def test():
    print("")

    case_datetime_to_string_1.run_with_columns_test()
    case_datetime_to_string_2.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.dt", preview=False)
