# git pull
# jupyter nbconvert --clear-output --inplace hbar.ipynb
# jupyter nbconvert --to script hbar.ipynb
# test hbar.py
# update README.md
# update version number in setuptools.setup
# python setup.py sdist bdist_wheel
# twine upload dist/*
# rm -r build dist *.egg-info .ipynb_checkpoints
# pip install hbar -U
# test module at home directory
# git commit and push
# check on https://pypi.org/project/hbar
# check on https://github.com/DiegoWang51/hbar

import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="hbar",
    version="0.1.3",
    author_email="lw7jz@virginia.edu",
    description="A physical quantity calculator with units.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DiegoWang51/hbar",
    py_modules=["hbar"],
    python_requires='>=3.6',
)
