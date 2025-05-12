from pydantic import BaseModel, Field
from typing import Optional, List

GEO_USA = ('US-AL', 'US-AK', 'US-AZ', 'US-AR', 'US-CA', 'US-CO', 'US-CT', 'US-DE', 'US-FL', 'US-GA',
           'US-HI', 'US-ID', 'US-IL', 'US-IN', 'US-IA', 'US-KS', 'US-KY', 'US-LA', 'US-ME', 'US-MD',
           'US-MA', 'US-MI', 'US-MN', 'US-MS', 'US-MO', 'US-MT', 'US-NE', 'US-NV', 'US-NH', 'US-NJ',
           'US-NM', 'US-NY', 'US-NC', 'US-ND', 'US-OH', 'US-OK', 'US-OR', 'US-PA', 'US-RI', 'US-SC',
           'US-SD', 'US-TN', 'US-TX', 'US-UT', 'US-VT', 'US-VA', 'US-WA', 'US-WV', 'US-WI', 'US-WY'
           'US')

class RegionData(BaseModel):
    region_code: str
    rank: int = Field(ge=1, le=5) # popularity ranking 1 of 5
    keyword: str
    link1: Optional[str] = None
    link2: Optional[str] = None
    link3: Optional[str] = None

class SummarizedData(BaseModel):
    region_code: str
    summ: List[str]

# key: map -->  mapRegion: geoCode