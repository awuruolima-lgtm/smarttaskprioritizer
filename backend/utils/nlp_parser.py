from typing import Optional
from datetime import datetime
from dateparser import parse as date_parse

def parse_human_date(text: Optional[str]) -> Optional[datetime]:
    if not text:
        return None
    dt = date_parse(text)  # Returns naïve datetime in local tz by default
    return dt
