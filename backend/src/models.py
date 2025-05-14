from pydantic import BaseModel, Field
from typing import Optional, List


class RegionData(BaseModel):
    region_code: str
    rank: int = Field(ge=1, le=5)  # popularity ranking 1 of 5
    categoryID: int = Field(ge=0, le=20)
    keyword: str
    link1: Optional[str] = None
    link2: Optional[str] = None
    link3: Optional[str] = None


class SummarizedData(BaseModel):
    region_code: str
    categoryID: int = Field(ge=0, le=20)
    summ: List[str]

CATEGORY_DICT = {
    1: "Autos and Vehicles",
    2: "Beauty and Fashion",
    3: "Business and Finance",
    4: "Entertainment",
    5: "Food and Drink",
    6: "Games",
    7: "Health",
    8: "Hobbies and Leisure",
    9: "Jobs and Education",
    10: "Law and Government",
    11: "Other",
    13: "Pets and Animals",
    14: "Politics",
    15: "Science",
    16: "Shopping",
    17: "Sports",
    18: "Technology",
    19: "Travel and Transportation",
    20: "Climate"
}
# key: map -->  mapRegion: geoCode
