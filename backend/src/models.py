from pydantic import BaseModel, Field
from typing import Optional, List


class RegionData(BaseModel):
    region_code: str
    rank: int = Field(ge=1, le=5)  # popularity ranking 1 of 5
    keyword: str
    link1: Optional[str] = None
    link2: Optional[str] = None
    link3: Optional[str] = None


class SummarizedData(BaseModel):
    region_code: str
    summ: List[str]

# key: map -->  mapRegion: geoCode
