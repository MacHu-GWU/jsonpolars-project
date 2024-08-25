# -*- coding: utf-8 -*-

from datetime import datetime, date

import polars as pl

from jsonpolars.expr import api as expr
from jsonpolars.tests.expr_case import Case

case_datetime_to_string_1 = Case(
    input_records=[
        {"time": datetime(2024, 8, 1, 12, 30, 45)},
    ],
    expr=expr.DtToString(
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
    expr=expr.DtToString(
        expr=expr.Column(name="time"),
        format="%m/%d/%Y %H:%M:%S",
    ),
    output_records=[
        {"time": "08/01/2024 12:30:45"},
    ],
)
case_dt_year = Case(
    input_records=[
        {"date": date(1977, 1, 1)},
        {"date": date(1978, 1, 1)},
        {"date": date(1979, 1, 1)},
    ],
    expr=expr.DtYear(
        expr=expr.Column(name="date"),
    ),
    output_records=[
        {"date": 1977},
        {"date": 1978},
        {"date": 1979},
    ],
)


def test():
    print("")

    case_datetime_to_string_1.run_with_columns_test()
    case_datetime_to_string_2.run_with_columns_test()
    case_dt_year.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.dt", preview=False)
