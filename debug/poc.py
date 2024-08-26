# -*- coding: utf-8 -*-

"""
这个脚本用于测试各种 polars.DataFrame method 和 expression 的效果.
"""

import polars as pl

df = pl.DataFrame(
    [
        {"data": {"x": 2, "y": 3}},
    ]
)

df1 = df.with_columns(
    pl.col("data").struct.with_fields(
        z=pl.field("x") * pl.field("y")
    ),
)

print(df1)
