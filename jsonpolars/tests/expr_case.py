# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl
from rich import print as rprint

from ..base_expr import parse_expr

if T.TYPE_CHECKING:  # pragma: no cover
    from ..expr.api import T_EXPR


@dataclasses.dataclass
class Case:
    input_records: T.List[T.Dict[str, T.Any]] = dataclasses.field()
    expr: "T_EXPR" = dataclasses.field()
    output_records: T.List[T.Dict[str, T.Any]] = dataclasses.field()

    def run_with_columns_test(self):

        print("---------- input_records ----------")
        rprint(self.input_records)
        print("---------- expr ----------")
        rprint(self.expr)
        df = pl.DataFrame(self.input_records)
        df1 = df.with_columns(self.expr.to_polars())
        records = df1.to_dicts()
        print("---------- records ----------")
        rprint(records)
        print("---------- output_records ----------")
        rprint(self.output_records)
        assert records == self.output_records

        expr_data = self.expr.to_dict()
        print("---------- expr_data ----------")
        rprint(expr_data)
        expr1 = parse_expr(expr_data)
        print("---------- expr1 ----------")
        rprint(expr1)
        df1 = df.with_columns(expr1.to_polars())
        records = df1.to_dicts()
        print("---------- records ----------")
        rprint(records)
        print("---------- output_records ----------")
        rprint(self.output_records)
        assert records == self.output_records
