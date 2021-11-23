# python -iB tests.py
# README.md
# version number at setuptools.setup
# commit, push, merge, pull, delete branch
# pip install electronvolt -U
# test from home directory or on mybinder.org

import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="electronvolt",
    version="1.5.9",
    author_email="lw7jz@virginia.edu",
    description="A physics quantity calculator with units.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dw61/electronvolt",
    py_modules=["electronvolt"],
    python_requires=">=3.6",
)
