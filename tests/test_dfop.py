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
case5 = Case(
    input_records=[{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}],
    dfop=dfop.Head(n=2),
    expected_output_records=[{"id": 1}, {"id": 2}],
)
case6 = Case(
    input_records=[{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}],
    dfop=dfop.Tail(n=2),
    expected_output_records=[{"id": 3}, {"id": 4}],
)
case7 = Case(
    input_records=[{"id": 1}, {"id": 2}, {"id": 3}],
    dfop=dfop.Count(),
    expected_output_records=[{"id": 3}],
)
case8 = Case(
    input_records=[{"id": 2}, {"id": 3}, {"id": 1}],
    dfop=dfop.Sort(by=["id"]),
    expected_output_records=[{"id": 1}, {"id": 2}, {"id": 3}],
)
case9 = Case(
    input_records=[
        {"id": 1, "name": "a"},
        {"id": 1, "name": "b"},
        {"id": 2, "name": "c"},
        {"id": 2, "name": "d"},
    ],
    dfop=dfop.Sort(by=["id", "name"], descending=[True, False]),
    expected_output_records=[
        {"id": 2, "name": "c"},
        {"id": 2, "name": "d"},
        {"id": 1, "name": "a"},
        {"id": 1, "name": "b"},
    ],
)
case10 = Case(
    input_records=[
        {"id": 1, "name": "a"},
        {"id": 2, "name": None},
        {"id": None, "name": "c"},
    ],
    dfop=dfop.DropNulls(),
    expected_output_records=[
        {"id": 1, "name": "a"},
    ],
)
case11 = Case(
    input_records=[
        {"id": 1, "name": "a"},
        {"id": 2, "name": None},
        {"id": None, "name": "c"},
    ],
    dfop=dfop.DropNulls(subset=["id"]),
    expected_output_records=[
        {"id": 1, "name": "a"},
        {"id": 2, "name": None},
    ],
)
case12 = Case(
    input_records=[
        {"id": 1, "name": "a"},
        {"id": 2, "name": None},
        {"id": None, "name": "c"},
    ],
    dfop=dfop.DropNulls(subset=["name"]),
    expected_output_records=[
        {"id": 1, "name": "a"},
        {"id": None, "name": "c"},
    ],
)


def test():
    print("")

    case1.run_test()
    case2.run_test()
    case3.run_test()
    case4.run_test()
    case5.run_test()
    case6.run_test()
    case7.run_test()
    case8.run_test()
    case9.run_test()
    case10.run_test()
    case11.run_test()
    case12.run_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.dfop", preview=False)
