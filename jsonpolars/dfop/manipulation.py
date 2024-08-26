# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..expr import api as expr
from ..utils_expr import (
    batch_to_jsonpolars_into_exprs,
    batch_to_jsonpolars_named_into_exprs,
    batch_to_polars_into_exprs,
    batch_to_polars_named_into_exprs,
)
from ..base_dfop import DfopEnum, BaseDfop, dfop_enum_to_klass_mapping

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_DFOP
    from ..expr.api import T_EXPR
    from ..typehint import IntoExpr, ColumnNameOrSelector


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
        return cls(
            exprs=batch_to_jsonpolars_into_exprs(dct["exprs"]),
            named_exprs=batch_to_jsonpolars_named_into_exprs(dct["named_exprs"]),
        )

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.select(
            *batch_to_polars_into_exprs(self.exprs),
            **batch_to_polars_named_into_exprs(self.named_exprs),
        )


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
        return cls(
            columns=batch_to_jsonpolars_into_exprs(dct["columns"]),
            strict=dct["strict"],
        )

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.drop(
            *batch_to_polars_into_exprs(self.columns),
            strict=self.strict,
        )


dfop_enum_to_klass_mapping[DfopEnum.drop.value] = Drop


@dataclasses.dataclass
class WithColumns(BaseDfop):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.with_columns.html
    """

    type: str = dataclasses.field(default=DfopEnum.with_columns.value)
    exprs: T.List["IntoExpr"] = dataclasses.field(default_factory=list)
    named_exprs: T.Dict[str, "IntoExpr"] = dataclasses.field(default_factory=dict)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            exprs=batch_to_jsonpolars_into_exprs(dct["exprs"]),
            named_exprs=batch_to_jsonpolars_named_into_exprs(dct["named_exprs"]),
        )

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.with_columns(
            *batch_to_polars_into_exprs(self.exprs),
            **batch_to_polars_named_into_exprs(self.named_exprs),
        )


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
    Ref: https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.sort.html
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
            by=batch_to_jsonpolars_into_exprs(dct["by"]),
            descending=dct["descending"],
            nulls_last=dct["nulls_last"],
            multithreaded=dct["multithreaded"],
            maintain_order=dct["maintain_order"],
        )

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.sort(
            *batch_to_polars_into_exprs(self.by),
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
            subset = batch_to_jsonpolars_into_exprs(dct["subset"])
        return cls(subset=subset)

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        if self.subset is None:
            subset = None
        else:
            subset = batch_to_polars_into_exprs(self.subset)
        return df.drop_nulls(subset=subset)


dfop_enum_to_klass_mapping[DfopEnum.drop_nulls.value] = DropNulls
