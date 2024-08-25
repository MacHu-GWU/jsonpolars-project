
.. image:: https://readthedocs.org/projects/jsonpolars/badge/?version=latest
    :target: https://jsonpolars.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://github.com/MacHu-GWU/jsonpolars-project/actions/workflows/main.yml/badge.svg
    :target: https://github.com/MacHu-GWU/jsonpolars-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/jsonpolars-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/jsonpolars-project

.. image:: https://img.shields.io/pypi/v/jsonpolars.svg
    :target: https://pypi.python.org/pypi/jsonpolars

.. image:: https://img.shields.io/pypi/l/jsonpolars.svg
    :target: https://pypi.python.org/pypi/jsonpolars

.. image:: https://img.shields.io/pypi/pyversions/jsonpolars.svg
    :target: https://pypi.python.org/pypi/jsonpolars

.. image:: https://img.shields.io/badge/Release_History!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/jsonpolars-project/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/jsonpolars-project

------

.. image:: https://img.shields.io/badge/Link-Document-blue.svg
    :target: https://jsonpolars.readthedocs.io/en/latest/

.. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://jsonpolars.readthedocs.io/en/latest/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/jsonpolars-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/jsonpolars-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/jsonpolars-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/jsonpolars#files


Welcome to ``jsonpolars`` Documentation
==============================================================================
.. image:: https://jsonpolars.readthedocs.io/en/latest/_static/jsonpolars-logo.png
    :target: https://jsonpolars.readthedocs.io/en/latest/

``jsonpolars`` is an innovative Python library designed to bridge the gap between JSON-based data manipulation syntax and the powerful Polars data processing library. This project aims to provide a flexible and intuitive way to express Polars operations using JSON structures, making it easier for developers to work with Polars in various contexts. The library allows users to define complex data transformations using JSON syntax, which can then be translated into native Polars operations.

Example:

.. code-block:: python

    import polars as pl
    from jsonpolars.api import parse_dfop

    df = pl.DataFrame(
        [
            {"id": 1, "firstname": "Alice", "lastname": "Smith"},
            {"id": 2, "firstname": "Bob", "lastname": "Johnson"},
            {"id": 3, "firstname": "Cathy", "lastname": "Williams"},
        ]
    )
    dfop_data = {
        "type": "with_columns",
        "exprs": [
            {
                "type": "alias",
                "name": "fullname",
                "expr": {
                    "type": "plus",
                    "left": {"type": "column", "name": "firstname"},
                    "right": {
                        "type": "plus",
                        "left": {
                            "type": "lit",
                            "value": " ",
                        },
                        "right": {"type": "column", "name": "lastname"},
                    },
                },
            }
        ],
    }
    op = parse_dfop(dfop_data)
    df1 = op.to_polars(df)
    print(df1)

Output:

.. code-block:: python

    shape: (3, 4)
    ┌─────┬───────────┬──────────┬────────────────┐
    │ id  ┆ firstname ┆ lastname ┆ fullname       │
    │ --- ┆ ---       ┆ ---      ┆ ---            │
    │ i64 ┆ str       ┆ str      ┆ str            │
    ╞═════╪═══════════╪══════════╪════════════════╡
    │ 1   ┆ Alice     ┆ Smith    ┆ Alice Smith    │
    │ 2   ┆ Bob       ┆ Johnson  ┆ Bob Johnson    │
    │ 3   ┆ Cathy     ┆ Williams ┆ Cathy Williams │
    └─────┴───────────┴──────────┴────────────────┘


.. _install:

Install
------------------------------------------------------------------------------

``jsonpolars`` is released on PyPI, so all you need is to:

.. code-block:: console

    $ pip install jsonpolars

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade jsonpolars
