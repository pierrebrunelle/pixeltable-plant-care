"""Plant Care API built with Pixeltable.

    pxt schema update app.py plants
    pxt service run app.py plants
"""
from pixeltable.serving import FastAPIRouter

from models import Plants, TableModel  # noqa: F401  (TableModel lets `pxt schema` find the models)
from queries import thirsty

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
