# Data Dictionary

## Raw Flight Dataset: `flights_2019.csv`

Source: Bureau of Transportation Statistics Airline On-Time Performance Data

| Column | Description |
|---|---|
| FL_DATE | Date of the flight |
| ORIGIN | Origin airport code |
| DEST | Destination airport code |
| DEP_DELAY | Departure delay in minutes |
| ARR_DELAY | Arrival delay in minutes |
| WEATHER_DELAY | Delay minutes attributed to weather |
| DISTANCE | Flight distance in miles |

## Raw Weather Dataset: `weather_2019.csv`

Source: NOAA Global Hourly Weather Data

| Column | Description |
|---|---|
| STATION | NOAA weather station identifier |
| NAME | Weather station name |
| DATE | Date and time of weather observation |
| TMP | Encoded temperature field |
| VIS | Encoded visibility field |
| WND | Encoded wind field |
| AA1 | Encoded precipitation field |

## Processed Integrated Dataset: `integrated_flights_weather.csv`

| Column | Description |
|---|---|
| origin | Origin airport code |
| destination | Destination airport code |
| flight_date | Date of flight |
| departure_delay | Departure delay in minutes |
| arrival_delay | Arrival delay in minutes |
| reported_weather_delay | Delay minutes attributed to weather |
| temperature_c | Daily average temperature in Celsius |
| visibility_m | Daily average visibility in meters |
| wind_speed_mps | Daily average wind speed in meters per second |
| precipitation_mm | Total daily precipitation in millimeters |
| low_visibility_day | Whether average daily visibility was below 5000 meters |
| precipitation_day | Whether precipitation was recorded that day |
| high_wind_day | Whether average wind speed was above 10 m/s |