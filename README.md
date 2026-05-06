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

## Data Integration

Data integration was performed using `scripts/04_integrate_data.py`. The flight dataset used airport codes, while the weather dataset used NOAA station identifiers. To connect the datasets, we created a station-to-airport mapping for ORD. This was necessary because the two datasets did not share a single direct identifier.

The integration used two main keys:

- origin airport
- date

The weather data was first aggregated to the daily level. Then, ORD flight records were matched with ORD weather observations by date. The final integrated dataset is stored as:

`data/processed/integrated_flights_weather.csv`

The integration summary showed:

- Cleaned flight rows: 104,619
- Cleaned weather rows: 365
- Flight rows eligible for merge: 23,290
- Integrated rows: 23,290
- Airport integrated: ORD

This means that all eligible ORD flight rows were successfully matched with daily weather observations. The integrated dataset allowed us to compare departure delays across different weather conditions.

## Findings

The final analysis was performed using `scripts/05_analyze_visualize.py`. The results are stored in `results/tables/` and `results/figures/`. The main outputs include summary tables comparing delays on precipitation days, low visibility days, and high wind days, as well as visualizations showing average delay patterns.

One of the clearest findings was that precipitation days were associated with higher departure delays than non-precipitation days. On days without precipitation, the average departure delay was 7.54 minutes and the delayed flight rate was 15.74%. On precipitation days, the average departure delay increased to 26.17 minutes and the delayed flight rate increased to 34.18%. This means that flights on precipitation days were delayed more than twice as often as flights on days without precipitation. The average reported weather delay was also higher on precipitation days, increasing from 1.29 minutes to 4.60 minutes. This supports the idea that precipitation has a measurable relationship with flight disruptions.

Low visibility had an even stronger relationship with delays. On days without low visibility, the average departure delay was 16.81 minutes and the delayed flight rate was 25.86%. On low visibility days, the average departure delay increased to 95.91 minutes and the delayed flight rate rose to 71.85%. The median delay also increased substantially, from -1.0 minutes on normal visibility days to 49.0 minutes on low visibility days. This suggests that low visibility was not just associated with a few extreme delays, but with a broader shift toward delayed departures. The average reported weather delay was also much higher on low visibility days: 20.82 minutes compared to 2.82 minutes on days without low visibility.

Wind was also considered, but our high-wind indicator did not identify any high-wind days based on the threshold used in the script. Because of this, we cannot draw strong conclusions about high-wind days from this dataset. Wind speed is still included in the integrated dataset, but a different threshold or a longer time period may be needed to study wind effects more meaningfully.

The monthly summary only included January in the integrated data, so seasonal comparisons were limited. For January, the average departure delay was 19.13 minutes, and 27.21% of flights were delayed by more than 15 minutes. Overall, the findings indicate that precipitation and especially low visibility were associated with greater departure delays at ORD during the selected period.

## Future Work

One major area for future work would be expanding the analysis to include more airports. Our original project plan considered multiple major airports, but the final analysis focuses on Chicago O'Hare. We made this adjustment because the NOAA weather dataset available for our workflow corresponded to the ORD weather station, which allowed us to create a clearer and more reliable linkage between airport flight records and daily weather observations. In the future, we could download additional NOAA weather files for airports such as ATL, JFK, LAX, and DFW. This would allow us to compare how different airports respond to similar weather conditions and determine whether ORD is more or less sensitive to weather disruptions than other major hubs.

Another improvement would be using hourly matching instead of daily aggregation. In this project, hourly weather observations were summarized into daily values so they could be merged more easily with flight records. While this approach worked, it may hide important details. For example, a storm that occurs in the morning may affect morning flights more than evening flights. Similarly, low visibility during only one part of the day may not explain delays for flights much later in the day. Future analysis could match each flight to the nearest weather observation based on scheduled departure time. This would allow for a more precise connection between weather conditions and individual flight outcomes.

We could also improve the analysis by using additional weather variables. This project focused on precipitation, visibility, temperature, and wind speed, but other conditions may also matter. Snow, cloud cover, pressure changes, runway visibility, and severe weather indicators could provide a more complete picture of how weather affects flight operations. Since Chicago has winter weather that can strongly affect airport operations, adding snow and ice-related variables would likely be useful.

Another direction for future work would be to use more advanced statistical methods. Our current analysis is mostly exploratory and compares average delays under different weather conditions. Future work could use regression models to estimate the relationship between weather variables and delay length while controlling for factors such as airline, destination, distance, and month. A classification model could also be used to predict whether a flight is likely to be delayed by more than 15 minutes.

Finally, future work could improve the reproducibility workflow by using Snakemake instead of a simple `run_all.py` script. The current workflow is reproducible because the scripts can be run in order, but Snakemake would make dependencies between files more explicit and avoid rerunning unnecessary steps. This would be especially helpful if the project were expanded to more airports or a longer time period.

## Challenges

One of the biggest challenges was working with large datasets. The raw BTS flight file was larger than 50MB, which made it difficult to store directly in GitHub. GitHub also has limits for uploading files through the browser, so we had to decide how to make the dataset accessible while still following the project requirements. To address this, we stored the flight file externally through Box and documented where users should download it and save it in the repository. This helped keep the repository organized while still supporting reproducibility.

Another challenge was the difference in identifiers between the datasets. The flight dataset used airport codes such as ORD, while the weather dataset used NOAA station identifiers. These identifiers do not automatically match, so we had to create a station-to-airport mapping. For the final project, we mapped the NOAA station in our weather dataset to Chicago O'Hare. This step was important because the quality of the integration depended on accurately linking the flight records to the correct weather station.

The NOAA weather fields were also challenging because they were encoded rather than already cleaned numeric variables. Temperature, visibility, wind speed, and precipitation each had to be parsed from formatted strings. In addition, NOAA uses special missing-value codes, which needed to be identified and handled during cleaning. This made the weather cleaning process more complicated than simply loading a CSV and selecting columns. However, this also made the project more realistic because it required actual data wrangling rather than using an analysis-ready dataset.

A final challenge was the change in scope from the original project plan. Initially, we intended to analyze and compare multiple major airports. However, after working with the actual NOAA data, we realized that the downloaded weather dataset corresponded to Chicago O'Hare. Instead of expanding the project with weaker or incomplete weather matches, we narrowed the analysis to ORD. This made the final integration more accurate, transparent, and reproducible. Although this reduced the geographic scope of the project, it improved the reliability of the final dataset and made the analysis easier to explain clearly.

## Reproducing

To reproduce this project:

1. Clone or download this GitHub repository.

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Download the raw flight dataset from the Box link listed in `data/raw/README.md`.

4. Save the file exactly as:

```text
data/raw/flights_2019.csv
```

5. Confirm that the weather dataset exists at:

```text
data/raw/weather_2019.csv
```

6. Run the full workflow:

```bash
python run_all.py
```

This will run the scripts in order:

```text
scripts/01_profile_data.py
scripts/02_clean_flights.py
scripts/03_clean_weather.py
scripts/04_integrate_data.py
scripts/05_analyze_visualize.py
```

The workflow generates processed datasets in `data/processed/`, summary tables in `results/tables/`, and visualizations in `results/figures/`.

## References

Bureau of Transportation Statistics. Airline On-Time Performance Data. U.S. Department of Transportation. https://transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ&QO_fu146_anzr=b0-gvzr

National Oceanic and Atmospheric Administration. Global Hourly Weather Data. National Centers for Environmental Information. https://www.ncei.noaa.gov/access/search/data-search/global-hourly

Python Software Foundation. Python Programming Language. https://www.python.org/

The pandas development team. pandas: Python Data Analysis Library. https://pandas.pydata.org/

Hunter, J. D. Matplotlib: A 2D Graphics Environment. Computing in Science & Engineering. https://matplotlib.org/

Harris, C. R., Millman, K. J., van der Walt, S. J., et al. Array programming with NumPy. Nature. https://numpy.org/


