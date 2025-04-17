# coding: utf-8

"""
    FlexPrice API

    FlexPrice API Service

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301
import os

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

# Read long description from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

NAME = "flexprice"
VERSION = "1.0.11"
PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "urllib3 >=2.0.0, <3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Official FlexPrice Python SDK",
    author="FlexPrice Team",
    author_email="tech@flexprice.io",
    url="https://github.com/flexprice/python-sdk",
    keywords=["FlexPrice", "Pricing", "API", "SDK", "FlexPrice API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description=long_description,
    package_data={"flexprice": ["py.typed"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Source": "https://github.com/flexprice/python-sdk",
        "Documentation": "https://docs.flexprice.io",
        "Bug Tracker": "https://github.com/flexprice/python-sdk/issues",
    },
    python_requires=PYTHON_REQUIRES,
)