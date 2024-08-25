# -*- coding: utf-8 -*-

from jsonpolars.expr import api as expr
from jsonpolars.dfop import api as dfop
from jsonpolars.tests.dfop_case import Case


case_select = Case(
    input_records=[
        {"a": 1, "b": 2, "c": 3},
    ],
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
    expected_output_records=[
        {"a": 1, "c": 3, "d": 2, "e": 5},
    ],
)
case_rename = Case(
    input_records=[
        {"a": 1, "b": 2, "c": 3},
    ],
    dfop=dfop.Rename(
        mapping={
            "a": "x",
            "c": "z",
        }
    ),
    expected_output_records=[
        {"x": 1, "b": 2, "z": 3},
    ],
)
case_drop = Case(
    input_records=[
        {"a": 1, "b": 2, "c": 3},
    ],
    dfop=dfop.Drop(columns=["a", expr.Column(name="c")]),
    expected_output_records=[
        {"b": 2},
    ],
)
case_with_columns = Case(
    input_records=[
        {"a": 1},
    ],
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
    expected_output_records=[
        {"a": 1, "b": 2, "c": 3},
    ],
)
case_head = Case(
    input_records=[
        {"id": 1},
        {"id": 2},
        {"id": 3},
        {"id": 4},
    ],
    dfop=dfop.Head(n=2),
    expected_output_records=[
        {"id": 1},
        {"id": 2},
    ],
)
case_tail = Case(
    input_records=[
        {"id": 1},
        {"id": 2},
        {"id": 3},
        {"id": 4},
    ],
    dfop=dfop.Tail(n=2),
    expected_output_records=[
        {"id": 3},
        {"id": 4},
    ],
)
case_count = Case(
    input_records=[
        {"id": 1},
        {"id": 2},
        {"id": 3},
    ],
    dfop=dfop.Count(),
    expected_output_records=[
        {"id": 3},
    ],
)
case_sort_1 = Case(
    input_records=[
        {"id": 2},
        {"id": 3},
        {"id": 1},
    ],
    dfop=dfop.Sort(by=["id"]),
    expected_output_records=[
        {"id": 1},
        {"id": 2},
        {"id": 3},
    ],
)
case_sort_2 = Case(
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
case_drop_nulls_1 = Case(
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
case_drop_nulls_2 = Case(
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
case_drop_nulls_3 = Case(
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

    case_select.run_test()
    case_rename.run_test()
    case_drop.run_test()
    case_with_columns.run_test()
    case_head.run_test()
    case_tail.run_test()
    case_count.run_test()
    case_sort_1.run_test()
    case_sort_2.run_test()
    case_drop_nulls_1.run_test()
    case_drop_nulls_2.run_test()
    case_drop_nulls_3.run_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.dfop.manipulation", preview=False)
