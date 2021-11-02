"""Functions for getting weather forecasts."""

from .api import get_forecast_xml
from .weather_sites import (
    get_weather_site_by_coordinates, get_weather_site_by_place_name
)


def get_forecast_by_site_code(
    site_code: str,
    province_code: str,
    language: str = "en"
) -> str:
    """
    Get the weather forecast for the given weather site.

    Parameters
    ----------
    site_code : str
        The site code to get the forecast for.
    province_code : str
        The province code corresponding to this site.
    language: str
        The language to retrieve the forecast in. Allowed values: "en", "fr".

    Returns
    -------
    str
        The XML weather forecast.
    """
    return get_forecast_xml(
        site_code=site_code,
        province_code=province_code,
        language=language
    )


def get_forecast_by_coordinates(
    x: float,
    y: float,
    language: str = "en"
) -> str:
    """
    Get the weather forecast for the site closest to the coordinates (x, y).

    Uses the scipy kd-tree nearest-neighbor algorithm to find the closest
    site.

    Parameters
    ----------
    x : float
        Longitude of the query point.
    y : float
        Latitude of the query point.
    language: str
        The language to retrieve the forecast in. Allowed values: "en", "fr".

    Returns
    -------
    str
        The XML weather forecast.
    """
    nearest_site = get_weather_site_by_coordinates(x, y)
    site_code = nearest_site['properties']['Codes']
    province_code = nearest_site['properties']['Province Codes']
    forecast = get_forecast_by_site_code(
        site_code=site_code,
        province_code=province_code
    )
    return forecast


def get_forecast_by_place_name(name: str, language: str = "en") -> str:
    """
    Find the coordinates of the place matching the given name,
    then get the weather forecast for the nearest site.

    Uses the osm geocoding API.

    Parameters
    ----------
    place_name : str
        The place name to pass to the geocoding API.
    language: str
        The language to retrieve the forecast in. Allowed values: "en", "fr".

    Returns
    -------
    str
        The XML weather forecast.
    """
    nearest_site = get_weather_site_by_place_name(name=name)
    site_code = nearest_site['properties']['Codes']
    province_code = nearest_site['properties']['Province Codes']
    forecast = get_forecast_by_site_code(
        site_code=site_code,
        province_code=province_code
    )
    return forecast
