# -*- coding: utf-8 -*-

"""
自动生成 api.py 模块.
"""

import importlib
import dataclasses

from jinja2 import Template
from jsonpolars.paths import dir_python_lib
from jsonpolars.base_expr import BaseExpr
from jsonpolars.base_dfop import BaseDfop


@dataclasses.dataclass
class Klass:
    module_name: str
    class_name: str


dir_expr = dir_python_lib / "expr"
dir_dfop = dir_python_lib / "dfop"


def gen_expr_api():
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
                        klass = Klass(
                            module_name=path.stem,
                            class_name=var_name,
                        )
                        klass_list.append(klass)

    path_tpl = dir_python_lib / "gen_code" / "expr_api.jinja"
    tpl = Template(path_tpl.read_text())
    content = tpl.render(klass_list=klass_list)

    path_api = dir_expr / "api.py"
    path_api.write_text(content)


def gen_dfop_api():
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
                        klass = Klass(
                            module_name=path.stem,
                            class_name=var_name,
                        )
                        klass_list.append(klass)

    path_tpl = dir_python_lib / "gen_code" / "dfop_api.jinja"
    tpl = Template(path_tpl.read_text())
    content = tpl.render(klass_list=klass_list)

    path_api = dir_dfop / "api.py"
    path_api.write_text(content)


gen_expr_api()
gen_dfop_api()
