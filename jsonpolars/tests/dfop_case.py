# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl
from rich import print as rprint

from ..base_dfop import parse_dfop

if T.TYPE_CHECKING:  # pragma: no cover
    from ..dfop.api import T_DFOP


@dataclasses.dataclass
class Case:
    input_records: T.List[T.Dict[str, T.Any]] = dataclasses.field()
    dfop: "T_DFOP" = dataclasses.field()
    output_records: T.List[T.Dict[str, T.Any]] = dataclasses.field()

    def run_test(self):

        print("---------- input_records ----------")
        rprint(self.input_records)
        print("---------- dfop ----------")
        rprint(self.dfop)
        df = pl.DataFrame(self.input_records)
        df1 = self.dfop.to_polars(df)
        records = df1.to_dicts()
        print("---------- records ----------")
        rprint(records)
        print("---------- output_records ----------")
        rprint(self.output_records)
        assert records == self.output_records

        dfop_data = self.dfop.to_dict()
        print("---------- dfop_data ----------")
        rprint(dfop_data)
        dfop1 = parse_dfop(dfop_data)
        print("---------- dfop1 ----------")
        rprint(dfop1)
        df1 = self.dfop.to_polars(df)
        records = df1.to_dicts()
        print("---------- records ----------")
        rprint(records)
        print("---------- output_records ----------")
        rprint(self.output_records)
        assert records == self.output_records
