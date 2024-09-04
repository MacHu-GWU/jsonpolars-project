# -*- coding: utf-8 -*-

import polars as pl
from rich import print as rprint


def struct_1():
    df = pl.DataFrame([{"a": 1, "b": 2, "c": 3}])
    df1 = df.select(
        pl.struct("a", "b").alias("data"),
    )
    rec = df1.to_dicts()[0]
    # print(df1)
    # print(rec)
    assert rec == {"data": {"a": 1, "b": 2}}

    df = pl.DataFrame([{"a": 1, "b": 2, "c": 3}])
    df1 = df.select(
        pl.struct(
            pl.col("a").alias("x"),
            pl.col("b").alias("y"),
        ).alias("data"),
    )
    rec = df1.to_dicts()[0]
    # print(df1)
    # print(rec)
    assert rec == {"data": {"x": 1, "y": 2}}

    df = pl.DataFrame([{"a": 1, "b": 2, "c": 3}])
    df1 = df.select(
        pl.struct(
            x=pl.col("a"),
            y=pl.col("b"),
        ).alias("data"),
    )
    rec = df1.to_dicts()[0]
    # print(df1)
    # print(rec)
    assert rec == {"data": {"x": 1, "y": 2}}

    df = pl.DataFrame([{"data": {"a": 1, "b": 2, "c": 3}}])
    df1 = df.select(
        pl.struct(
            pl.col("data").struct.field("a").alias("x"),
            pl.col("data").struct.field("b").alias("y"),
        ).alias("res"),
    )
    rec = df1.to_dicts()[0]
    # print(df1)
    # print(rec)
    assert rec == {"res": {"x": 1, "y": 2}}

    df = pl.DataFrame([{"data": {"a": 1, "b": 2, "c": 3}}])
    df1 = df.select(
        pl.struct(
            x=pl.col("data").struct.field("a"),
            y=pl.col("data").struct.field("b"),
        ).alias("res"),
    )
    rec = df1.to_dicts()[0]
    # print(df1)
    # print(rec)
    assert rec == {"res": {"x": 1, "y": 2}}

    df = pl.DataFrame([{"data": {"a": 1, "b": 2, "c": 3}}])
    df1 = df.select(
        pl.struct(
            pl.col("data").struct.field("a", "b"),
        ).alias("res"),
    )
    rec = df1.to_dicts()[0]
    # print(df1)
    # print(rec)
    assert rec == {"res": {"a": 1, "b": 2}}


struct_1()
