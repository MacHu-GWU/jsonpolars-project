# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..arg import REQ, NA, rm_na, T_KWARGS
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR


def ensure_list(expr: "T_EXPR") -> pl.Expr:
    if isinstance(expr, List):
        return expr.to_polars()
    else:
        return expr.to_polars().list


@dataclasses.dataclass
class List(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/list.html
    """

    type: str = dataclasses.field(default=ExprEnum.list.value)
    expr: "T_EXPR" = dataclasses.field(default=REQ)

    @classmethod
    def from_dict(cls, dct: T_KWARGS):
        return cls(
            expr=parse_expr(dct["expr"]),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_list(self.expr)


expr_enum_to_klass_mapping[ExprEnum.list.value] = List


@dataclasses.dataclass
class ListGet(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.list.get.html#polars.Expr.list.get
    """

    type: str = dataclasses.field(default=ExprEnum.list_get.value)
    expr: "T_EXPR" = dataclasses.field(default=REQ)
    index: T.Union[int, "T_EXPR"] = dataclasses.field(default=REQ)
    null_on_oob: bool = dataclasses.field(default=NA)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        req_kwargs, opt_kwargs = cls._split_req_opt(dct)
        req_kwargs["expr"] = parse_expr(req_kwargs["expr"])
        index = req_kwargs["index"]
        if isinstance(index, int):
            pass
        elif isinstance(index, dict):
            req_kwargs["index"] = parse_expr(index)
        else:  # pragma: no cover
            raise ValueError(f"Unknown index type: {index}")
        return cls(**req_kwargs, **rm_na(**opt_kwargs))

    def to_polars(self) -> pl.Expr:
        expr = ensure_list(self.expr)
        if isinstance(self.index, int):
            index = self.index
        elif isinstance(self.index, BaseExpr):
            index = self.index.to_polars()
        else:  # pragma: no cover
            raise NotImplementedError("IMPOSSIBLE TO REACH HERE!")
        return expr.get(index=index, **rm_na(null_on_oob=self.null_on_oob))


expr_enum_to_klass_mapping[ExprEnum.list_get.value] = ListGet


@dataclasses.dataclass
class ListEval(BaseExpr):
    """
    Ref: https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.list.eval.html
    """

    type: str = dataclasses.field(default=ExprEnum.list_eval.value)
    expr: "T_EXPR" = dataclasses.field(default=REQ)
    expr_to_run: "T_EXPR" = dataclasses.field(default=REQ)
    parallel: bool = dataclasses.field(default=NA)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        req_kwargs, opt_kwargs = cls._split_req_opt(dct)
        req_kwargs["expr"] = parse_expr(req_kwargs["expr"])
        req_kwargs["expr_to_run"] = parse_expr(req_kwargs["expr_to_run"])
        return cls(**req_kwargs, **rm_na(**opt_kwargs))

    def to_polars(self) -> pl.Expr:
        expr = ensure_list(self.expr)
        return expr.eval(self.expr_to_run.to_polars(), **rm_na(parallel=self.parallel))


expr_enum_to_klass_mapping[ExprEnum.list_eval.value] = ListEval
