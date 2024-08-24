# -*- coding: utf-8 -*-

from datetime import datetime

import polars as pl

from jsonpolars.expr import api as expr
from jsonpolars.tests.expr_case import Case


case1 = Case(
    input_records=[{"id": 1}],
    expr=expr.Alias(
        name="id_plus_100",
        expr=expr.Plus(
            left=expr.Column(name="id"),
            right=expr.Lit(value=100),
        ),
    ),
    output_records=[{"id": 1, "id_plus_100": 101}],
)
case2 = Case(
    input_records=[{"id": 1}],
    expr=expr.Alias(
        name="id_minus_100",
        expr=expr.Minus(
            left=expr.Column(name="id"),
            right=expr.Lit(value=100),
        ),
    ),
    output_records=[{"id": 1, "id_minus_100": -99}],
)
case3 = Case(
    input_records=[{"time": "2024-08-01T12:30:45"}],
    expr=expr.Cast(
        dtype=pl.Datetime(),
        expr=expr.Column(name="time"),
    ),
    output_records=[{"time": datetime(2024, 8, 1, 12, 30, 45)}],
)
case4 = Case(
    input_records=[{"id": "a-1"}],
    expr=expr.ListGet(
        expr=expr.List(
            expr=expr.Split(
                expr=expr.String(expr=expr.Column(name="id")),
                by="-",
            )
        ),
        index=0,
    ),
    output_records=[{"id": "a"}],
)
case5 = Case(
    input_records=[{"id": "a-1"}],
    expr=expr.ListGet(
        expr=expr.List(
            expr=expr.Split(
                expr=expr.String(expr=expr.Column(name="id")),
                by="-",
            )
        ),
        index=expr.Lit(value=1),
    ),
    output_records=[{"id": "1"}],
)
case6 = Case(
    input_records=[{"time": datetime(2024, 8, 1, 12, 30, 45)}],
    expr=expr.DatetimeToString(
        expr=expr.Datetime(expr=expr.Column(name="time")),
        format="%Y-%m-%d %H:%M:%S",
    ),
    output_records=[{"time": "2024-08-01 12:30:45"}],
)


def test():
    print("")

    case1.run_with_columns_test()
    case2.run_with_columns_test()
    case3.run_with_columns_test()
    case4.run_with_columns_test()
    case5.run_with_columns_test()
    case6.run_with_columns_test()


if __name__ == "__main__":
    from polars_transform.tests import run_cov_test

    run_cov_test(__file__, "polars_transform.expr", preview=False)
