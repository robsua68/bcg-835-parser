""" Setup file for bcg-835-parser """
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

install_requires = ["pandas"]

# tests_require = [
#     'pytest'
# ]

setuptools.setup(
    name="bcg-835-parser",
    version="1.8.0",
    author="Roberto Suarez",
    author_email="robsua68@hotmail.com",
    description="B Consulting Group EDI 835 file format parser.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/robsua68/bcg-835-parser",
    packages=setuptools.find_packages(),
    classifiers=[
        "PROGRAMMING LANGUAGE :: PYTHON :: 3.9",
        "LICENSE :: OSI APPROVED :: MIT LICENSE",
        "OPERATING SYSTEM :: OS INDEPENDENT",
    ],
    install_requires=install_requires,
    # tests_require=tests_require,
    python_requires=">=3.9.0",
)
