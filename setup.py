""" Setup file for bcg-edi-835-parser """
import setuptools


install_requires = ["pandas"]

# tests_require = [
#     'pytest'
# ]

setuptools.setup(
    name="bcg-edi-835-parser",
    version="1.7.0",
    author="Roberto Suarez",
    author_email="robsua68@hotmail.com",
    description="B Consulting Group EDI 835 file format parser.",
    long_description="B Consulting EDI 835 parser. Extending code from Keiron Stoddart",
    long_description_content_type="text/markdown",
    url="https://github.com/robsua68/bcg-edi-835-parser",
    packages=setuptools.find_packages(),
    classifiers=[
        "PROGRAMMING LANGUAGE :: PYTHON :: 3",
        "LICENSE :: OSI APPROVED :: MIT LICENSE",
        "OPERATING SYSTEM :: OS INDEPENDENT",
    ],
    install_requires=install_requires,
    # tests_require=tests_require,
    python_requires=">=3.11",
)
