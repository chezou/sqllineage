from setuptools import find_packages, setup

from sqllineage import NAME, VERSION

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    author="Reata",
    author_email="reddevil.hjw@gmail.com",
    description="SQL Lineage Analysis Tool powered by Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/reata/sqllineage",
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    python_requires=">=3.6",
    install_requires=["sqlparse>=0.3.0,<0.4", "networkx>=2.4,<3.0"],
    entry_points={"console_scripts": ["sqllineage = sqllineage.runner:main"]},
    extras_require={
        "all": ["matplotlib", "pygraphviz"],
        "ci": [
            "bandit",
            "flake8",
            "flake8-blind-except",
            "flake8-builtins",
            "flake8-import-order",
            "flake8-logging-format",
            "mypy",
            "pytest>=4.5.0,<5.0",
            "pytest-cov",
            "tox>=3.11.0,<4.0",
            "twine",
            "wheel",
        ],
    },
)
