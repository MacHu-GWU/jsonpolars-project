# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..arg import REQ, NA, rm_na, T_KWARGS
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
    def from_dict(cls, dct: T_KWARGS):
        return cls(
            exprs=batch_to_jsonpolars_into_exprs(dct.get("exprs", list())),
            named_exprs=batch_to_jsonpolars_named_into_exprs(
                dct.get("named_exprs", dict())
            ),
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
        default=REQ
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
    columns: T.List["ColumnNameOrSelector"] = dataclasses.field(default=REQ)
    strict: bool = dataclasses.field(default=NA)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            columns=batch_to_jsonpolars_into_exprs(dct["columns"]),
            **rm_na(
                strict=dct.get("strict", NA),
            ),
        )

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.drop(
            *batch_to_polars_into_exprs(self.columns),
            **rm_na(
                strict=self.strict,
            ),
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
    def from_dict(cls, dct: T_KWARGS):
        return cls(
            exprs=batch_to_jsonpolars_into_exprs(dct.get("exprs", list())),
            named_exprs=batch_to_jsonpolars_named_into_exprs(
                dct.get("named_exprs", dict())
            ),
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
    n: int = dataclasses.field(default=NA)

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.head(**rm_na(n=self.n))


dfop_enum_to_klass_mapping[DfopEnum.head.value] = Head


@dataclasses.dataclass
class Tail(BaseDfop):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.tail.html
    """

    type: str = dataclasses.field(default=DfopEnum.tail.value)
    n: int = dataclasses.field(default=NA)

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.tail(**rm_na(n=self.n))


dfop_enum_to_klass_mapping[DfopEnum.tail.value] = Tail


@dataclasses.dataclass
class Sort(BaseDfop):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.sort.html
    """

    type: str = dataclasses.field(default=DfopEnum.sort.value)
    by: T.List["IntoExpr"] = dataclasses.field(default=REQ)
    descending: T.Union[bool, T.List[bool]] = dataclasses.field(default=NA)
    nulls_last: T.Union[bool, T.List[bool]] = dataclasses.field(default=NA)
    multithreaded: bool = dataclasses.field(default=NA)
    maintain_order: bool = dataclasses.field(default=NA)

    @classmethod
    def from_dict(cls, dct: T_KWARGS):
        req_kwargs, opt_kwargs = cls._split_req_opt(dct)
        req_kwargs["by"] = batch_to_jsonpolars_into_exprs(
            batch_to_jsonpolars_into_exprs(dct["by"])
        )
        return cls(**req_kwargs, **rm_na(**opt_kwargs))

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.sort(
            *batch_to_polars_into_exprs(self.by),
            **rm_na(
                descending=self.descending,
                nulls_last=self.nulls_last,
                multithreaded=self.multithreaded,
                maintain_order=self.maintain_order,
            ),
        )


dfop_enum_to_klass_mapping[DfopEnum.sort.value] = Sort


@dataclasses.dataclass
class DropNulls(BaseDfop):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.drop_nulls.html
    """

    type: str = dataclasses.field(default=DfopEnum.drop_nulls.value)
    subset: T.List["ColumnNameOrSelector"] = dataclasses.field(default=NA)

    @classmethod
    def from_dict(cls, dct: T_KWARGS):
        req_kwargs, opt_kwargs = cls._split_req_opt(dct)
        if "subset" in opt_kwargs:
            opt_kwargs["subset"] = batch_to_jsonpolars_into_exprs(opt_kwargs["subset"])
        return cls(**req_kwargs, **rm_na(**opt_kwargs))

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        kwargs = dict()
        if isinstance(self.subset, list):
            kwargs["subset"] = batch_to_polars_into_exprs(self.subset)
        return df.drop_nulls(**kwargs)


dfop_enum_to_klass_mapping[DfopEnum.drop_nulls.value] = DropNulls
