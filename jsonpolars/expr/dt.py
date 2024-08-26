# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from datetime import timedelta

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr
from ..utils_expr import to_jsonpolars_other_expr


if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR


def ensure_datetime(expr: "T_EXPR") -> pl.Expr:
    if isinstance(expr, Datetime):
        return expr.to_polars()
    else:
        return expr.to_polars().dt


@dataclasses.dataclass
class Datetime(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/temporal.html
    """

    type: str = dataclasses.field(default=ExprEnum.dt.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]))

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr)


expr_enum_to_klass_mapping[ExprEnum.dt.value] = Datetime


@dataclasses.dataclass
class DtToString(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.dt.to_string.html
    """

    type: str = dataclasses.field(default=ExprEnum.dt_to_string.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    format: str = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            format=dct["format"],
        )

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).to_string(format=self.format)


expr_enum_to_klass_mapping[ExprEnum.dt_to_string.value] = DtToString


@dataclasses.dataclass
class DtYear(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.dt.year.html
    """

    type: str = dataclasses.field(default=ExprEnum.dt_year.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]))

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).year()


expr_enum_to_klass_mapping[ExprEnum.dt_year.value] = DtYear


@dataclasses.dataclass
class DtQuarter(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.dt.quarter.html
    """

    type: str = dataclasses.field(default=ExprEnum.dt_quarter.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]))

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).quarter()


expr_enum_to_klass_mapping[ExprEnum.dt_quarter.value] = DtQuarter


@dataclasses.dataclass
class DtMonth(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.dt.month.html
    """

    type: str = dataclasses.field(default=ExprEnum.dt_month.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]))

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).month()


expr_enum_to_klass_mapping[ExprEnum.dt_month.value] = DtMonth


@dataclasses.dataclass
class DtDay(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.dt.day.html
    """

    type: str = dataclasses.field(default=ExprEnum.dt_day.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]))

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).day()


expr_enum_to_klass_mapping[ExprEnum.dt_day.value] = DtDay


@dataclasses.dataclass
class DtHour(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.dt.hour.html
    """

    type: str = dataclasses.field(default=ExprEnum.dt_hour.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]))

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).hour()


expr_enum_to_klass_mapping[ExprEnum.dt_hour.value] = DtHour


@dataclasses.dataclass
class DtMinute(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.dt.minute.html
    """

    type: str = dataclasses.field(default=ExprEnum.dt_minute.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]))

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).minute()


expr_enum_to_klass_mapping[ExprEnum.dt_minute.value] = DtMinute


@dataclasses.dataclass
class DtSecond(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.dt.second.html
    """

    type: str = dataclasses.field(default=ExprEnum.dt_second.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]))

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).second()


expr_enum_to_klass_mapping[ExprEnum.dt_second.value] = DtSecond


@dataclasses.dataclass
class DtNanoSecond(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.dt.nanosecond.html
    """

    type: str = dataclasses.field(default=ExprEnum.dt_nanosecond.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]))

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).nanosecond()


expr_enum_to_klass_mapping[ExprEnum.dt_nanosecond.value] = DtNanoSecond


@dataclasses.dataclass
class DtEpoch(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.dt.epoch.html
    """

    type: str = dataclasses.field(default=ExprEnum.dt_epoch.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    time_unit: str = dataclasses.field(default="us")

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]), time_unit=dct["time_unit"])

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).epoch(time_unit=self.time_unit)


expr_enum_to_klass_mapping[ExprEnum.dt_epoch.value] = DtEpoch


@dataclasses.dataclass
class DtTimestamp(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.dt.timestamp.html
    """

    type: str = dataclasses.field(default=ExprEnum.dt_timestamp.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    time_unit: str = dataclasses.field(default="us")

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]), time_unit=dct["time_unit"])

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).timestamp(time_unit=self.time_unit)


expr_enum_to_klass_mapping[ExprEnum.dt_timestamp.value] = DtTimestamp


@dataclasses.dataclass
class DtTotalDays(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.dt.total_days.html
    """

    type: str = dataclasses.field(default=ExprEnum.dt_total_days.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]))

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).total_days()


expr_enum_to_klass_mapping[ExprEnum.dt_total_days.value] = DtTotalDays


@dataclasses.dataclass
class DtTotalHours(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.dt.total_hours.html
    """

    type: str = dataclasses.field(default=ExprEnum.dt_total_hours.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]))

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).total_hours()


expr_enum_to_klass_mapping[ExprEnum.dt_total_hours.value] = DtTotalHours


@dataclasses.dataclass
class DtTotalMinutes(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.dt.total_minutes.html
    """

    type: str = dataclasses.field(default=ExprEnum.dt_total_minutes.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]))

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).total_minutes()


expr_enum_to_klass_mapping[ExprEnum.dt_total_minutes.value] = DtTotalMinutes


@dataclasses.dataclass
class DtTotalSeconds(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.dt.total_seconds.html
    """

    type: str = dataclasses.field(default=ExprEnum.dt_total_seconds.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]))

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).total_seconds()


expr_enum_to_klass_mapping[ExprEnum.dt_total_seconds.value] = DtTotalSeconds


@dataclasses.dataclass
class DtTotalMilliSeconds(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.dt.total_milliseconds.html
    """

    type: str = dataclasses.field(default=ExprEnum.dt_total_milliseconds.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]))

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).total_milliseconds()


expr_enum_to_klass_mapping[ExprEnum.dt_total_milliseconds.value] = DtTotalMilliSeconds


@dataclasses.dataclass
class DtTotalMicroSeconds(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.dt.total_microseconds.html
    """

    type: str = dataclasses.field(default=ExprEnum.dt_total_microseconds.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]))

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).total_microseconds()


expr_enum_to_klass_mapping[ExprEnum.dt_total_microseconds.value] = DtTotalMicroSeconds


@dataclasses.dataclass
class DtTotalNanoSeconds(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.dt.total_nanoseconds.html
    """

    type: str = dataclasses.field(default=ExprEnum.dt_total_nanoseconds.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]))

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).total_nanoseconds()


expr_enum_to_klass_mapping[ExprEnum.dt_total_nanoseconds.value] = DtTotalNanoSeconds


@dataclasses.dataclass
class DtTruncate(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.dt.truncate.html
    """

    type: str = dataclasses.field(default=ExprEnum.dt_truncate.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    every: T.Union[str, timedelta, "T_EXPR"] = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            every=to_jsonpolars_other_expr(dct["every"]),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).truncate(every=self.every)


expr_enum_to_klass_mapping[ExprEnum.dt_truncate.value] = DtTruncate
