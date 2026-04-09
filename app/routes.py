from fastapi import APIRouter
from app.models import RouteRequest, RouteResponse, Carrier

router = APIRouter()

# Hardcoded carrier data as specified in the test
ROUTE_DATA = {
    ("new york", "washington"): [
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
    # Normalize — remove punctuation, lowercase
    from_normalized = request.from_city.lower().replace(".", "").strip()
    to_normalized = request.to_city.lower().replace(".", "").strip()

    carriers = DEFAULT_CARRIERS
    for (from_key, to_key), value in ROUTE_DATA.items():
        if from_key in from_normalized and to_key in to_normalized:
            carriers = value
            break

    return RouteResponse(
        from_city=request.from_city,
        to_city=request.to_city,
        carriers=carriers,
    )