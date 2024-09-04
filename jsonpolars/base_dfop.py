# -*- coding: utf-8 -*-

"""
Base DataFrame operation.
"""

import typing as T
import enum
import dataclasses

import polars as pl
from .model import BaseModel
from .base_expr import BaseExpr

from .exc import ParamError
from .arg import REQ, rm_na, T_KWARGS

if T.TYPE_CHECKING:  # pragma: no cover
    from .dfop.api import T_DFOP


class DfopEnum(str, enum.Enum):
    """ """

    # Aggregation
    count = "count"
    max = "max"
    max_horizontal = "max_horizontal"
    mean = "mean"
    mean_horizontal = "mean_horizontal"
    median = "median"
    min = "min"
    min_horizontal = "min_horizontal"
    product = "product"
    quantile = "quantile"
    std = "std"
    sum = "sum"
    sum_horizontal = "sum_horizontal"
    var = "var"
    # Attributes
    # Computation
    # Descriptive
    # Export
    # GroupBy
    group_by_agg = "group_by_agg"
    group_by_all = "group_by_all"
    group_by_count = "group_by_count"
    group_by_first = "group_by_first"
    group_by_head = "group_by_head"
    group_by_last = "group_by_last"
    group_by_len = "group_by_len"
    group_by_map_groups = "group_by_map_groups"
    group_by_max = "group_by_max"
    group_by_mean = "group_by_mean"
    group_by_median = "group_by_median"
    group_by_min = "group_by_min"
    group_by_n_unique = "group_by_n_unique"
    group_by_quantile = "group_by_quantile"
    group_by_sum = "group_by_sum"
    group_by_tail = "group_by_tail"
    # Manipulation / selection
    bottom_k = "bottom_k"
    cast = "cast"
    clear = "clear"
    clone = "clone"
    drop = "drop"
    drop_in_place = "drop_in_place"
    drop_nulls = "drop_nulls"
    explode = "explode"
    extend = "extend"
    fill_nan = "fill_nan"
    fill_null = "fill_null"
    filter = "filter"
    gather_every = "gather_every"
    get_column = "get_column"
    get_column_index = "get_column_index"
    get_columns = "get_columns"
    group_by = "group_by"
    group_by_dynamic = "group_by_dynamic"
    head = "head"
    hstack = "hstack"
    insert_column = "insert_column"
    interpolate = "interpolate"
    item = "item"
    iter_columns = "iter_columns"
    iter_rows = "iter_rows"
    iter_slices = "iter_slices"
    join = "join"
    join_asof = "join_asof"
    limit = "limit"
    melt = "melt"
    merge_sorted = "merge_sorted"
    partition_by = "partition_by"
    pipe = "pipe"
    pivot = "pivot"
    rechunk = "rechunk"
    rename = "rename"
    replace_column = "replace_column"
    reverse = "reverse"
    rolling = "rolling"
    row = "row"
    rows = "rows"
    rows_by_key = "rows_by_key"
    sample = "sample"
    select = "select"
    select_seq = "select_seq"
    set_sorted = "set_sorted"
    shift = "shift"
    shrink_to_fit = "shrink_to_fit"
    slice = "slice"
    sort = "sort"
    sql = "sql"
    tail = "tail"
    to_dummies = "to_dummies"
    to_series = "to_series"
    top_k = "top_k"
    transpose = "transpose"
    unique = "unique"
    unnest = "unnest"
    unpivot = "unpivot"
    unstack = "unstack"
    update = "update"
    upsample = "upsample"
    vstack = "vstack"
    with_columns = "with_columns"
    with_columns_seq = "with_columns_seq"
    with_row_count = "with_row_count"
    with_row_index = "with_row_index"
    # Miscellaneous
    # Plot
    # Style


def to_dict(inst) -> "T_KWARGS":
    """
    Convert an instance of ``BaseExpr`` to a dict. This dict can be used in
    ``BaseExpr.from_dict`` method to create a identical instance of the original
    ``BaseExpr`` instance.
    """
    if isinstance(inst, BaseExpr):
        return inst.to_dict()
    elif isinstance(inst, (tuple, list)):
        return type(inst)([to_dict(v) for v in inst])
    elif isinstance(inst, dict):
        kwargs = {k: to_dict(v) for k, v in inst.items()}
        return rm_na(**kwargs)
    else:
        return inst


@dataclasses.dataclass
class BaseDfop(BaseModel):
    type: str = dataclasses.field(default=REQ)

    def _validate(self):
        for field in dataclasses.fields(self.__class__):
            if field.init:
                k = field.name
                if getattr(self, k) is REQ:  # pragma: no cover
                    raise ParamError(f"Field {k!r} is required for {self.__class__}.")

    def __post_init__(self):
        self._validate()

    def to_dict(self) -> T_KWARGS:
        kwargs = dict()
        for field in dataclasses.fields(self.__class__):
            value = getattr(self, field.name)
            kwargs[field.name] = to_dict(value)
        return rm_na(**kwargs)

    @classmethod
    def from_dict(cls, dct: T_KWARGS):
        """
        Create an instance of ``BaseExpr`` from either a human created dict,
        or a dict created by the ``BaseExpr.to_dict`` method.
        """
        req_kwargs, opt_kwargs = cls._split_req_opt(dct)
        return cls(**req_kwargs, **rm_na(**opt_kwargs))

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        raise NotImplementedError()


dfop_enum_to_klass_mapping: T.Dict[str, T.Type["T_DFOP"]] = dict()


def parse_dfop(dct: T.Dict[str, T.Any]) -> "T_DFOP":
    """
    Note: you have to import everything in the :mod:`jsonpolars.dfop` module
    to make this work.
    """
    return dfop_enum_to_klass_mapping[dct["type"]].from_dict(dct)
