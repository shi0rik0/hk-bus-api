from pydantic import BaseModel

from typing import List, Optional


class Route(BaseModel):
    route: str
    bound: str
    service_type: str
    orig_en: str
    orig_tc: str
    orig_sc: str
    dest_en: str
    dest_tc: str
    dest_sc: str


class RouteListResponse(BaseModel):
    type: str
    version: str
    generated_timestamp: str
    data: List[Route]


class Stop(BaseModel):
    stop: str
    name_en: str
    name_tc: str
    name_sc: str
    lat: float
    long: float


class StopListResponse(BaseModel):
    type: str
    version: str
    generated_timestamp: str
    data: List[Stop]


class StopETA(BaseModel):
    route: str
    service_type: int
    dir: str
    seq: int
    dest_tc: str
    dest_en: str
    dest_sc: str
    eta_seq: int
    eta: Optional[str]
    rmk_tc: str
    rmk_en: str
    rmk_sc: str


class StopETAResponse(BaseModel):
    type: str
    version: str
    generated_timestamp: str
    data: List[StopETA]
