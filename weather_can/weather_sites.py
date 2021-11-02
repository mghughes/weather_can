"""Spatial functions for finding weather sites."""

import geocoder
import fiona
import numpy as np
from scipy.spatial import KDTree

import os


def get_weather_site_collection() -> fiona.Collection:
    """
    Get all weather sites as a fiona collection.

    Returns
    -------
    fiona.Collection
        Fiona collection with all weather sites.
    """
    site_list_filepath = os.path.join(
        os.path.dirname(__file__),
        'data',
        'site_list_en.geojson'
    )
    return fiona.open(site_list_filepath)


def get_weather_site_by_coordinates(x: float, y: float) -> dict:
    """
    Get the weather forecast site closest to the given (x, y) point.

    Uses a nearest-neighbor algorithm on a k-d tree, implemented by
    scipy.KDTree().query().

    Parameters
    ----------
    x : float
        Longitude of the query point.
    y : float
        Latitude of the query point.

    Returns
    -------
    dict
        geojson feature describing the nearest site.
    """
    # Build up array of [x, y] coordinates.
    features = list(get_weather_site_collection())
    points = np.asarray([feat['geometry']['coordinates'] for feat in features])

    # Construct a k-d tree.
    tree = KDTree(points)
    querypoint = np.asarray([[x, y]])

    # Get single nearest-neighbour to our query point.
    result = tree.query(querypoint, 1)
    index = result[1][0]
    return features[index]


def get_weather_site_by_place_name(name: str) -> dict:
    """
    Find the coordinates of the place matching the given name, then get
    the cloest weather site to these coordinates.

    Parameters
    ----------
    place_name : str
        The place name to pass to the geocoding API.
    language: str
        The language to retrieve the forecast in. Allowed values: "en", "fr".

    Returns
    -------
    dict
        geojson feature describing the nearest site.
    """
    location = geocoder.osm(name)
    if not location.ok:
        raise ValueError(f"OSM could not find location for {name}")

    coordinates = location.geojson['features'][0]['geometry']['coordinates']
    nearest_site = get_weather_site_by_coordinates(
        x=coordinates[0], y=coordinates[1]
    )
    return nearest_site
