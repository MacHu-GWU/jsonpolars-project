# -*- coding: utf-8 -*-

from jsonpolars import api


def test():
    _ = api
    _ = api.parse_expr
    _ = api.T_EXPR
    _ = api.expr
    _ = api.parse_dfop
    _ = api.T_DFOP
    _ = api.dfop

    # --- expr ---
    _ = api.expr.Column
    _ = api.expr.Alias
    _ = api.expr.Datetime
    _ = api.expr.DatetimeToString
    _ = api.expr.Lit
    _ = api.expr.Plus
    _ = api.expr.Minus
    _ = api.expr.List
    _ = api.expr.ListGet
    _ = api.expr.Cast
    _ = api.expr.String
    _ = api.expr.Split

    # --- dfop ---
    _ = api.dfop.Select
    _ = api.dfop.Rename
    _ = api.dfop.Drop


if __name__ == "__main__":
    from polars_transform.tests import run_cov_test

    run_cov_test(__file__, "polars_transform.api", preview=False)
