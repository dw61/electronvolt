# test electronvolt.py using command I
# update README.md
# update version number in setuptools.setup
# python setup.py sdist bdist_wheel
# twine upload dist/*
# rm -r build dist *.egg-info
# pip install electronvolt -U
# test module in nteract
# git commit and push
# https://pypi.org/project/electronvolt
# https://github.com/dw61/electronvolt

import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="electronvolt",
    version="0.1.1",
    author_email="lw7jz@virginia.edu",
    description="A physical quantity calculator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dw61/electronvolt",
    py_modules=["electronvolt"],
    python_requires='>=3.6',
)
