# -*- coding: utf-8 -*-

import polars as pl
from jsonpolars.api import parse_dfop

df = pl.DataFrame(
    [
        {"id": 1, "firstname": "Alice", "lastname": "Smith"},
        {"id": 2, "firstname": "Bob", "lastname": "Johnson"},
        {"id": 3, "firstname": "Cathy", "lastname": "Williams"},
    ]
)
dfop_data = {
    "type": "with_columns",
    "exprs": [
        {
            "type": "alias",
            "name": "fullname",
            "expr": {
                "type": "plus",
                "left": {"type": "column", "name": "firstname"},
                "right": {
                    "type": "plus",
                    "left": {
                        "type": "lit",
                        "value": " ",
                    },
                    "right": {"type": "column", "name": "lastname"},
                },
            },
        }
    ],
    "named_exprs": {},
}
op = parse_dfop(dfop_data)
df1 = op.to_polars(df)
print(df1)
