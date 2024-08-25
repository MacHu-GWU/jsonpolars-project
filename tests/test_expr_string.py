# -*- coding: utf-8 -*-

from datetime import datetime

import polars as pl

from jsonpolars.expr import api as expr
from jsonpolars.tests.expr_case import Case


case_split = Case(
    input_records=[{"id": "a-1"}],
    expr=expr.Split(
        expr=expr.Column(name="id"),
        by="-",
    ),
    output_records=[{"id": ["a", "1"]}],
)

case_join = Case(
    input_records=[
        {"foo": "1"},
        {"foo": "2"},
        {"foo": "3"},
    ],
    expr=expr.StrJoin(
        delimiter="-",
        expr=expr.Column(name="foo"),
    ),
    output_records=[
        {"foo": "1-2-3"},
        {"foo": "1-2-3"},
        {"foo": "1-2-3"},
    ],
)


def test():
    print("")

    case_split.run_with_columns_test()
    case_join.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.string", preview=False)
