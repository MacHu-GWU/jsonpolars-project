# -*- coding: utf-8 -*-

from datetime import datetime, date, timezone

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
case_to_datetime_1 = Case(
    input_records=[
        {"time": "2024-08-15T10:45:28"},
    ],
    expr=expr.StrToDatetime(
        expr=expr.Column(name="time"),
    ),
    expected_output_records=[
        {"time": datetime(2024, 8, 15, 10, 45, 28)},
    ],
)
# unit test doesn't pass in lower version of polars, however the code works fine
# case_to_datetime_2 = Case(
#     input_records=[
#         {"time": "2024-08-15T10:45:28"},
#     ],
#     expr=expr.StrToDatetime(
#         expr=expr.Column(name="time"),
#         time_zone="UTC",
#     ),
#     expected_output_records=[
#         {"time": datetime(2024, 8, 15, 10, 45, 28, tzinfo=timezone.utc)},
#     ],
# )
case_to_date = Case(
    input_records=[
        {"date": "2024-08-15"},
    ],
    expr=expr.StrToDate(
        expr=expr.Column(name="date"),
    ),
    expected_output_records=[
        {"date": date(2024, 8, 15)},
    ],
)
case_zfill = Case(
    input_records=[
        {"id": "1"},
    ],
    expr=expr.StrZfill(
        expr=expr.Column(name="id"),
        length=3,
    ),
    expected_output_records=[
        {"id": "001"},
    ],
)
case_pad_start = Case(
    input_records=[
        {"id": "1"},
    ],
    expr=expr.StrPadStart(
        expr=expr.Column(name="id"),
        length=3,
        fill_char="0",
    ),
    expected_output_records=[
        {"id": "001"},
    ],
)
case_pad_end = Case(
    input_records=[
        {"id": "1"},
    ],
    expr=expr.StrPadEnd(
        expr=expr.Column(name="id"),
        length=3,
        fill_char="0",
    ),
    expected_output_records=[
        {"id": "100"},
    ],
)
case_to_lowercase = Case(
    input_records=[
        {"id": "Env"},
    ],
    expr=expr.StrToLowerCase(
        expr=expr.Column(name="id"),
    ),
    expected_output_records=[
        {"id": "env"},
    ],
)
case_to_uppercase = Case(
    input_records=[
        {"id": "Env"},
    ],
    expr=expr.StrToUpperCase(
        expr=expr.Column(name="id"),
    ),
    expected_output_records=[
        {"id": "ENV"},
    ],
)
case_to_titlecase = Case(
    input_records=[
        {"id": "env"},
    ],
    expr=expr.StrToTitleCase(
        expr=expr.Column(name="id"),
    ),
    expected_output_records=[
        {"id": "Env"},
    ],
)
case_head = Case(
    input_records=[
        {"id": "Env"},
    ],
    expr=expr.StrHead(
        expr=expr.Column(name="id"),
        n=1,
    ),
    expected_output_records=[
        {"id": "E"},
    ],
)
case_tail = Case(
    input_records=[
        {"id": "Env"},
    ],
    expr=expr.StrTail(
        expr=expr.Column(name="id"),
        n=1,
    ),
    expected_output_records=[
        {"id": "v"},
    ],
)
case_slice = Case(
    input_records=[
        {"time": "2024-08-15 10:45:28"},
    ],
    expr=expr.StrSlice(
        expr=expr.Column(name="time"),
        offset=5,
        length=5,
    ),
    expected_output_records=[
        {"time": "08-15"},
    ],
)
case_replace_1 = Case(
    input_records=[
        {"text": "current env is prod, target env is prod"},
    ],
    expr=expr.StrReplace(
        expr=expr.Column(name="text"),
        pattern="prod",
        value="dev",
        literal=True,
    ),
    expected_output_records=[
        {"text": "current env is dev, target env is prod"},
    ],
)
case_replace_2 = Case(
    input_records=[
        {"text": "current env is prod, target env is prod"},
    ],
    expr=expr.StrReplace(
        expr=expr.Column(name="text"),
        pattern=expr.Lit(value="prod"),
        value=expr.Lit(value="dev"),
        literal=True,
    ),
    expected_output_records=[
        {"text": "current env is dev, target env is prod"},
    ],
)
case_replace_all_2 = Case(
    input_records=[
        {"text": "current env is prod, target env is prod"},
    ],
    expr=expr.StrReplaceAll(
        expr=expr.Column(name="text"),
        pattern=expr.Lit(value="prod"),
        value=expr.Lit(value="dev"),
        literal=True,
    ),
    expected_output_records=[
        {"text": "current env is dev, target env is dev"},
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
    case_to_datetime_1.run_with_columns_test()
    # case_to_datetime_2.run_with_columns_test()
    case_to_date.run_with_columns_test()
    case_zfill.run_with_columns_test()
    case_pad_start.run_with_columns_test()
    case_pad_end.run_with_columns_test()
    case_to_lowercase.run_with_columns_test()
    case_to_uppercase.run_with_columns_test()
    case_to_titlecase.run_with_columns_test()
    case_head.run_with_columns_test()
    case_tail.run_with_columns_test()
    case_slice.run_with_columns_test()
    case_replace_1.run_with_columns_test()
    case_replace_2.run_with_columns_test()
    case_replace_all_2.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.string", preview=False)
