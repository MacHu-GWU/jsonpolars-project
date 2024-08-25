# -*- coding: utf-8 -*-

from jsonpolars.expr import api as expr
from jsonpolars.tests.expr_case import Case

case_alias = Case(
    input_records=[
        {"a": 1},
    ],
    expr=expr.Alias(
        name="b",
        expr=expr.Column(name="a"),
    ),
    expected_output_records=[
        {"a": 1, "b": 1},
    ],
)


def test():
    print("")

    case_alias.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.column", preview=False)
