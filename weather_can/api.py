"""Web-related functionality for pulling weather data."""

import requests

API_URL = "https://dd.weather.gc.ca/citypage_weather/xml/{province_code}/{site_code}_{language}.xml"  # noqa


LANGUAGE_CODE_TO_URL_CODE = {
    'en': 'e',
    'fr': 'f',
}


def get_forecast_xml(
    site_code: str,
    province_code: str,
    language: str = "en"
) -> str:
    """
    Send a GET request to the weather API to get forecast data.

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

    Raises
    ------
    requests.HTTPError
        If the weather server returns a 4xx or 5xx response.
    """
    url = API_URL.format(
        province_code=province_code,
        site_code=site_code,
        language=LANGUAGE_CODE_TO_URL_CODE[language]
    )
    response = requests.get(url)
    response.raise_for_status()
    return response.text
