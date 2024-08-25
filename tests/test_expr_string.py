# -*- coding: utf-8 -*-

import polars as pl

from jsonpolars.expr import api as expr
from jsonpolars.tests.expr_case import Case


case_split_1 = Case(
    input_records=[
        {"id": "a-1"},
    ],
    expr=expr.Split(
        expr=expr.Column(name="id"),
        by="-",
    ),
    expected_output_records=[
        {"id": ["a", "1"]},
    ],
)

case_split_2 = Case(
    input_records=[
        {"id": "a-1"},
    ],
    expr=expr.Split(
        expr=expr.String(expr=expr.Column(name="id")),
        by="-",
    ),
    expected_output_records=[
        {"id": ["a", "1"]},
    ],
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
    expected_output_records=[
        {"foo": "1-2-3"},
        {"foo": "1-2-3"},
        {"foo": "1-2-3"},
    ],
)
case_contains_1 = Case(
    input_records=[
        {"foo": "123-456-7890"},
    ],
    expr=expr.StrContains(
        expr=expr.Column(name="foo"),
        pattern="456",
    ),
    expected_output_records=[
        {"foo": True},
    ],
)
case_contains_2 = Case(
    input_records=[
        {"foo": "123-456-7890"},
    ],
    expr=expr.StrContains(
        expr=expr.Column(name="foo"),
        pattern=r"\d{4}",
    ),
    expected_output_records=[
        {"foo": True},
    ],
)
case_contains_3 = Case(
    input_records=[
        {"foo": "123-456-7890"},
    ],
    expr=expr.StrContains(
        expr=expr.Column(name="foo"),
        pattern=expr.Lit(value=r"\d{10}"),
    ),
    expected_output_records=[
        {"foo": False},
    ],
)
case_decode = Case(
    input_records=[
        {"color": "ffff00"},
    ],
    expr=expr.StrDecode(
        expr=expr.Column(name="color"),
        encoding="hex",
    ),
    expected_output_records=[
        {"color": b"\xff\xff\x00"},
    ],
)
case_encode = Case(
    input_records=[
        {"word": "foo"},
    ],
    expr=expr.StrEncode(
        expr=expr.Column(name="word"),
        encoding="hex",
    ),
    expected_output_records=[
        {"word": "666f6f"},
    ],
)
case_starts_with_1 = Case(
    input_records=[
        {"foo": "Alice"},
    ],
    expr=expr.StrStartsWith(
        expr=expr.Column(name="foo"),
        prefix="A",
    ),
    expected_output_records=[
        {"foo": True},
    ],
)
case_starts_with_2 = Case(
    input_records=[
        {"foo": "Alice"},
    ],
    expr=expr.StrStartsWith(
        expr=expr.Column(name="foo"),
        prefix=expr.Lit(value="B"),
    ),
    expected_output_records=[
        {"foo": False},
    ],
)
case_starts_with_3 = Case(
    input_records=[
        {"foo": "Alice", "prefix": "A"},
    ],
    expr=expr.StrStartsWith(
        expr=expr.Column(name="foo"),
        prefix=expr.Column(name="prefix"),
    ),
    expected_output_records=[
        {"foo": True, "prefix": "A"},
    ],
)
case_ends_with_1 = Case(
    input_records=[
        {"foo": "Alice"},
    ],
    expr=expr.StrEndsWith(
        expr=expr.Column(name="foo"),
        suffix="e",
    ),
    expected_output_records=[
        {"foo": True},
    ],
)
case_ends_with_2 = Case(
    input_records=[
        {"foo": "Alice"},
    ],
    expr=expr.StrEndsWith(
        expr=expr.Column(name="foo"),
        suffix=expr.Lit(value="f"),
    ),
    expected_output_records=[
        {"foo": False},
    ],
)
case_ends_with_3 = Case(
    input_records=[
        {"foo": "Alice", "suffix": "e"},
    ],
    expr=expr.StrEndsWith(
        expr=expr.Column(name="foo"),
        suffix=expr.Column(name="suffix"),
    ),
    expected_output_records=[
        {"foo": True, "suffix": "e"},
    ],
)


def test():
    print("")

    case_split_1.run_with_columns_test()
    case_split_2.run_with_columns_test()
    case_join.run_with_columns_test()
    case_contains_1.run_with_columns_test()
    case_contains_2.run_with_columns_test()
    case_contains_3.run_with_columns_test()
    case_decode.run_with_columns_test()
    case_encode.run_with_columns_test()
    case_starts_with_1.run_with_columns_test()
    case_starts_with_2.run_with_columns_test()
    case_starts_with_3.run_with_columns_test()
    case_ends_with_1.run_with_columns_test()
    case_ends_with_2.run_with_columns_test()
    case_ends_with_3.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.string", preview=False)
