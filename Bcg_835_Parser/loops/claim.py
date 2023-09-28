""" Claims Loop """
# Imports from standard library
from typing import Iterator, Tuple, Optional, List
from warnings import warn

# Local application imports
from Bcg_835_Parser.segments.claim import Claim as ClaimSegment
from Bcg_835_Parser.segments.entity import Entity as EntitySegment
from Bcg_835_Parser.segments.reference import Reference as ReferenceSegment
from Bcg_835_Parser.segments.date import Date as DateSegment
from Bcg_835_Parser.segments.amount import Amount as AmountSegment
from Bcg_835_Parser.segments.utilities import find_identifier
from Bcg_835_Parser.loops.service import Service as ServiceLoop


class Claim:
    """Claim Loop Class"""

    initiating_identifier = ClaimSegment.identification
    terminating_identifiers = [ClaimSegment.identification, "SE"]

    def __init__(
        self,
        claim: ClaimSegment = None,
        entities: List[EntitySegment] = None,
        services: List[ServiceLoop] = None,
        references: List[ReferenceSegment] = None,
        dates: List[DateSegment] = None,
        amount: AmountSegment = None,
    ):
        self.claim = claim
        self.entities = entities if entities else []
        self.services = services if services else []
        self.references = references if references else []
        self.dates = dates if dates else []
        self.amount = amount

    def __repr__(self) -> str:
        return "\n".join(str(item) for item in self.__dict__.items())

    @property
    def rendering_provider(self) -> Optional[EntitySegment]:
        """Rendering Provider"""
        rendering_provider = [
            e for e in self.entities if e.entity == "rendering provider"
        ]
        assert len(rendering_provider) <= 1

        if len(rendering_provider) == 1:
            return rendering_provider[0]

    @property
    def claim_statement_period_start(self) -> Optional[DateSegment]:
        """Claim Statement Period Start"""
        claim_statement_period_start = [
            d for d in self.dates if d.qualifier == "claim statement period start"
        ]
        assert len(claim_statement_period_start) <= 1

        if len(claim_statement_period_start) == 1:
            return claim_statement_period_start[0]

    @property
    def claim_statement_period_end(self) -> Optional[DateSegment]:
        """Claim Statement Period End"""
        claim_statement_period_end = [
            d for d in self.dates if d.qualifier == "claim statement period end"
        ]
        assert len(claim_statement_period_end) <= 1

        if len(claim_statement_period_end) == 1:
            return claim_statement_period_end[0]

    @property
    def patient(self) -> EntitySegment:
        """Patient"""
        patient = [e for e in self.entities if e.entity == "patient"]
        assert len(patient) == 1

        return patient[0]

    @classmethod
    def build(
        cls, segment: str, segments: Iterator[str]
    ) -> Tuple["Claim", Optional[Iterator[str]], Optional[str]]:
        """Build Claim Loop"""
        claim = Claim()
        claim.claim = ClaimSegment(segment)

        segment = segments.__next__()

        while True:
            try:
                if segment is None:
                    segment = segments.__next__()

                identifier = find_identifier(segment)

                if identifier == ServiceLoop.initiating_identifier:
                    service, segments, segment = ServiceLoop.build(segment, segments)
                    claim.services.append(service)

                elif identifier == EntitySegment.identification:
                    entity = EntitySegment(segment)
                    claim.entities.append(entity)
                    segment = None

                elif identifier == ReferenceSegment.identification:
                    reference = ReferenceSegment(segment)
                    claim.references.append(reference)
                    segment = None

                elif identifier == DateSegment.identification:
                    date = DateSegment(segment)
                    claim.dates.append(date)
                    segment = None

                elif identifier == AmountSegment.identification:
                    claim.amount = AmountSegment(segment)
                    segment = None

                elif identifier in cls.terminating_identifiers:
                    return claim, segments, segment

                else:
                    segment = None
                    message = f"Identifier: {identifier} not handled in claim loop."
                    warn(message)

            except StopIteration:
                return claim, None, None
