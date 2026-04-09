from pydantic import BaseModel
from typing import List


# Request model — what the frontend sends
class RouteRequest(BaseModel):
    from_city: str
    to_city: str


# Single carrier — what we return per carrier
class Carrier(BaseModel):
    name: str
    trucks_per_day: int


# Response model — the full API response
class RouteResponse(BaseModel):
    from_city: str
    to_city: str
    carriers: List[Carrier]