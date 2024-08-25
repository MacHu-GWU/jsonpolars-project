# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..expr import api as expr
from ..base_dfop import DfopEnum, BaseDfop, dfop_enum_to_klass_mapping

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_DFOP
    from ..expr.api import T_EXPR
    from ..typehint import IntoExpr, ColumnNameOrSelector


@dataclasses.dataclass
class Count(BaseDfop):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.count.html
    """

    type: str = dataclasses.field(default=DfopEnum.count.value)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls()

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.count()


dfop_enum_to_klass_mapping[DfopEnum.count.value] = Count

