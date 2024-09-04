# -*- coding: utf-8 -*-

import copy
from jsonpolars.arg import REQ, NA, rm_na


def test_sentinel():
    for obj in [REQ, NA]:
        assert (obj == 1) is False
        assert ("a" == obj) is False
        assert (obj == [1, 2]) is False
        assert ({"a": 1} == obj) is False
        assert (obj == obj) is True
        assert (obj == copy.deepcopy(obj)) is True
        assert (copy.deepcopy(obj) == obj) is True

    assert (REQ != NA) is True
    assert (REQ == NA) is False


def test_rm_na():
    kwargs = {"a": 1, "b": NA}
    assert rm_na(**kwargs) == {"a": 1}


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.arg", preview=False)
