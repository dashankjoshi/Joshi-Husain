# Weather Conditions and Flight Delays at Chicago O'Hare

## Contributors

- Dashank Joshi, NetID: [add NetID]
- Farwah Husain, NetID: [add NetID]

### Contribution Statement

Dashank Joshi contributed to dataset acquisition, repository organization, data profiling, analysis outputs, visualization review, and final documentation. Farwah Husain contributed to data cleaning, preprocessing, data integration, workflow documentation, and final report revision. Both team members reviewed the final repository and report for reproducibility and clarity.

## Summary

This project investigates how weather conditions are related to flight delays at Chicago O'Hare International Airport (ORD). Flight delays are a common issue in air travel and can be influenced by many factors, including airline operations, airport congestion, aircraft availability, and weather. For this project, we focused specifically on weather-related factors because they are measurable through public meteorological data and can be integrated with flight performance records. Our main goal was to move from two separate raw datasets to a cleaned, integrated dataset that could be used to analyze whether weather conditions were associated with longer or more frequent delays.

Our original project plan considered analyzing several major airports. However, as we began working with the actual datasets, we narrowed the final scope to Chicago O'Hare because the NOAA weather dataset we downloaded corresponded to the ORD weather station. This allowed us to create a cleaner and more reliable linkage between the airport flight records and the daily weather observations. Rather than forcing weaker matches across multiple airports, we focused on one airport where the integration was more accurate and reproducible.

The main research question guiding our project was: how do weather conditions such as precipitation, visibility, temperature, and wind relate to departure delays? We were also interested in whether certain weather conditions appeared to be more strongly associated with flight disruptions than others. To answer these questions, we integrated two public government datasets: flight performance data from the Bureau of Transportation Statistics (BTS) and hourly weather observations from the National Oceanic and Atmospheric Administration (NOAA).

Our workflow included data acquisition, profiling, cleaning, integration, analysis, and visualization. The BTS dataset provided flight-level information such as flight date, origin airport, destination airport, departure delay, arrival delay, and reported weather delay. The NOAA dataset provided weather observations such as temperature, visibility, wind speed, and precipitation. Because the weather data was hourly and the flight data was analyzed at the daily level, we aggregated the weather observations into daily summaries before merging them with the flight records.

After cleaning and integration, the final integrated dataset contained 23,290 flight records for ORD matched with daily weather observations. The results suggest that precipitation and low visibility were associated with noticeably higher departure delays. Flights on precipitation days had an average departure delay of 26.17 minutes, compared to 7.54 minutes on non-precipitation days. Low visibility days had an even stronger relationship with delays, with an average departure delay of 95.91 minutes compared to 16.81 minutes on days without low visibility.

This project also emphasizes data curation and reproducibility. In addition to analyzing delay patterns, we created scripts for profiling, cleaning, integrating, and analyzing the datasets. We also documented the file organization, data sources, data dictionary, and reproduction steps so that another user can rerun the workflow. Overall, this project demonstrates how integrating transportation data with weather data can reveal meaningful patterns in flight disruptions, while also showing the importance of careful data cleaning and transparent documentation.

## Data Profile

### Dataset 1: BTS Airline On-Time Performance Data

The first dataset is the BTS Airline On-Time Performance dataset from the U.S. Bureau of Transportation Statistics. This dataset contains flight-level records for U.S. commercial flights. Each row represents an individual flight and includes information about the flight date, airline carrier, origin airport, destination airport, delay values, and flight distance. This dataset is the main source for measuring flight delay outcomes in our project.

The raw flight dataset is named `flights_2019.csv`. Because the file is larger than 50MB, it is stored externally through Box instead of directly in GitHub. Download instructions are provided in:

`data/raw/README.md`

After downloading, the file should be saved as:

`data/raw/flights_2019.csv`

Original source: https://transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ&QO_fu146_anzr=b0-gvzr

Important variables used from this dataset include:

- `FL_DATE`: date of the flight
- `ORIGIN`: origin airport code
- `DEST`: destination airport code
- `DEP_DELAY`: departure delay in minutes
- `ARR_DELAY`: arrival delay in minutes
- `WEATHER_DELAY`: delay minutes attributed to weather
- `DISTANCE`: flight distance in miles

This dataset relates directly to our research question because it provides the delay outcomes we are trying to explain. The main variable of interest is departure delay, since our analysis focuses on whether weather conditions are associated with longer departure delays or higher delay rates. The dataset also includes reported weather delay, which provides an additional field for checking whether BTS attributed part of a delay to weather.

### Dataset 2: NOAA Global Hourly Weather Data

The second dataset is the NOAA Global Hourly Weather dataset from the National Oceanic and Atmospheric Administration. This dataset contains hourly weather observations from weather stations. Each row represents a weather observation at a specific station and time. The data includes encoded weather fields that describe temperature, visibility, wind, precipitation, and other atmospheric conditions.

The raw weather dataset is stored directly in the repository as:

`data/raw/weather_2019.csv`

Original source: https://www.ncei.noaa.gov/access/search/data-search/global-hourly

Important variables used from this dataset include:

- `STATION`: NOAA weather station identifier
- `NAME`: station name
- `DATE`: date and time of the weather observation
- `TMP`: encoded temperature field
- `VIS`: encoded visibility field
- `WND`: encoded wind field
- `AA1`: encoded precipitation field

This dataset provides the weather variables needed to evaluate possible relationships between weather conditions and flight delays. The weather station used in this project corresponds to Chicago O'Hare, which allowed us to integrate the weather data with ORD flight records.

### Processed and Integrated Data

The cleaned flight dataset is stored as:

`data/processed/flights_cleaned.csv`

The cleaned weather dataset is stored as:

`data/processed/weather_cleaned.csv`

The final integrated dataset is stored as:

`data/processed/integrated_flights_weather.csv`

The integrated dataset combines ORD flight records with daily weather summaries. Each integrated row represents a flight from ORD with matching daily weather conditions for that date. Key integrated variables include departure delay, arrival delay, reported weather delay, daily average temperature, daily average visibility, daily average wind speed, total daily precipitation, and indicator variables for precipitation days, low visibility days, and high wind days.

Additional documentation is included in:

`docs/data_dictionary.md`

### Ethical and Legal Considerations

Both datasets come from U.S. government sources and are publicly available for research and educational use. The data does not contain personally identifiable information about passengers. Since the datasets describe flights and weather observations rather than individuals, the main ethical considerations are proper citation, accurate interpretation, and transparent documentation of cleaning and analysis decisions.

The BTS and NOAA datasets are used only for academic analysis. We do not claim ownership over the original government datasets. Our own code and documentation are included in this repository for reproducibility and are covered by the repository license.

## Data Quality

We assessed data quality using `scripts/01_profile_data.py`, which produced summary tables in `results/tables/`. These outputs include row counts, column names, duplicate row counts, and missing value summaries. This step helped us better understand the structure of each dataset before cleaning or integration. It also allowed us to identify which fields were reliable enough to use in the analysis and which fields needed additional processing.

The raw flight dataset was large and contained more columns than were needed for this project. Since our research questions focused on the relationship between weather and flight delays, we selected only the variables relevant to flight timing, location, and delay outcomes. Important fields included flight date, origin airport, destination airport, departure delay, arrival delay, distance, and delay-cause variables. One issue we identified was that some delay-related fields contained missing values. This was especially true for cause-specific delay columns such as weather delay, carrier delay, NAS delay, and late aircraft delay. In the BTS data, this is expected because these fields are usually only populated when a delay is long enough to require a reported cause. As a result, missing values in these cause-specific columns were treated differently from missing values in key fields such as flight date or departure delay.

The raw weather dataset also required quality review because NOAA hourly weather fields are not provided as simple numeric columns. Instead, variables such as temperature, visibility, wind, and precipitation were encoded in compact string formats. For example, wind speed and direction were stored together in the `WND` field, while precipitation was stored in the `AA1` field. These fields had to be parsed before they could be used in analysis. We also had to account for NOAA missing-value codes, such as `999999` for visibility or `999.9` for temperature. These values do not represent real observations, so they were converted to missing values during cleaning.

Another data quality issue was the difference in time granularity between the two datasets. The flight dataset was analyzed at the flight/date level, while the weather dataset contained hourly observations. To make the datasets compatible, we aggregated hourly weather observations into daily summaries. This allowed us to match each flight date with the corresponding daily weather conditions. While this approach supports a reproducible integration, it also reduces some time-specific detail. For example, a short storm during one part of the day may not affect all flights equally, but daily aggregation treats the weather for that date as a general condition.

A final data quality limitation is that the integrated dataset only matched flights from ORD because the NOAA weather data selected for this project corresponded to Chicago O'Hare. As a result, the findings should not be generalized to all U.S. airports. Instead, they should be interpreted as a focused analysis of ORD during the selected 2019 period. This limitation was documented so the scope of the final results is clear and transparent.

## Data Cleaning

Data cleaning was performed using two main scripts: `scripts/02_clean_flights.py` and `scripts/03_clean_weather.py`.

For the flight dataset, we selected only the columns needed for analysis. These included flight date, carrier, flight number, origin, destination, departure delay, arrival delay, distance, and delay-cause variables. This reduced the dataset to the fields most directly related to our research questions and helped make the workflow easier to reproduce. The script converted flight dates into a standard datetime format and removed rows missing key fields such as flight date, origin airport, destination airport, departure delay, and arrival delay.

The flight cleaning script also converted delay columns to numeric values. Cause-specific delay columns such as weather delay, carrier delay, NAS delay, and late aircraft delay were filled with zero when missing, because missing values usually indicated that no reportable delay was assigned to that category. The dataset was filtered to selected major airports during the cleaning phase, and the final integration used ORD because that was the airport linked to the NOAA weather station. Extreme delay outliers above 600 minutes were removed so rare disruptions would not dominate the analysis.

For the weather dataset, the cleaning script parsed NOAA encoded fields into usable variables. Temperature was converted from the `TMP` field into Celsius. Visibility was extracted from the `VIS` field in meters. Wind speed was extracted from the `WND` field in meters per second. Precipitation was parsed from the `AA1` field in millimeters. These transformations were necessary because the raw NOAA file stored weather values in compact encoded strings rather than clean numeric columns.

The weather script also handled NOAA missing-value codes by converting them to missing values. After parsing, hourly observations were grouped by station and date to create daily summaries. These summaries included average temperature, average visibility, average wind speed, and total precipitation. The script also created indicator variables for precipitation days, low visibility days, and high wind days. These indicator variables made the final analysis more interpretable because they allowed us to compare average delays under different types of weather conditions.

The cleaned outputs are stored in:

- `data/processed/flights_cleaned.csv`
- `data/processed/weather_cleaned.csv`

