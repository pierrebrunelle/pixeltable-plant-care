"""Queries over the plants table."""
import pixeltable as pxt

from models import Plants


@pxt.query
def thirsty():
    """Plants whose computed advice is 'water today'."""
    return Plants.where(Plants.water_label == 'water today').select(
        Plants.id, Plants.notes_blurb, Plants.days_since_water
    ).order_by(Plants.days_since_water, asc=False)
