# -*- coding: utf-8 -*-

from jsonpolars.expr import api as expr
from jsonpolars.dfop import api as dfop
from jsonpolars.tests.dfop_case import Case


case1 = Case(
    input_records=[{"a": 1, "b": 2, "c": 3}],
    dfop=dfop.Select(
        exprs=[
            "a",
            expr.Column(name="c"),
        ],
        named_exprs={
            "d": "b",
            "e": expr.Lit(value=5),
        },
    ),
    expected_output_records=[{"a": 1, "c": 3, "d": 2, "e": 5}],
)
case2 = Case(
    input_records=[{"a": 1, "b": 2, "c": 3}],
    dfop=dfop.Rename(
        mapping={
            "a": "x",
            "c": "z",
        }
    ),
    expected_output_records=[{"x": 1, "b": 2, "z": 3}],
)
case3 = Case(
    input_records=[{"a": 1, "b": 2, "c": 3}],
    dfop=dfop.Drop(columns=["a", expr.Column(name="c")]),
    expected_output_records=[{"b": 2}],
)
case4 = Case(
    input_records=[{"a": 1}],
    dfop=dfop.WithColumns(
        exprs=[
            expr.Alias(
                name="b",
                expr=expr.Plus(
                    left=expr.Column(name="a"),
                    right=expr.Lit(value=1),
                ),
            ),
        ],
        named_exprs={
            "c": expr.Plus(
                left=expr.Column(name="a"),
                right=expr.Lit(value=2),
            )
        },
    ),
    expected_output_records=[{"a": 1, "b": 2, "c": 3}],
)


def test():
    print("")

    case1.run_test()
    case2.run_test()
    case3.run_test()
    case4.run_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.dfop", preview=False)
