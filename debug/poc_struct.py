# -*- coding: utf-8 -*-

import polars as pl


def struct_field_1():
    df = pl.DataFrame(
        [
            {"data": {"a": 1, "b": 2, "c": 3}},
        ]
    )
    df1 = df.select(pl.col("data").struct.field("a").alias("res"))
    rec = df1.to_dicts()[0]
    # print(df1)
    # print(rec)
    assert rec == {"res": 1}

    df1 = df.select(pl.col("data").struct.field("*"))
    rec = df1.to_dicts()[0]
    # print(df1)
    # print(rec)
    assert rec == {"a": 1, "b": 2, "c": 3}

    df1 = df.select(pl.col("data").struct.field(["a", "b"]))
    rec = df1.to_dicts()[0]
    # print(df1)
    # print(rec)
    assert rec == {"a": 1, "b": 2}

    df1 = df.select(pl.col("data").struct.field("a", "b"))
    rec = df1.to_dicts()[0]
    # print(df1)
    # print(rec)
    assert rec == {"a": 1, "b": 2}

    df1 = df.select(pl.col("data").struct[0].alias("res"))
    rec = df1.to_dicts()[0]
    # print(df1)
    # print(rec)
    assert rec == {"res": 1}


struct_field_1()


def struct_field_2():
    df = pl.DataFrame(
        [
            {
                "id": 1,
                "profile": {
                    "name": "Alice",
                    "address": {
                        "street": "123 Main St",
                        "zipcode": "12345",
                    },
                },
            },
        ]
    )

    df1 = df.select(
        pl.struct(
            pl.struct(
                pl.col("profile")
                .struct.field("address")
                .struct.field("street")
                .alias("street")
            ).alias("address")
        ).alias("profile")
    )
    rec = df1.to_dicts()[0]
    print(df1)
    print(rec)
    assert rec == {"profile": {"address": {"street": "123 Main St"}}}


struct_field_2()
