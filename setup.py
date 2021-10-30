# python -iB tests.py
# update README.md
# update version number in setuptools.setup
# git commit and push
# pip install electronvolt -U
# test module in home directory or on mybinder.org

import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="electronvolt",
    version="1.4.2",
    author_email="lw7jz@virginia.edu",
    description="A physics quantity calculator with units.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dw61/electronvolt",
    py_modules=["electronvolt"],
    python_requires='>=3.6',
)
