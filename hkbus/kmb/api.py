"""https://data.gov.hk/tc-data/dataset/hk-td-tis_21-etakmb"""

from .models import *

import requests

BASE_URL = "https://data.etabus.gov.hk"


def get_route_list() -> RouteListResponse:
    response = requests.get(f"{BASE_URL}/v1/transport/kmb/route")
    response.raise_for_status()
    return RouteListResponse.model_validate_json(response.text)


def get_stop_list() -> StopListResponse:
    response = requests.get(f"{BASE_URL}/v1/transport/kmb/stop")
    response.raise_for_status()
    return StopListResponse.model_validate_json(response.text)


def get_stop_eta(stop_id: str) -> StopETAResponse:
    response = requests.get(f"{BASE_URL}/v1/transport/kmb/stop-eta/{stop_id}")
    response.raise_for_status()
    return StopETAResponse.model_validate_json(response.text)
