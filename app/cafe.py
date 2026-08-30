import datetime


from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated!")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Expiration date late!")
        if ("wearing_a_mask" not in visitor
                or visitor["wearing_a_mask"] is False):
            raise NotWearingMaskError("Need to wear a mask!")
        return f"Welcome to {self.name}"
