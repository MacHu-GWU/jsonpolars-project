# -*- coding: utf-8 -*-

from jsonpolars.expr import api as expr
from jsonpolars.tests.expr_case import Case

data = {"id": 1, "name": "Alice", "profile": {"ssn": "1234567890"}}
case_field_1 = Case(
    input_records=[
        {"data": data},
    ],
    expr=expr.Alias(
        expr=expr.StructField(
            expr=expr.Struct(
                expr=expr.Column(name="data"),
            ),
            name="id",
        ),
        name="res",
    ),
    expected_output_records=[
        {"data": data, "res": 1},
    ],
)
case_field_2 = Case(
    input_records=[
        {"data": data},
    ],
    expr=expr.Alias(
        expr=expr.StructField(
            expr=expr.Column(name="data"),
            name="id",
        ),
        name="res",
    ),
    expected_output_records=[
        {"data": data, "res": 1},
    ],
)
case_field_3 = Case(
    input_records=[
        {"data": data},
    ],
    expr=expr.StructField(
        expr=expr.Column(name="data"),
        name=["id", "name"],
    ),
    expected_output_records=[
        {"data": data, "id": 1, "name": "Alice"},
    ],
)
case_rename_fields_1 = Case(
    input_records=[
        {"data": {"id": 1, "name": "Alice"}},
    ],
    expr=expr.StructRenameFields(
        expr=expr.Column(name="data"),
        names=["user_id", "user_name"],
    ),
    expected_output_records=[
        {"data": {"user_id": 1, "user_name": "Alice"}},
    ],
)
case_rename_fields_2 = Case(
    input_records=[
        {"data": {"id": 1, "name": "Alice"}},
    ],
    expr=expr.StructRenameFields(
        expr=expr.Column(name="data"),
        # if number of item in names doesn't match number of fields,
        # it will follow the order of the fields and rename it with the names
        names=["user_name"],
    ),
    expected_output_records=[
        {"data": {"user_name": 1}},
    ],
)
case_with_fields = Case(
    input_records=[
        {"data": {"a": 2, "b": 3}},
    ],
    expr=expr.StructWithFields(
        expr=expr.Column(name="data"),
        exprs=[
            expr.Alias(
                name="c",
                expr=expr.Plus(
                    left=expr.StructField(expr=None, name="a"),
                    right=expr.StructField(expr=None, name="b"),
                ),
            )
        ],
        named_exprs={
            "d": expr.Multiply(
                left=expr.StructField(expr=None, name="a"),
                right=expr.StructField(expr=None, name="b"),
            )
        },
    ),
    expected_output_records=[
        {"data": {"a": 2, "b": 3, "c": 5, "d": 6}},
    ],
)


def test():
    print("")

    case_field_1.run_with_columns_test()
    case_field_2.run_with_columns_test()
    case_field_3.run_with_columns_test()
    case_rename_fields_1.run_with_columns_test()
    case_rename_fields_2.run_with_columns_test()
    case_with_fields.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.struct", preview=False)
