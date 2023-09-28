""" Service Loop """
# Import from standard library
from typing import Tuple, Iterator, Optional, List
from warnings import warn

# Local application imports
from Bcg_835_Parser.segments.service import Service as ServiceSegment
from Bcg_835_Parser.segments.claim import Claim as ClaimSegment
from Bcg_835_Parser.segments.date import Date as DateSegment
from Bcg_835_Parser.segments.reference import Reference as ReferenceSegment
from Bcg_835_Parser.segments.amount import Amount as AmountSegment
from Bcg_835_Parser.segments.service_adjustment import (
    ServiceAdjustment as ServiceAdjustmentSegment,
)
from Bcg_835_Parser.segments.remark import Remark as RemarkSegment
from Bcg_835_Parser.segments.utilities import find_identifier
from Bcg_835_Parser.elements.dollars import Dollars


class Service:
    """Service Loop Class"""

    initiating_identifier = ServiceSegment.identification
    terminating_identifier = [
        ServiceSegment.identification,
        ClaimSegment.identification,
        "SE",
    ]

    def __init__(
        self,
        service: ServiceSegment = None,
        dates: List[DateSegment] = None,
        references: List[ReferenceSegment] = None,
        remarks: List[RemarkSegment] = None,
        amount: AmountSegment = None,
        adjustments: List[ServiceAdjustmentSegment] = None,
    ):
        self.service = service
        self.dates = dates if dates else []
        self.references = references if references else []
        self.remarks = remarks if remarks else []
        self.amount = amount
        self.adjustments = adjustments if adjustments else []

    def __repr__(self) -> str:
        return "\n".join(str(item) for item in self.__dict__.items())

    @property
    def allowed_amount(self) -> Optional[Dollars]:
        """ Allowed Amount """
        if self.amount:
            if self.amount.qualifier == "allowed - actual":
                return self.amount.amount

    @property
    def service_date(self) -> Optional[DateSegment]:
        """ Service Date """
        service_date = [d for d in self.dates if d.qualifier == "service"]
        assert len(service_date) <= 1, f"{self.dates}"

        if len(service_date) == 1:
            return service_date[0]

    @property
    def service_period_start(self) -> Optional[str]:
        """ Service Period Start """
        service_period_start = [
            d for d in self.dates if d.qualifier == "service period start"
        ]
        assert len(service_period_start) <= 1, f"{self.dates}"

        if len(service_period_start) == 1:
            return service_period_start[0]
        else:
            return self.service_date

    @property
    def service_period_end(self) -> Optional[str]:
        """ Service Period End """
        service_period_end = [
            d for d in self.dates if d.qualifier == "service period end"
        ]
        assert len(service_period_end) <= 1, f"{self.dates}"

        if len(service_period_end) == 1:
            return service_period_end[0]
        else:
            return self.service_date

    @classmethod
    def build(
        cls, segment: str, segments: Iterator[str]
    ) -> Tuple["Service", Optional[str], Optional[Iterator[str]]]:
        """Build Service Loop Class Method """
        service = Service()
        service.service = ServiceSegment(segment)

        while True:
            try:
                segment = segments.__next__()
                identifier = find_identifier(segment)

                if identifier == DateSegment.identification:
                    date = DateSegment(segment)
                    service.dates.append(date)

                elif identifier == AmountSegment.identification:
                    service.amount = AmountSegment(segment)

                elif identifier == RemarkSegment.identification:
                    remark = RemarkSegment(segment)
                    service.remarks.append(remark)

                elif identifier == ReferenceSegment.identification:
                    reference = ReferenceSegment(segment)
                    service.references.append(reference)

                elif identifier == ServiceAdjustmentSegment.identification:
                    adjustment = ServiceAdjustmentSegment(segment)
                    service.adjustments.append(adjustment)

                else:
                    message = (
                        f"Identifier: {identifier} not handled in service loop."
                    )
                    warn(message)

            except StopIteration:
                return service, None, None

if __name__ == "__main__":
    pass
