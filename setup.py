# git pull
# update README.md
# update version number in setuptools.setup
# python setup.py sdist bdist_wheel
# twine upload dist/*
# rm -r build dist *.egg-info
# git commit and push
# check on https://pypi.org/project/hbar
# check on https://github.com/DiegoWang51/hbar

import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="hbar",
    version="0.0.5",
    author_email="lw7jz@virginia.edu",
    description="A physical quantity calculator with units.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DiegoWang51/hbar",
    py_modules=["hbar"],
    python_requires='>=3.6',
)
