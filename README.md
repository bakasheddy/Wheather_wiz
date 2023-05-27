### About Data Source
The Historical Weather API is based on reanalysis datasets and uses a combination of weather station, aircraft, buoy, radar, and satellite observations to create a comprehensive record of past weather conditions. These datasets are able to fill in gaps by using mathematical models to estimate the values of various weather variables. As a result, reanalysis datasets are able to provide detailed historical weather information for locations that may not have had weather stations nearby, such as rural areas or the open ocean.

## Hourly Weather Data Parameter Definition

Parameter | Description
---|---------
`time` | time of each observation in year, month, day, hour, min, and sec
`city` | the city of observation
`temperature_2m` | Air temperature at 2 meters above ground
`relativehumidity_2m` | Relative humidity at 2 meters above ground
`apparent_temperature` | Apparent temperature is the perceived feels-like temperature combining wind chill factor, relative humidity and solar radiation
`precipitation` | Total precipitation (rain, showers, snow) sum of the preceding hour. Data is stored with a 0.1 mm precision. If precipitation data is summed up to monthly sums, there might be small inconsistencies with the total precipitation amount.
`surface_pressure` | Atmospheric air pressure reduced to mean sea level (msl) or pressure at surface. Typically pressure on mean sea level is used in meteorology. Surface pressure gets lower with increasing elevation.
`rain` | Only liquid precipitation of the preceding hour including local showers and rain from large scale systems.
`cloudcover` | Total cloud cover as an area fraction
`windspeed_10m` | Wind speed at 10 meters above ground. Wind speed on 10 meters is the standard level.
`winddirection_10m` | Wind direction at 10 meters above ground

#### notes: 
this data is a Weather history for Abuja, minna, keffi, and lagos Nigeria


Source: [open-meteo.com](https://open-meteo.com/en/docs/historical-weather-api#latitude=9.93&longitude=8.89&start_date=2000-01-01&end_date=2023-05-24&daily=temperature_2m_mean&timezone=Europe%2FLondon)
