# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import expr_enum_to_klass_mapping
from ..base_dfop import DfopEnum, BaseDfop, dfop_enum_to_klass_mapping

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_DFOP
    from ..expr.api import T_EXPR


@dataclasses.dataclass
class Select(BaseDfop):
    type: str = dataclasses.field(default=DfopEnum.select.value)
    exprs: T.List["T_EXPR"] = dataclasses.field(default_factory=list)
    named_exprs: T.Dict[str, "T_EXPR"] = dataclasses.field(default_factory=dict)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        exprs = list()
        for dct_expr in dct["exprs"]:
            if isinstance(dct_expr, str):
                exprs.append(dct_expr)
            else:
                exprs.append(
                    expr_enum_to_klass_mapping[dct_expr["type"]].from_dict(dct_expr)
                )
        named_exprs = dict()
        for name, dct_expr in dct["named_exprs"].items():
            if isinstance(dct_expr, str):
                named_exprs[name] = dct_expr
            else:
                named_exprs[name] = expr_enum_to_klass_mapping[
                    dct_expr["type"]
                ].from_dict(dct_expr)
        return cls(exprs=exprs, named_exprs=named_exprs)

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        exprs = list()
        for expr in self.exprs:
            if isinstance(expr, str):
                exprs.append(expr)
            else:
                exprs.append(expr.to_polars())
        named_exprs = dict()
        for name, expr in self.named_exprs.items():
            if isinstance(expr, str):
                named_exprs[name] = expr
            else:
                named_exprs[name] = expr.to_polars()
        return df.select(*exprs, **named_exprs)


dfop_enum_to_klass_mapping[DfopEnum.select.value] = Select


@dataclasses.dataclass
class Rename(BaseDfop):
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
    type: str = dataclasses.field(default=DfopEnum.drop.value)
    columns: T.List[T.Union[str, "T_EXPR"]] = dataclasses.field(default=REQUIRED)
    strict: bool = dataclasses.field(default=True)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        columns = []
        for dct_expr in dct["columns"]:
            if isinstance(dct_expr, str):
                columns.append(dct_expr)
            else:
                columns.append(
                    expr_enum_to_klass_mapping[dct_expr["type"]].from_dict(dct_expr)
                )
        return cls(
            columns=columns,
            strict=dct["strict"],
        )

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        columns = list()
        for col in self.columns:
            if isinstance(col, str):
                columns.append(col)
            else:
                columns.append(col.to_polars())
        return df.drop(*columns, strict=self.strict)


dfop_enum_to_klass_mapping[DfopEnum.drop.value] = Drop
