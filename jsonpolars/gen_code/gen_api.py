# -*- coding: utf-8 -*-

"""
自动生下列模块中的代码:

- ``jsonpolars/expr/api.py``
- ``jsonpolars/dfop/api.py``
- ``docs/source/02-Supported-Polars-Expressions/index.rst``
"""

import typing as T
import re
import importlib
import dataclasses

from jinja2 import Template
from jsonpolars.paths import dir_project_root, dir_python_lib
from jsonpolars.base_expr import BaseExpr
from jsonpolars.base_dfop import BaseDfop


@dataclasses.dataclass
class Klass:
    module_name: str
    class_name: str
    doc_url: str


dir_expr = dir_python_lib / "expr"
dir_dfop = dir_python_lib / "dfop"


p_ref = r"Ref: https://\S+"


def gen_expr_api() -> T.List[Klass]:
    ignore_file = [
        "__init__.py",
        "api.py",
    ]
    ignore_class_name = [
        "BaseExpr",
    ]
    klass_list = list()
    for path in dir_expr.iterdir():
        if path.name.endswith(".py") and path.name not in ignore_file:
            print(f"extract class from {path.name!r} ...")
            module_name = f"jsonpolars.expr.{path.stem}"
            module_content = path.read_text()
            module = importlib.import_module(module_name)
            for var_name, var_value in module.__dict__.items():
                if isinstance(var_value, type) and issubclass(var_value, BaseExpr):
                    if (f"class {var_name}" in module_content) and (
                        var_name not in ignore_class_name
                    ):
                        print(f"  found class {var_name!r}")
                        res = re.findall(p_ref, var_value.__doc__)
                        if res:
                            doc_url = res[0].split(":", 1)[1].strip()
                        else:
                            doc_url = "https://docs.pola.rs/api/python/stable/reference/expressions/index.html"
                        klass = Klass(
                            module_name=path.stem,
                            class_name=var_name,
                            doc_url=doc_url,
                        )
                        klass_list.append(klass)

    path_tpl = dir_python_lib / "gen_code" / "expr_api.jinja"
    tpl = Template(path_tpl.read_text())
    content = tpl.render(klass_list=klass_list)

    path_api = dir_expr / "api.py"
    path_api.write_text(content)

    return klass_list


def gen_dfop_api() -> T.List[Klass]:
    ignore_file = [
        "__init__.py",
        "api.py",
    ]
    ignore_class_name = [
        "BaseDfop",
    ]
    klass_list = list()
    for path in dir_dfop.iterdir():
        if path.name.endswith(".py") and path.name not in ignore_file:
            print(f"extract class from {path.name!r} ...")
            module_name = f"jsonpolars.dfop.{path.stem}"
            module_content = path.read_text()
            module = importlib.import_module(module_name)
            for var_name, var_value in module.__dict__.items():
                if isinstance(var_value, type) and issubclass(var_value, BaseDfop):
                    if (f"class {var_name}" in module_content) and (
                        var_name not in ignore_class_name
                    ):
                        print(f"  found class {var_name!r}")
                        res = re.findall(p_ref, var_value.__doc__)
                        if res:
                            doc_url = res[0].split(":", 1)[1].strip()
                        else:
                            doc_url = "https://docs.pola.rs/api/python/stable/reference/dataframe/index.html"
                        klass = Klass(
                            module_name=path.stem,
                            class_name=var_name,
                            doc_url=doc_url,
                        )
                        klass_list.append(klass)

    path_tpl = dir_python_lib / "gen_code" / "dfop_api.jinja"
    tpl = Template(path_tpl.read_text())
    content = tpl.render(klass_list=klass_list)

    path_api = dir_dfop / "api.py"
    path_api.write_text(content)

    return klass_list


def gen_supported_polars_expression_doc(
    expr_klass_list: T.List[Klass],
    dfop_klass_list: T.List[Klass],
):
    path_tpl = dir_python_lib / "gen_code" / "supported_polars_expressions.jinja"
    tpl = Template(path_tpl.read_text())
    content = tpl.render(
        expr_klass_list=expr_klass_list,
        dfop_klass_list=dfop_klass_list,
    )
    path_doc = (
        dir_project_root
        / "docs"
        / "source"
        / "02-Supported-Polars-Expressions"
        / "index.rst"
    )
    path_doc.write_text(content)


expr_klass_list = gen_expr_api()
dfop_klass_list = gen_dfop_api()
gen_supported_polars_expression_doc(expr_klass_list, dfop_klass_list)
