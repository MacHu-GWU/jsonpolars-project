# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..expr import api as expr
from .. import utils_expr
from ..base_dfop import DfopEnum, BaseDfop, dfop_enum_to_klass_mapping

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_DFOP
    from ..expr.api import T_EXPR
    from ..typehint import IntoExpr, ColumnNameOrSelector


def _extract_exprs_named_exprs(exprs, named_exprs):
    """
    Used in Select.from_dict and WithColumns.from_dict.
    """
    new_exprs = [utils_expr.to_jsonpolars_into_expr(expr_like) for expr_like in exprs]
    new_named_exprs = {
        name: utils_expr.to_jsonpolars_into_expr(expr_like)
        for name, expr_like in named_exprs.items()
    }
    return new_exprs, new_named_exprs


def _convert_to_exprs_named_exprs(exprs, named_exprs):
    """
    Used in Select.to_polars and WithColumns.to_polars.
    """
    new_exprs = [utils_expr.to_polars_into_expr(expr_like) for expr_like in exprs]
    new_named_exprs = {
        name: utils_expr.to_polars_into_expr(expr_like)
        for name, expr_like in named_exprs.items()
    }
    return new_exprs, new_named_exprs


@dataclasses.dataclass
class Select(BaseDfop):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.select.html
    """

    type: str = dataclasses.field(default=DfopEnum.select.value)
    exprs: T.List["IntoExpr"] = dataclasses.field(default_factory=list)
    named_exprs: T.Dict[str, "IntoExpr"] = dataclasses.field(default_factory=dict)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        exprs, named_exprs = _extract_exprs_named_exprs(
            dct["exprs"], dct["named_exprs"]
        )
        return cls(exprs=exprs, named_exprs=named_exprs)

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        exprs, named_exprs = _convert_to_exprs_named_exprs(self.exprs, self.named_exprs)
        return df.select(*exprs, **named_exprs)


dfop_enum_to_klass_mapping[DfopEnum.select.value] = Select


@dataclasses.dataclass
class Rename(BaseDfop):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.rename.html
    """

    type: str = dataclasses.field(default=DfopEnum.rename.value)
    mapping: T.Union[T.Dict[str, str], T.Callable[[str], str]] = dataclasses.field(
        default=REQUIRED
    )

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            mapping=dct["mapping"],
        )

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.rename(self.mapping)


dfop_enum_to_klass_mapping[DfopEnum.rename.value] = Rename


@dataclasses.dataclass
class Drop(BaseDfop):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.drop.html
    """

    type: str = dataclasses.field(default=DfopEnum.drop.value)
    columns: T.List["ColumnNameOrSelector"] = dataclasses.field(default=REQUIRED)
    strict: bool = dataclasses.field(default=True)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        columns, _ = _extract_exprs_named_exprs(dct["columns"], {})
        return cls(
            columns=columns,
            strict=dct["strict"],
        )

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        columns, _ = _convert_to_exprs_named_exprs(self.columns, {})
        return df.drop(*columns, strict=self.strict)


dfop_enum_to_klass_mapping[DfopEnum.drop.value] = Drop


@dataclasses.dataclass
class WithColumns(BaseDfop):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.with_columns.html#
    """

    type: str = dataclasses.field(default=DfopEnum.with_columns.value)
    exprs: T.List["IntoExpr"] = dataclasses.field(default_factory=list)
    named_exprs: T.Dict[str, "IntoExpr"] = dataclasses.field(default_factory=dict)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        exprs, named_exprs = _extract_exprs_named_exprs(
            dct["exprs"], dct["named_exprs"]
        )
        return cls(exprs=exprs, named_exprs=named_exprs)

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        exprs, named_exprs = _convert_to_exprs_named_exprs(self.exprs, self.named_exprs)
        return df.with_columns(*exprs, **named_exprs)


dfop_enum_to_klass_mapping[DfopEnum.with_columns.value] = WithColumns


@dataclasses.dataclass
class Head(BaseDfop):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.head.html
    """

    type: str = dataclasses.field(default=DfopEnum.head.value)
    n: int = dataclasses.field(default=5)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(n=dct["n"])

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.head(self.n)


dfop_enum_to_klass_mapping[DfopEnum.head.value] = Head


@dataclasses.dataclass
class Tail(BaseDfop):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.tail.html
    """

    type: str = dataclasses.field(default=DfopEnum.tail.value)
    n: int = dataclasses.field(default=5)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(n=dct["n"])

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.tail(self.n)


dfop_enum_to_klass_mapping[DfopEnum.tail.value] = Tail


@dataclasses.dataclass
class Sort(BaseDfop):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.sort.html#
    """

    type: str = dataclasses.field(default=DfopEnum.sort.value)
    by: T.List["IntoExpr"] = dataclasses.field(default=REQUIRED)
    descending: T.Union[bool, T.List[bool]] = dataclasses.field(default=False)
    nulls_last: T.Union[bool, T.List[bool]] = dataclasses.field(default=False)
    multithreaded: bool = dataclasses.field(default=True)
    maintain_order: bool = dataclasses.field(default=False)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            by=[
                utils_expr.to_jsonpolars_into_expr(expr_like) for expr_like in dct["by"]
            ],
            descending=dct["descending"],
            nulls_last=dct["nulls_last"],
            multithreaded=dct["multithreaded"],
            maintain_order=dct["maintain_order"],
        )

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.sort(
            *[utils_expr.to_polars_into_expr(expr_like) for expr_like in self.by],
            descending=self.descending,
            nulls_last=self.nulls_last,
            multithreaded=self.multithreaded,
            maintain_order=self.maintain_order,
        )


dfop_enum_to_klass_mapping[DfopEnum.sort.value] = Sort


@dataclasses.dataclass
class DropNulls(BaseDfop):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.drop_nulls.html
    """

    type: str = dataclasses.field(default=DfopEnum.drop_nulls.value)
    subset: T.List["ColumnNameOrSelector"] = dataclasses.field(default=None)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        if dct["subset"] is None:
            subset = None
        else:
            subset, _ = _extract_exprs_named_exprs(dct["subset"], {})
        return cls(subset=subset)

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.drop_nulls(subset=self.subset)


dfop_enum_to_klass_mapping[DfopEnum.drop_nulls.value] = DropNulls
