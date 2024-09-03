# -*- coding: utf-8 -*-

import typing as T
import enum
import dataclasses

import polars as pl
from .vendor.better_dataclasses import DataClass, T_DATA

from .sentinel import NOTHING, REQUIRED, resolve_kwargs
from .arg import _REQUIRED, REQ, _NOTHING, NA, rm_na, T_KWARGS
from .exc import ParamError

if T.TYPE_CHECKING:  # pragma: no cover
    from .expr.api import T_EXPR


class ExprEnum(str, enum.Enum):
    # Aggregation
    agg = "agg"
    agg_groups = "agg_groups"
    arg_max = "arg_max"
    arg_min = "arg_min"
    agg_count = "agg_count"
    agg_first = "agg_first"
    agg_implode = "agg_implode"
    agg_last = "agg_last"
    agg_len = "agg_len"
    agg_max = "agg_max"
    agg_mean = "agg_mean"
    agg_median = "agg_median"
    agg_min = "agg_min"
    agg_nan_max = "agg_nan_max"
    agg_nan_min = "agg_nan_min"
    agg_product = "agg_product"
    agg_quantile = "agg_quantile"
    agg_std = "agg_std"
    agg_sum = "agg_sum"
    agg_var = "agg_var"
    # Array
    arr = "arr"
    arr_max = "arr_max"
    arr_min = "arr_min"
    arr_median = "arr_median"
    arr_sum = "arr_sum"
    arr_std = "arr_std"
    arr_to_list = "arr_to_list"
    arr_unique = "arr_unique"
    arr_n_unique = "arr_n_unique"
    arr_var = "arr_var"
    arr_all = "arr_all"
    arr_any = "arr_any"
    arr_sort = "arr_sort"
    arr_reverse = "arr_reverse"
    arr_arg_min = "arr_arg_min"
    arr_arg_max = "arr_arg_max"
    arr_get = "arr_get"
    arr_first = "arr_first"
    arr_last = "arr_last"
    arr_join = "arr_join"
    arr_explode = "arr_explode"
    arr_contains = "arr_contains"
    arr_count_matches = "arr_count_matches"
    arr_to_struct = "arr_to_struct"
    arr_shift = "arr_shift"
    # Binary
    binary = "binary"
    binary_contains = "binary_contains"
    binary_decode = "binary_decode"
    binary_encode = "binary_encode"
    binary_ends_with = "binary_ends_with"
    binary_size = "binary_size"
    binary_starts_with = "binary_starts_with"
    # Boolean
    # Categories
    # Columns / names
    column = "column"
    alias = "alias"
    # Computation
    # Functions
    func_all = "func_all"
    func_all_horizontal = "func_all_horizontal"
    func_any = "func_any"
    func_any_horizontal = "func_any_horizontal"
    func_approx_n_unique = "func_approx_n_unique"
    func_arange = "func_arange"
    func_arctan2 = "func_arctan2"
    func_arctan2d = "func_arctan2d"
    func_arg_sort_by = "func_arg_sort_by"
    func_arg_where = "func_arg_where"
    func_business_day_count = "func_business_day_count"
    func_coalesce = "func_coalesce"
    func_concat_list = "func_concat_list"
    func_concat_str = "func_concat_str"
    func_corr = "func_corr"
    func_count = "func_count"
    func_cov = "func_cov"
    func_cum_count = "func_cum_count"
    func_cum_fold = "func_cum_fold"
    func_cum_reduce = "func_cum_reduce"
    func_cum_sum = "func_cum_sum"
    func_cum_sum_horizontal = "func_cum_sum_horizontal"
    func_date = "func_date"
    func_datetime = "func_datetime"
    func_date_range = "func_date_range"
    func_date_ranges = "func_date_ranges"
    func_datetime_range = "func_datetime_range"
    func_datetime_ranges = "func_datetime_ranges"
    func_duration = "func_duration"
    func_element = "func_element"
    func_exclude = "func_exclude"
    func_first = "func_first"
    func_fold = "func_fold"
    func_format = "func_format"
    func_from_epoch = "func_from_epoch"
    func_groups = "func_groups"
    func_head = "func_head"
    func_implode = "func_implode"
    func_int_range = "func_int_range"
    func_int_ranges = "func_int_ranges"
    func_last = "func_last"
    func_len = "func_len"
    func_lit = "func_lit"
    func_map_batches = "func_map_batches"
    func_map_groups = "func_map_groups"
    func_max = "func_max"
    func_max_horizontal = "func_max_horizontal"
    func_mean = "func_mean"
    func_mean_horizontal = "func_mean_horizontal"
    func_median = "func_median"
    func_min = "func_min"
    func_min_horizontal = "func_min_horizontal"
    func_n_unique = "func_n_unique"
    func_nth = "func_nth"
    func_ones = "func_ones"
    func_quantile = "func_quantile"
    func_reduce = "func_reduce"
    func_repeat = "func_repeat"
    func_rolling_corr = "func_rolling_corr"
    func_rolling_cov = "func_rolling_cov"
    func_select = "func_select"
    func_std = "func_std"
    func_struct = "func_struct"
    func_sum = "func_sum"
    func_sum_horizontal = "func_sum_horizontal"
    func_sql = "func_sql"
    func_sql_expr = "func_sql_expr"
    func_tail = "func_tail"
    func_time = "func_time"
    func_time_range = "func_time_range"
    func_time_ranges = "func_time_ranges"
    func_var = "func_var"
    func_when = "func_when"
    func_zeros = "func_zeros"
    # plus = "plus"
    # minus = "minus"
    # multiple = "multiple"
    # divide = "divide"
    # List
    list = "list"
    list_all = "list_all"
    list_any = "list_any"
    list_drop_nulls = "list_drop_nulls"
    list_arg_max = "list_arg_max"
    list_arg_min = "list_arg_min"
    list_concat = "list_concat"
    list_contains = "list_contains"
    list_count_matches = "list_count_matches"
    list_diff = "list_diff"
    list_eval = "list_eval"
    list_explode = "list_explode"
    list_first = "list_first"
    list_gather = "list_gather"
    list_get = "list_get"
    list_head = "list_head"
    list_join = "list_join"
    list_last = "list_last"
    list_len = "list_len"
    list_max = "list_max"
    list_mean = "list_mean"
    list_median = "list_median"
    list_min = "list_min"
    list_reverse = "list_reverse"
    list_sample = "list_sample"
    list_set_difference = "list_set_difference"
    list_set_intersection = "list_set_intersection"
    list_set_symmetric_difference = "list_set_symmetric_difference"
    list_set_union = "list_set_union"
    list_shift = "list_shift"
    list_slice = "list_slice"
    list_sort = "list_sort"
    list_std = "list_std"
    list_sum = "list_sum"
    list_tail = "list_tail"
    list_to_array = "list_to_array"
    list_to_struct = "list_to_struct"
    list_unique = "list_unique"
    list_n_unique = "list_n_unique"
    list_var = "list_var"
    list_gather_every = "list_gather_every"
    # Manipulation / selection
    append = "append"
    arg_sort = "arg_sort"
    arg_true = "arg_true"
    backward_fill = "backward_fill"
    bottom_k = "bottom_k"
    bottom_k_by = "bottom_k_by"
    cast = "cast"
    ceil = "ceil"
    clip = "clip"
    cut = "cut"
    drop_nans = "drop_nans"
    drop_nulls = "drop_nulls"
    explode = "explode"
    extend_constant = "extend_constant"
    fill_nan = "fill_nan"
    fill_null = "fill_null"
    filter = "filter"
    flatten = "flatten"
    floor = "floor"
    forward_fill = "forward_fill"
    gather = "gather"
    gather_every = "gather_every"
    get = "get"
    head = "head"
    inspect = "inspect"
    interpolate = "interpolate"
    interpolate_by = "interpolate_by"
    limit = "limit"
    lower_bound = "lower_bound"
    pipe = "pipe"
    qcut = "qcut"
    rechunk = "rechunk"
    reinterpret = "reinterpret"
    repeat_by = "repeat_by"
    replace = "replace"
    replace_strict = "replace_strict"
    reshape = "reshape"
    reverse = "reverse"
    rle = "rle"
    rle_id = "rle_id"
    round = "round"
    round_sig_figs = "round_sig_figs"
    sample = "sample"
    shift = "shift"
    shrink_dtype = "shrink_dtype"
    shuffle = "shuffle"
    slice = "slice"
    sort = "sort"
    sort_by = "sort_by"
    tail = "tail"
    to_physical = "to_physical"
    top_k = "top_k"
    top_k_by = "top_k_by"
    upper_bound = "upper_bound"
    where = "where"
    # Meta
    # Miscellaneous
    # Name
    # Operators
    and_ = "and"
    or_ = "or"
    eq = "eq"
    eq_missing = "eq_missing"
    ge = "ge"
    gt = "gt"
    le = "le"
    lt = "lt"
    ne = "ne"
    ne_missing = "ne_missing"
    add = "add"
    floordiv = "floordiv"
    mod = "mod"
    mul = "mul"
    neg = "neg"
    sub = "sub"
    truediv = "truediv"
    pow = "pow"
    xor = "xor"
    # String
    string = "string"
    str_concat = "str_concat"
    str_contains = "str_contains"
    str_contains_any = "str_contains_any"
    str_count_matches = "str_count_matches"
    str_decode = "str_decode"
    str_encode = "str_encode"
    str_ends_with = "str_ends_with"
    str_explode = "str_explode"
    str_extract = "str_extract"
    str_extract_all = "str_extract_all"
    str_extract_groups = "str_extract_groups"
    str_extract_many = "str_extract_many"
    str_find = "str_find"
    str_head = "str_head"
    str_join = "str_join"
    str_json_decode = "str_json_decode"
    str_json_path_match = "str_json_path_match"
    str_len_bytes = "str_len_bytes"
    str_len_chars = "str_len_chars"
    str_pad_end = "str_pad_end"
    str_pad_start = "str_pad_start"
    str_replace = "str_replace"
    str_replace_all = "str_replace_all"
    str_replace_many = "str_replace_many"
    str_reverse = "str_reverse"
    str_slice = "str_slice"
    str_split = "str_split"
    str_split_exact = "str_split_exact"
    str_splitn = "str_splitn"
    str_starts_with = "str_starts_with"
    str_strip_chars = "str_strip_chars"
    str_strip_chars_start = "str_strip_chars_start"
    str_strip_chars_end = "str_strip_chars_end"
    str_strip_prefix = "str_strip_prefix"
    str_strip_suffix = "str_strip_suffix"
    str_strptime = "str_strptime"
    str_tail = "str_tail"
    str_to_date = "str_to_date"
    str_to_datetime = "str_to_datetime"
    str_to_decimal = "str_to_decimal"
    str_to_integer = "str_to_integer"
    str_to_lowercase = "str_to_lowercase"
    str_to_titlecase = "str_to_titlecase"
    str_to_time = "str_to_time"
    str_to_uppercase = "str_to_uppercase"
    str_zfill = "str_zfill"
    # Struct
    struct = "struct"
    struct_field = "struct_field"
    struct_json_encode = "struct_json_encode"
    struct_rename_fields = "struct_rename_fields"
    struct_with_fields = "struct_with_fields"
    # Temporal
    dt = "datetime"
    dt_add_business_days = "dt_add_business_days"
    dt_base_utc_offset = "dt_base_utc_offset"
    dt_cast_time_unit = "dt_cast_time_unit"
    dt_century = "dt_century"
    dt_combine = "dt_combine"
    dt_convert_time_zone = "dt_convert_time_zone"
    dt_date = "dt_date"
    dt_datetime = "dt_datetime"
    dt_day = "dt_day"
    dt_dst_offset = "dt_dst_offset"
    dt_epoch = "dt_epoch"
    dt_hour = "dt_hour"
    dt_is_leap_year = "dt_is_leap_year"
    dt_iso_year = "dt_iso_year"
    dt_microsecond = "dt_microsecond"
    dt_millennium = "dt_millennium"
    dt_millisecond = "dt_millisecond"
    dt_minute = "dt_minute"
    dt_month = "dt_month"
    dt_month_end = "dt_month_end"
    dt_month_start = "dt_month_start"
    dt_nanosecond = "dt_nanosecond"
    dt_offset_by = "dt_offset_by"
    dt_ordinal_day = "dt_ordinal_day"
    dt_quarter = "dt_quarter"
    dt_replace_time_zone = "dt_replace_time_zone"
    dt_round = "dt_round"
    dt_second = "dt_second"
    dt_strftime = "dt_strftime"
    dt_time = "dt_time"
    dt_timestamp = "dt_timestamp"
    dt_to_string = "dt_to_string"
    dt_total_days = "dt_total_days"
    dt_total_hours = "dt_total_hours"
    dt_total_microseconds = "dt_total_microseconds"
    dt_total_milliseconds = "dt_total_milliseconds"
    dt_total_minutes = "dt_total_minutes"
    dt_total_nanoseconds = "dt_total_nanoseconds"
    dt_total_seconds = "dt_total_seconds"
    dt_truncate = "dt_truncate"
    dt_week = "dt_week"
    dt_weekday = "dt_weekday"
    dt_with_time_unit = "dt_with_time_unit"
    dt_year = "dt_year"
    # Window


# def to_dict(inst) -> "T_DATA":
#     """
#     Convert an instance of ``BaseExpr`` to a dict. This dict can be used in
#     ``BaseExpr.from_dict`` method to create a identical instance of the original
#     ``BaseExpr`` instance.
#     """
#     if isinstance(inst, BaseExpr):
#         kwargs = dict()
#         for field in dataclasses.fields(inst.__class__):
#             value = getattr(inst, field.name)
#             kwargs[field.name] = to_dict(value)
#         return rm_na(**kwargs)
#     elif isinstance(inst, (tuple, list)):
#         return type(inst)([to_dict(v) for v in inst])
#     elif isinstance(inst, dict):
#         kwargs = {k: to_dict(v) for k, v in inst.items()}
#         return rm_na(**kwargs)
#     else:
#         return inst

def to_dict(inst) -> "T_DATA":
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
class BaseExpr(DataClass):
    type: str = dataclasses.field(default=REQ)

    def _validate(self):
        for field in dataclasses.fields(self.__class__):
            if field.init:
                k = field.name
                if getattr(self, k) is REQ:  # pragma: no cover
                    raise ParamError(f"Field {k!r} is required for {self.__class__}.")

    def __post_init__(self):
        self._validate()

    # def to_dict(self) -> T_KWARGS:
    #     """
    #     Convert an instance of ``BaseExpr`` to a dict. This dict can be used in
    #     ``BaseExpr.from_dict`` method to create a identical instance of the original
    #     ``BaseExpr`` instance.
    #     """
    #     return to_dict(self)

    def to_dict(self) -> T_KWARGS:
        kwargs = dict()
        for field in dataclasses.fields(self.__class__):
            value = getattr(self, field.name)
            kwargs[field.name] = to_dict(value)
            # if isinstance(value, (tuple, list)):
            #     return type(value)([to_dict(v) for v in value])
            # elif isinstance(value, dict):
            #     kwargs = {k: to_dict(v) for k, v in value.items()}
            #     return rm_na(**kwargs)
            # else:
            #     return value

        return rm_na(**kwargs)
    @classmethod
    def from_dict(cls, dct: T_KWARGS):
        """
        Create an instance of ``BaseExpr`` from either a human created dict,
        or a dict created by the ``BaseExpr.to_dict`` method.
        """
        req_kwargs, opt_kwargs = cls._split_req_opt(dct)
        return cls(**req_kwargs, **rm_na(**opt_kwargs))

    @classmethod
    def _split_req_opt(cls, kwargs: T_KWARGS) -> T.Tuple[T_KWARGS, T_KWARGS]:
        req_kwargs, opt_kwargs = dict(), dict()
        for field in dataclasses.fields(cls):
            if isinstance(field.default, _REQUIRED):
                try:
                    req_kwargs[field.name] = kwargs[field.name]
                except KeyError:
                    raise ParamError(
                        f"{field.name!r} is a required parameter for {cls}!"
                    )
            else:
                try:
                    opt_kwargs[field.name] = kwargs[field.name]
                except KeyError:
                    pass
        opt_kwargs = rm_na(**opt_kwargs)
        return req_kwargs, opt_kwargs

    def to_polars(self) -> pl.Expr:
        raise NotImplementedError()


expr_enum_to_klass_mapping: T.Dict[str, T.Type["T_EXPR"]] = dict()


def parse_expr(dct: T.Dict[str, T.Any]) -> "T_EXPR":
    """
    Note: you have to import everything in the :mod:`jsonpolars.expr` module
    to make this work.
    """
    return expr_enum_to_klass_mapping[dct["type"]].from_dict(dct)
