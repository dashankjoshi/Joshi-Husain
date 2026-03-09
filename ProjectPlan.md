# Project Plan

## Overview

The goal of this project is to analyze how weather conditions affect flight delays at major airports in the United States. Flight delays are a common issue in the aviation industry and can cause disruptions for passengers, airlines, and airport operations. Weather conditions such as precipitation, wind speed, temperature, and visibility are known to significantly impact flight schedules. Understanding how these environmental factors influence flight delays can provide valuable insights into patterns of airline disruptions and operational challenges.

This project will integrate two primary datasets: a flight performance dataset from the U.S. Bureau of Transportation Statistics (BTS) and a historical weather dataset from the National Oceanic and Atmospheric Administration (NOAA). The flight dataset contains information about individual flights including departure delays, arrival delays, origin airports, destination airports, and flight dates. The weather dataset contains hourly observations including temperature, wind speed, precipitation, and visibility collected from weather stations.

The project will combine these datasets using shared attributes such as airport location and date. By aligning flight records with weather observations at the corresponding airport and time period, we can analyze how weather variables correlate with flight delays. The workflow for the project will involve data acquisition, data cleaning, data integration, exploratory analysis, and visualization.

The final outcome of the project will be an integrated dataset that enables analysis of the relationship between weather conditions and flight delays. Through this analysis, we aim to identify which weather conditions most strongly influence delays and whether these patterns vary across airports or time periods.


## Team

This project will be completed by two team members:

**Dashank Joshi**
- Responsible for dataset acquisition and documentation
- Responsible for repository organization and project documentation
- Assist with data analysis and visualization

**Farwah Husain**
- Responsible for data cleaning and preprocessing
- Responsible for data integration using Python/Pandas
- Assist with exploratory analysis and interpretation of results

Both of us will collaborate on writing the project report, preparing visualizations, and documenting the workflow to ensure reproducibility.


## Research or Business Questions

This project aims to investigate how weather conditions influence flight delays. The following research questions will guide our analysis:

1. How do weather conditions such as precipitation, wind speed, temperature, and visibility affect flight departure delays?
2. Are certain weather variables more strongly associated with flight delays than others?
3. Do specific airports experience more weather-related delays compared to others?
4. Are there seasonal patterns in flight delays related to weather conditions?

These questions can be addressed by integrating the flight dataset with historical weather observations and performing statistical and exploratory analysis.


## Datasets

### Dataset 1: Flight On-Time Performance Data

The first dataset used in this project is the **Airline On-Time Performance dataset** provided by the U.S. Bureau of Transportation Statistics (BTS). This dataset contains detailed records of commercial airline flights in the United States.

Important attributes in this dataset include:

- `FL_DATE` – Date of the flight
- `ORIGIN` – Origin airport code
- `DEST` – Destination airport code
- `DEP_DELAY` – Departure delay in minutes
- `ARR_DELAY` – Arrival delay in minutes
- `WEATHER_DELAY` – Delay attributed to weather
- `DISTANCE` – Distance of the flight

This dataset provides the operational data necessary to measure flight delays and identify disruptions in airline schedules.

---

### Dataset 2: NOAA Global Hourly Weather Data

The second dataset used in this project is the **Global Hourly Weather Dataset** from the National Oceanic and Atmospheric Administration (NOAA). This dataset contains hourly weather observations collected from weather stations worldwide.

Relevant attributes in this dataset include:

- `STATION` – Weather station identifier
- `DATE` – Timestamp of observation
- `TMP` – Air temperature
- `WND` – Wind speed and direction
- `VIS` – Visibility
- `AA1` – Hourly precipitation
- `RH1` – Relative humidity

These variables represent key atmospheric conditions that may impact flight operations.




## Timeline

## Constraints

## Gaps
