"""The plants table."""
import pixeltable as pxt
import pixeltable.functions as pxtf

from udfs import care_blurb, water_advice

TableModel = pxt.model_base()


class Plants(TableModel, name='plants'):
    id = pxt.Column(value=pxtf.uuid.uuid7(), primary_key=True)
    species: pxt.String
    location: pxt.String
    moisture: pxt.String | None
    days_since_water: pxt.Int | None
    notes: pxt.String | None

    water_label = water_advice(moisture, days_since_water)
    species_upper = pxtf.string.upper(species)
    notes_blurb = care_blurb(species, location)
