# Weather Can API

Retrieve Canadian weather forecasts.

This wraps for the Environment and Climate Change Canada (ECCC) Data Server's `citypage_weather` API. See [the ECCC MSC data site](https://eccc-msc.github.io/open-data/msc-data/citypage-weather/readme_citypageweather-datamart_en/) for documentation.

Geocoding (searching by city, town, county, street, etc.) is available via the `geocoder` library, using the [OpenStreetMaps (OSM) Nominatim API](https://geocoder.readthedocs.io/providers/OpenStreetMap.html).


## Setup

## GeoJSON Format

This API makes use of the ECCC list of location names and sites code [found here in GeoJSON format](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/citypage-weather/site_list_en.geojson).

This GeoJSON is comprised of a `FeatureCollection` with a list of `Point` features. Each `Point` has the following properties associated:

| Property | Description
| --- | ---
| Codes          | The unique site code for this city. This is of the form `s0000583`
| English Names  | The english name for the city/site.
| Province Codes | The 2-digit province code for the site.
| Latitude       | The latitude coordinate for this site.
| Longitude      | The longitude coordinate for this site.

## Return Format

## Language Support

Weather data is provided in English and French.

## License

This repository is licensed under [the MIT license](https://opensource.org/licenses/MIT).

Use of returned weather data is governed by the [Environment and Climate Change Canada Data Servers End-use License](https://eccc-msc.github.io/open-data/licence/readme_en/).

Usage of geocoding functionality is governed by the [OSM Nominatim usage policy](https://operations.osmfoundation.org/policies/nominatim/).
