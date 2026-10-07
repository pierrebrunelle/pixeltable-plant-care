"""Plant Care API built with Pixeltable.

    pxt schema update app.py plants
    pxt service run app.py plants
"""
import pixeltable as pxt
import pixeltable.functions as pxtf
from pixeltable.serving import FastAPIRouter

from udfs import care_blurb, water_advice

# ---- tables ----
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


# ---- queries ----
@pxt.query
def thirsty():
    """Plants whose computed advice is 'water today'."""
    return Plants.where(Plants.water_label == 'water today').select(
        Plants.id, Plants.notes_blurb, Plants.days_since_water
    ).order_by(Plants.days_since_water, asc=False)


# ---- routes ----
plants_api = FastAPIRouter(name='plants_api')
plants_api.add_insert_route(
    Plants, path='/plants',
    inputs=[Plants.species, Plants.location, Plants.moisture, Plants.days_since_water, Plants.notes],
    outputs=[Plants.id, Plants.water_label, Plants.species_upper, Plants.notes_blurb],
)
plants_api.add_update_route(Plants, path='/plants/update', inputs=[Plants.moisture, Plants.days_since_water],
                            outputs=[Plants.id, Plants.water_label])
plants_api.add_compute_route(Plants, path='/water-label', inputs=[Plants.moisture, Plants.days_since_water],
                             outputs=[Plants.water_label])
plants_api.add_query_route(path='/plants/thirsty', query=thirsty, method='get')
