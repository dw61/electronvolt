import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mevpc2",
    version="0.0.1",
    author="Diego Wang",
    author_email="lw7jz@virginia.edu",
    description="A physical quantity calculator with units",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DiegoWang51/modern",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
