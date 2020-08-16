from typing import Optional
from datetime import date

from fastapi import FastAPI, Query
from pydantic import BaseModel
from functools import lru_cache

from . import config

from .utils import get_events


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


app = FastAPI(
    title="NFL Games",
    description="This API can be used to retrive recent NFL games and the current standings of the involved teams",
    version="0.1.0",
    docs_url="/",
    redoc_url=None
)


@lru_cache()
def get_settings():
    return config.Settings()


today = date.today()
default_start_date = today.strftime("%Y-%m-%d")
# Date regex to match YYYY-MM-DD format
# For insperation & explanation https://www.regextester.com/96683
DATE_REGEX = "([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))"


@app.get("/games/", tags=["games"])
def read_item(
    start: str = Query(default_start_date, regex=DATE_REGEX),
    end: Optional[str] = Query(None, regex=DATE_REGEX)
):
    if not end:
        end = start

    return get_events(start, end, get_settings().nfl_api_key)
