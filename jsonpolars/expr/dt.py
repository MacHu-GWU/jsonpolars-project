# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR


def ensure_datetime(expr: "T_EXPR") -> pl.Expr:
    if isinstance(expr, Datetime):
        return expr.to_polars()
    else:
        return expr.to_polars().dt


@dataclasses.dataclass
class Datetime(BaseExpr):
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
    type: str = dataclasses.field(default=ExprEnum.dt_year.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]))

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).year()


expr_enum_to_klass_mapping[ExprEnum.dt_year.value] = DtYear


@dataclasses.dataclass
class DtMonth(BaseExpr):
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
class DtTotalDays(BaseExpr):
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
    type: str = dataclasses.field(default=ExprEnum.dt_total_nanoseconds.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]))

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).total_nanoseconds()


expr_enum_to_klass_mapping[ExprEnum.dt_total_nanoseconds.value] = DtTotalNanoSeconds
