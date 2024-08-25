# -*- coding: utf-8 -*-

from jsonpolars.expr import api as expr
from jsonpolars.dfop import api as dfop
from jsonpolars.tests.dfop_case import Case


case_count = Case(
    input_records=[
        {"id": 1},
        {"id": 2},
        {"id": 3},
    ],
    dfop=dfop.Count(),
    expected_output_records=[
        {"id": 3},
    ],
)


def test():
    print("")

    case_count.run_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.dfop.aggregation", preview=False)
