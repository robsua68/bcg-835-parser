# bcg-edi-835-parser

### bcg-edi-835-parser: a lightweight EDI 835 file parser
This package provides a simple-to-use Python interface to EDI 835 Health Care Claim Payment and Remittance Advice files.

*This package has been modified by Roberto Suarez as an extension of the original package developed by Keiron Stoddart, the company behind is B Consulting Group, an industry leading Consulting and Billing for Home Health Care Agency in Florida, USA.*

*It is necessary to add Claim data in columns, for example: Claim Number, Remark Codes, etc.*

*The original package is made publicly available by Senscio Systems, the company behind the Ibis Program, an industry leading healthcare initiative that helps people take control of their chronic condition management.*

### Installation
Binary installers for the latest released version are at the Python Package Index. Please note that you need to run Python 3.9 or higher to install the bc-edi-835-parser.
```
pip install bcg-edi-835-parser
```
### Usage
To parse an EDI 835 file simply execute the `parse` function.
```python
from bcg_edi_835_parser import parse

path = '~/Desktop/my_edi_file.txt'
transaction_set = parse(path)
```

The `parse` function also works on a directory path.
```python
from bcg_edi_835_parser import parse

path = '~/Desktop/my_directory_of_edi_files'
transaction_sets = parse(path)
```

In both cases, `parse` returns an instance of the `TransactionSets` class. 
This is the class you manipulate depending on your needs. 
For example, say you want to work with the transaction sets data as a `pd.DataFrame`.
```python
from bcg_edi_835_parser import parse

path = '~/Desktop/my_directory_of_edi_files'
transaction_sets = parse(path)

data = transaction_sets.to_dataframe()
```
And then save that `pd.DataFrame` as a `.csv` file.
```python
data.to_csv('~/Desktop/my_edi_file.csv')
```

The complete set of `TransactionSets` functionality can be found by inspecting the `TransactionSets` class found at `edi_parser/transaction_set/transaction_sets.py`

### Tests
Example EDI 835 files can be found in `tests/test_edi_835/files`. To run the tests use `pytest`.
```
python -m pytest
```





