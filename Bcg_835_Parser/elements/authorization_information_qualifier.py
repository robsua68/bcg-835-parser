""" Authorization Information Qualifier """
from typing import Optional

from Bcg_835_Parser.elements import Element


class AuthorizationInformationQualifier(Element):
    """Authorization Information Qualifier"""

    def parser(self, value: str) -> Optional[str]:
        if value == "00":
            value = None

        return value
