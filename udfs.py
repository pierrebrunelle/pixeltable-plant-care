"""Pixeltable UDFs for plant care (recorded by module path, e.g. `udfs.water_advice`)."""
import pixeltable as pxt


@pxt.udf
def water_advice(moisture: str | None, days_since_water: int | None) -> str:
    m = (moisture or '').strip().lower()
    d = days_since_water or 0
    if m == 'dry' or (m == 'slightly-dry' and d >= 4):
        return 'water today'
    if m == 'slightly-dry':
        return 'check tomorrow'
    if m in ('moist', 'wet'):
        return 'skip'
    return 'check soil'


@pxt.udf
def care_blurb(species: str, location: str) -> str:
    return f'{species} in the {location}'
