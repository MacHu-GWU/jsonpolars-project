# -*- coding: utf-8 -*-

from pathlib import Path

dir_python_lib = Path(__file__).absolute().parent
PACKAGE_NAME = dir_python_lib.name

dir_project_root = dir_python_lib.parent

# ------------------------------------------------------------------------------
# Virtual Environment Related
# ------------------------------------------------------------------------------
dir_venv = dir_project_root / ".venv"
dir_venv_bin = dir_venv / "bin"

# virtualenv executable paths
bin_pytest = dir_venv_bin / "pytest"

# test related
dir_htmlcov = dir_project_root / "htmlcov"
path_cov_index_html = dir_htmlcov / "index.html"
dir_unit_test = dir_project_root / "tests"
