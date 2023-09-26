import setuptools

install_requires = [
    'pandas'
]

setuptools.setup(
    name="bcg-edi-835-parser",
    version="1.6.0",
    author="Roberto Suarez",
    author_email="robsua68@hotmail.com",
    description="B Consulting Group EDI 835 file format parser.",
    long_description="B Consulting Group EDI 835 file format parser. Extending to code edi-835-parser from Keiron Stoddart",
    long_description_content_type="text/markdown",
    url="https://github.com/robsua68/bcg-edi-835-parser",
    packages=setuptools.find_packages(),
    classifiers=[
        "OPERATING SYSTEM :: OS INDEPENDENT",
        "LICENSE :: OSI APPROVED :: MIT LICENSE",
    ],
    install_requires=install_requires,
    # tests_require=tests_require,
    python_requires='>=3.11',
)