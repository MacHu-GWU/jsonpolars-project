# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone

import polars as pl

from jsonpolars.expr import api as expr
from jsonpolars.tests.expr_case import Case

# fmt: off
case_datetime_to_string_1 = Case(
    input_records=[
        {"time": datetime(2024, 8, 1, 12, 30, 45)},
    ],
    expr=expr.DtToString(
        expr=expr.Datetime(expr=expr.Column(name="time")),
        format="%m/%d/%Y %H:%M:%S",
    ),
    expected_output_records=[
        {"time": "08/01/2024 12:30:45"},
    ],
)
case_datetime_to_string_2 = Case(
    input_records=[
        {"time": datetime(2024, 8, 1, 12, 30, 45)},
    ],
    expr=expr.DtToString(
        expr=expr.Column(name="time"),
        format="%m/%d/%Y %H:%M:%S",
    ),
    expected_output_records=[
        {"time": "08/01/2024 12:30:45"},
    ],
)
case_dt_year = Case(
    input_records=[
        {"dt": datetime(2021, 6, 15, 14, 30, 45, 123000)},
    ],
    expr=expr.DtYear(
        expr=expr.Column(name="dt"),
    ),
    expected_output_records=[
        {"dt": 2021},
    ],
)
case_dt_quarter = Case(
    input_records=[
        {"dt": datetime(2021, 6, 15, 14, 30, 45, 123000)},
    ],
    expr=expr.DtQuarter(
        expr=expr.Column(name="dt"),
    ),
    expected_output_records=[
        {"dt": 2},
    ],
)
case_dt_month = Case(
    input_records=[
        {"dt": datetime(2021, 6, 15, 14, 30, 45, 123000)},
    ],
    expr=expr.DtMonth(
        expr=expr.Column(name="dt"),
    ),
    expected_output_records=[
        {"dt": 6},
    ],
)
case_dt_day = Case(
    input_records=[
        {"dt": datetime(2021, 6, 15, 14, 30, 45, 123000)},
    ],
    expr=expr.DtDay(
        expr=expr.Column(name="dt"),
    ),
    expected_output_records=[
        {"dt": 15},
    ],
)
case_dt_hour = Case(
    input_records=[
        {"dt": datetime(2021, 6, 15, 14, 30, 45, 123000)},
    ],
    expr=expr.DtHour(
        expr=expr.Column(name="dt"),
    ),
    expected_output_records=[
        {"dt": 14},
    ],
)
case_dt_minute = Case(
    input_records=[
        {"dt": datetime(2021, 6, 15, 14, 30, 45, 123000)},
    ],
    expr=expr.DtMinute(
        expr=expr.Column(name="dt"),
    ),
    expected_output_records=[
        {"dt": 30},
    ],
)
case_dt_second = Case(
    input_records=[
        {"dt": datetime(2021, 6, 15, 14, 30, 45, 123)},
    ],
    expr=expr.DtSecond(
        expr=expr.Column(name="dt"),
    ),
    expected_output_records=[
        {"dt": 45},
    ],
)
case_dt_nanosecond = Case(
    input_records=[
        {"dt": datetime(2021, 6, 15, 14, 30, 45, 123000)},
    ],
    expr=expr.DtNanoSecond(
        expr=expr.Column(name="dt"),
    ),
    expected_output_records=[
        {"dt": 123000000},
    ],
)
case_dt_epoch = Case(
    input_records=[
        {"dt": datetime(2021, 6, 15, 14, 30, 45, 123000)},
    ],
    expr=expr.DtEpoch(
        expr=expr.Column(name="dt"),
    ),
    expected_output_records=[
        {"dt": 1623767445123000},
    ],
)
case_dt_timestamp = Case(
    input_records=[
        {"dt": datetime(2021, 6, 15, 14, 30, 45, 123000)},
    ],
    expr=expr.DtTimestamp(
        expr=expr.Column(name="dt"),
    ),
    expected_output_records=[
        {"dt": 1623767445123000},
    ],
)
case_dt_total_days = Case(
    input_records=[
        {"dt": datetime(2021, 6, 15, 14, 30, 45, 123000)},
    ],
    expr=expr.DtTotalDays(
        expr=expr.Minus(
            left=expr.Column(name="dt"),
            right=datetime(1970, 1, 1),
        ),
    ),
    expected_output_records=[
        {"dt": 18793},
    ],
)
case_dt_total_hours = Case(
    input_records=[
        {"dt": datetime(2021, 6, 15, 14, 30, 45, 123000)},
    ],
    expr=expr.DtTotalHours(
        expr=expr.Minus(
            left=expr.Column(name="dt"),
            right=datetime(1970, 1, 1),
        ),
    ),
    expected_output_records=[
        {"dt": 451046},
    ],
)
case_dt_total_minutes = Case(
    input_records=[
        {"dt": datetime(2021, 6, 15, 14, 30, 45, 123000)},
    ],
    expr=expr.DtTotalMinutes(
        expr=expr.Minus(
            left=expr.Column(name="dt"),
            right=datetime(1970, 1, 1),
        ),
    ),
    expected_output_records=[
        {"dt": 27062790},
    ],
)
case_dt_total_seconds = Case(
    input_records=[
        {"dt": datetime(2021, 6, 15, 14, 30, 45, 123000)},
    ],
    expr=expr.DtTotalSeconds(
        expr=expr.Minus(
            left=expr.Column(name="dt"),
            right=datetime(1970, 1, 1),
        ),
    ),
    expected_output_records=[
        {"dt": 1623767445},
    ],
)
case_dt_total_milliseconds = Case(
    input_records=[
        {"dt": datetime(2021, 6, 15, 14, 30, 45, 123000)},
    ],
    expr=expr.DtTotalMilliSeconds(
        expr=expr.Minus(
            left=expr.Column(name="dt"),
            right=datetime(1970, 1, 1),
        ),
    ),
    expected_output_records=[
        {"dt": 1623767445123},
    ],
)
case_dt_total_microseconds = Case(
    input_records=[
        {"dt": datetime(2021, 6, 15, 14, 30, 45, 123000)},
    ],
    expr=expr.DtTotalMicroSeconds(
        expr=expr.Minus(
            left=expr.Column(name="dt"),
            right=datetime(1970, 1, 1),
        ),
    ),
    expected_output_records=[
        {"dt": 1623767445123000},
    ],
)
case_dt_total_nanoseconds = Case(
    input_records=[
        {"dt": datetime(2021, 6, 15, 14, 30, 45, 123000)},
    ],
    expr=expr.DtTotalNanoSeconds(
        expr=expr.Minus(
            left=expr.Column(name="dt"),
            right=datetime(1970, 1, 1),
        ),
    ),
    expected_output_records=[
        {"dt": 1623767445123000000},
    ],
)
case_dt_truncate_1 = Case(
    input_records=[
        {"dt": datetime(2021, 6, 15, 14, 30, 45, 123000)},
    ],
    expr=expr.DtTruncate(
        expr=expr.Column(name="dt"),
        every="1h",
    ),
    expected_output_records=[
        {"dt": datetime(2021, 6, 15, 14, 0, 0, 0)},
    ],
)
case_dt_truncate_2 = Case(
    input_records=[
        {"dt": datetime(2021, 6, 15, 14, 30, 45, 123000)},
    ],
    expr=expr.DtTruncate(
        expr=expr.Column(name="dt"),
        every=timedelta(hours=1),
    ),
    expected_output_records=[
        {"dt": datetime(2021, 6, 15, 14, 0, 0, 0)},
    ],
)
# fmt: on


def test():
    print("")

    case_datetime_to_string_1.run_with_columns_test()
    case_datetime_to_string_2.run_with_columns_test()
    case_dt_year.run_with_columns_test()
    case_dt_quarter.run_with_columns_test()
    case_dt_month.run_with_columns_test()
    case_dt_day.run_with_columns_test()
    case_dt_hour.run_with_columns_test()
    case_dt_minute.run_with_columns_test()
    case_dt_second.run_with_columns_test()
    case_dt_nanosecond.run_with_columns_test()
    case_dt_epoch.run_with_columns_test()
    case_dt_timestamp.run_with_columns_test()
    case_dt_total_days.run_with_columns_test()
    case_dt_total_hours.run_with_columns_test()
    case_dt_total_minutes.run_with_columns_test()
    case_dt_total_seconds.run_with_columns_test()
    case_dt_total_milliseconds.run_with_columns_test()
    case_dt_total_microseconds.run_with_columns_test()
    case_dt_total_nanoseconds.run_with_columns_test()
    case_dt_truncate_1.run_with_columns_test()
    case_dt_truncate_2.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.dt", preview=False)
