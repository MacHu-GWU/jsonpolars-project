# -*- coding: utf-8 -*-

"""
This test case also an example to show how to implement the dataclass model correctly.
"""

import typing as T
import dataclasses
from datetime import datetime

import pytest

from jsonpolars.exc import ParamError
from jsonpolars.arg import REQ, NA, rm_na, T_KWARGS
from jsonpolars.base_expr import BaseExpr, parse_expr, expr_enum_to_klass_mapping


@dataclasses.dataclass
class Person(BaseExpr):
    type: str = dataclasses.field(default="test_person")
    name: str = dataclasses.field(default=REQ)
    age: int = dataclasses.field(default=20)
    gender: str = dataclasses.field(default=NA)


expr_enum_to_klass_mapping["test_person"] = Person


@dataclasses.dataclass
class Model(BaseExpr):
    type: str = dataclasses.field(default="test_model")
    id: int = dataclasses.field(default=REQ)
    name: str = dataclasses.field(default="my_model")
    create_at: str = dataclasses.field(default=NA)
    person: Person = dataclasses.field(default=REQ)
    person_list: T.List[Person] = dataclasses.field(default_factory=list)
    person_dict: T.Dict[str, Person] = dataclasses.field(default_factory=dict)

    @classmethod
    def from_dict(cls, dct: T_KWARGS):
        req_kwargs, opt_kwargs = cls._split_req_opt(dct)
        req_kwargs["person"] = parse_expr(req_kwargs["person"])
        opt_kwargs["person_list"] = [
            parse_expr(d) for d in opt_kwargs.get("person_list", [])
        ]
        opt_kwargs["person_dict"] = {
            k: parse_expr(v) for k, v in opt_kwargs.get("person_dict", {}).items()
        }
        return cls(**req_kwargs, **rm_na(**opt_kwargs))


expr_enum_to_klass_mapping["test_model"] = Model


@dataclasses.dataclass
class Record(BaseExpr):
    type: str = dataclasses.field(default="test_record")
    create_time: datetime = dataclasses.field(default=REQ)

    def to_dict(self) -> T_KWARGS:
        dct = super().to_dict()
        dct["create_time"] = dct["create_time"].isoformat()
        return dct

    @classmethod
    def from_dict(cls, dct: T_KWARGS):
        return cls(create_time=datetime.fromisoformat(dct["create_time"]))


expr_enum_to_klass_mapping["test_record"] = Record


def test_init():
    # id field is required
    with pytest.raises(ParamError):
        model = Model()

    # person field is required
    with pytest.raises(ParamError):
        model = Model(id=1)


def test_to_dict_from_dict():
    model = Model(
        id=1,
        person=Person(name="Alice"),
        person_list=[Person(name="Bob")],
        person_dict={"c": Person(name="Cathy")},
    )
    assert model.create_at == NA
    dct = model.to_dict()
    assert dct == {
        "type": "test_model",
        "id": 1,
        "name": "my_model",
        "person": {"type": "test_person", "name": "Alice", "age": 20},
        "person_list": [{"type": "test_person", "name": "Bob", "age": 20}],
        "person_dict": {"c": {"type": "test_person", "name": "Cathy", "age": 20}},
    }

    model1 = Model.from_dict(dct)
    assert model1 == model

    req_kwargs, opt_kwargs = Model._split_req_opt(dct)
    assert req_kwargs == {
        "id": 1,
        "person": {"type": "test_person", "name": "Alice", "age": 20},
    }
    assert opt_kwargs == {
        "type": "test_model",
        "name": "my_model",
        "person_list": [{"type": "test_person", "name": "Bob", "age": 20}],
        "person_dict": {"c": {"type": "test_person", "name": "Cathy", "age": 20}},
    }

    with pytest.raises(ParamError):
        Model._split_req_opt({})


class TestRecord:
    def test_to_dict_from_dict(self):
        record = Record(create_time=datetime(2000, 1, 1))
        dct = record.to_dict()
        assert dct == {"type": "test_record", "create_time": "2000-01-01T00:00:00"}

        record1 = Record.from_dict(dct)
        assert record1 == record


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.base_expr", preview=False)
