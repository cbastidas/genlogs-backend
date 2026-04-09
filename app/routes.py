from fastapi import APIRouter
from app.models import RouteRequest, RouteResponse, Carrier

# APIRouter lets us keep routes organized in separate files
router = APIRouter()

# Hardcoded carrier data as specified in the test
ROUTE_DATA = {
    ("new york", "washington dc"): [
        Carrier(name="Knight-Swift Transport Services", trucks_per_day=10),
        Carrier(name="J.B. Hunt Transport Services Inc", trucks_per_day=7),
        Carrier(name="YRC Worldwide", trucks_per_day=5),
    ],
    ("san francisco", "los angeles"): [
        Carrier(name="XPO Logistics", trucks_per_day=9),
        Carrier(name="Schneider", trucks_per_day=6),
        Carrier(name="Landstar Systems", trucks_per_day=2),
    ],
}

# Default carriers for any other route
DEFAULT_CARRIERS = [
    Carrier(name="UPS Inc.", trucks_per_day=11),
    Carrier(name="FedEx Corp", trucks_per_day=9),
]


@router.post("/carriers", response_model=RouteResponse)
def get_carriers(request: RouteRequest):
    """
    Receives from_city and to_city, returns the list of carriers
    operating on that corridor with their trucks/day data.
    """
    # Normalize to lowercase for matching
    key = (request.from_city.lower().strip(), request.to_city.lower().strip())

    carriers = ROUTE_DATA.get(key, DEFAULT_CARRIERS)

    return RouteResponse(
        from_city=request.from_city,
        to_city=request.to_city,
        carriers=carriers,
    )