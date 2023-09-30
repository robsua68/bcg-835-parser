""" Amount Qualifier """
from rsa_835_parser.elements import Element

# https://ushik.ahrq.gov/ViewItemDetails?system=mdr&itemKey=133081000
amount_qualifiers = {
	'B6': 'allowed - actual',
	'AU': 'coverage amount'
}


class AmountQualifier(Element):
    """ Amount Qualifier class """

    def parser(self, value: str) -> str:
        return amount_qualifiers.get(value, value)
