# -*- coding: utf-8 -*-

import polars as pl

from jsonpolars.api import expr, dfop

df = pl.DataFrame(
    [
        {"id": 1, "firstname": "Alice", "lastname": "Smith"},
        {"id": 2, "firstname": "Bob", "lastname": "Johnson"},
        {"id": 3, "firstname": "Cathy", "lastname": "Williams"},
    ]
)

op = dfop.WithColumns(
    exprs=[
        expr.Alias(
            name="fullname",
            expr=expr.Plus(
                left=expr.Column(name="firstname"),
                right=expr.Plus(
                    left=expr.Lit(value=" "),
                    right=expr.Column(name="lastname"),
                ),
            ),
        )
    ]
)

df1 = op.to_polars(df)
print(df1)

print(op.to_dict())