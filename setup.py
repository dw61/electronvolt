# test electronvolt.py with atom script
# python -i electronvolt.py
# update README.md
# update version number in setuptools.setup
# rm -r __pycache__
# python setup.py sdist bdist_wheel
# twine upload dist/*
# rm -r build dist *.egg-info
# pip install electronvolt -U
# git commit and push
# pypi.org/project/electronvolt
# github.com/dw61/electronvolt
# test module in home directory or on mybinder.org

import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="electronvolt",
    version="1.3.8",
    author_email="lw7jz@virginia.edu",
    description="A physical quantity calculator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dw61/electronvolt",
    py_modules=["electronvolt"],
    python_requires='>=3.6',
)
