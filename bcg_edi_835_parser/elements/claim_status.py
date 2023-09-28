""" Claim Status """
from Bcg_Edi_835_Parser.elements import Element

class ClaimStatus(Element):
    """Claim Status"""

    # Explanation in -- https://x12.org/codes/claim-status-codes

    def parser(self, value: str) -> int:
        return int(value)
