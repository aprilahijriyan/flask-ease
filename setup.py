
import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


# This call to setup() does all the work
setup(
    name="FlaskEase",
    version="0.2.0",
    description="Flask extension for creating REST APIs. You get autogenerated OpenAPI spec (with Redoc and Swagger Docs), Request parsing and validations (query, path, body, form and files) and Response validation.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/zero-shubham/flask-ease",
    author="Shubham Biswas",
    author_email="shubhambiswas.zero@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude=("tests", "example")),
    include_package_data=True,
    install_requires=[
        "flask==1.1.2",
        "pydantic==1.5.1"
    ],
)
