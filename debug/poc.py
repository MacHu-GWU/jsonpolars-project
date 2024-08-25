# -*- coding: utf-8 -*-

"""
这个脚本用于测试各种 polars.DataFrame method 和 expression 的效果.
"""

import polars as pl

df = pl.DataFrame(
    [
        {"id": 1, "name": "alice"},
        {"id": 2, "name": "bob"},
    ]
)

df1 = df.with_columns(
    pl.col("id")
)

print(df1)
