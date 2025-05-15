from pydantic import BaseModel, Field
from typing import Optional, List


class RegionData(BaseModel):
    region_code: str
    rank: int = Field(ge=1, le=5)  # popularity ranking 1 of 5
    category_id: int = Field(ge=0, le=20)
    keyword: str
    link1: Optional[str] = None
    link2: Optional[str] = None
    link3: Optional[str] = None


class SummarizedData(BaseModel):
    region_code: str
    category_id: int = Field(ge=0, le=20)
    language: str
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

LANG_DICT = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "ja": "Japanese",
    "ko": "Korean",
    "zh": "Chinese",
    "ar": "Arabic",
    "ru": "Russian",
    "hi": "Hindi",
    "tr": "Turkish",
    "vi": "Vietnamese",
    "th": "Thai",
    "pl": "Polish",
    "nl": "Dutch",
    "sv": "Swedish",
    "da": "Danish",
    "fi": "Finnish",
    "no": "Norwegian",
    "cs": "Czech",
    "hu": "Hungarian",
    "ro": "Romanian",
    "sk": "Slovak",
    "bg": "Bulgarian",
    "el": "Greek",
    "he": "Hebrew",
    "id": "Indonesian",
    "ms": "Malay",
    "tl": "Tagalog",
    "sw": "Swahili",
    "uk": "Ukrainian",
    "bn": "Bengali",
    "pa": "Punjabi",
    "ta": "Tamil",
    "te": "Telugu",
    "ml": "Malayalam",
    "kn": "Kannada",
    "mr": "Marathi",
    "gu": "Gujarati",
    "or": "Odia",
    "as": "Assamese",
    "ne": "Nepali",
    "si": "Sinhalese",
    "km": "Khmer",
    "la": "Latvian",
    "lt": "Lithuanian",
    "et": "Estonian",
    "lv": "Latvian",
    "is": "Icelandic",
    "cy": "Welsh",
    "ga": "Irish",
    "eu": "Basque",
    "ca": "Catalan",
    "gl": "Galician",
    "sq": "Albanian",
    "mk": "Macedonian",
    "sr": "Serbian",
    "bs": "Bosnian",
    "hr": "Croatian",
    "sl": "Slovenian",
    "mt": "Maltese",
    "hy": "Armenian",
    "az": "Azerbaijani",
    "tk": "Turkmen",
    "uz": "Uzbek",
    "kk": "Kazakh",
    "ky": "Kyrgyz",
    "tg": "Tajik",
    "mn": "Mongolian",
    "ps": "Pashto",
    "fa": "Persian",
    "dv": "Dhivehi",
    "sd": "Sindhi",
    "ku": "Kurdish",
    "yi": "Yiddish",
    "xh": "Xhosa",
    "zu": "Zulu",
    "am": "Amharic",
    "so": "Somali",
    "sn": "Shona",
    "st": "Sesotho",
    "jw": "Javanese",
    "su": "Sundanese"
}
# key: map -->  mapRegion: geoCode
