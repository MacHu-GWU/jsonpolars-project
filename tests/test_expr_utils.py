# -*- coding: utf-8 -*-

import polars as pl
from jsonpolars.expr import api as expr
from jsonpolars.utils_expr import (
    to_jsonpolars_into_expr,
    to_polars_into_expr,
    to_jsonpolars_other_expr,
    to_polars_other_expr,
)


def test_to_jsonpolars_into_expr():
    assert to_jsonpolars_into_expr("col_1") == "col_1"
    assert to_jsonpolars_into_expr({"type": "column", "name": "col_1"}) == expr.Column(
        name="col_1"
    )
    assert to_jsonpolars_into_expr(expr.Column(name="col_1")) == expr.Column(
        name="col_1"
    )


def test_to_polars_into_expr():
    assert to_polars_into_expr("col_1") == "col_1"
    assert isinstance(to_polars_into_expr(expr.Column(name="col_1")), pl.Expr)


def test_parse_other_expr():
    assert to_jsonpolars_other_expr("hello") == "hello"
    assert to_jsonpolars_other_expr({"type": "column", "name": "col_1"}) == expr.Column(
        name="col_1"
    )


def test_other_expr_to_polars():
    assert to_polars_other_expr("hello") == "hello"
    assert isinstance(to_polars_other_expr(expr.Column(name="col_1")), pl.Expr)


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.utils_expr", preview=False)
