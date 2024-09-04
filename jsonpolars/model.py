# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from .exc import ParamError
from .arg import _REQUIRED, REQ, rm_na, T_KWARGS


@dataclasses.dataclass
class BaseModel:
    def _validate(self):
        for field in dataclasses.fields(self.__class__):
            if field.init:
                k = field.name
                if getattr(self, k) is REQ:  # pragma: no cover
                    raise ParamError(f"Field {k!r} is required for {self.__class__}.")

    def __post_init__(self):
        self._validate()

    def to_dict(self) -> T_KWARGS:
        raise NotImplementedError

    @classmethod
    def from_dict(cls, dct: T_KWARGS):
        raise NotImplementedError

    @classmethod
    def _split_req_opt(cls, kwargs: T_KWARGS) -> T.Tuple[T_KWARGS, T_KWARGS]:
        req_kwargs, opt_kwargs = dict(), dict()
        for field in dataclasses.fields(cls):
            if isinstance(field.default, _REQUIRED):
                try:
                    req_kwargs[field.name] = kwargs[field.name]
                except KeyError:
                    raise ParamError(
                        f"{field.name!r} is a required parameter for {cls}!"
                    )
            else:
                try:
                    opt_kwargs[field.name] = kwargs[field.name]
                except KeyError:
                    pass
        opt_kwargs = rm_na(**opt_kwargs)
        return req_kwargs, opt_kwargs
