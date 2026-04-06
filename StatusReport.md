# Status Report

## Project Overview

Our project aims to analyze how weather conditions affect flight delays at major airports in the United States. We are integrating flight performance data from the U.S. Bureau of Transportation Statistics (BTS) with weather data from the National Oceanic and Atmospheric Administration (NOAA). The goal is to identify relationships between weather variables such as precipitation, wind speed, temperature, and visibility and flight delays.

Since submitting our project plan, we have made progress in data acquisition, initial data exploration, and early data cleaning steps. We have also refined aspects of our project plan based on feedback and a better understanding of the datasets.

---

## Progress on Planned Tasks

### 1. Data Acquisition

We successfully downloaded both datasets described in our project plan:

- **Flight Dataset (BTS)**  
  Stored in: `data/raw/T_ONTIME_REPORTING.csv`  
  Source: https://transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ&QO_fu146_anzr=b0-gvzr  

- **Weather Dataset (NOAA Global Hourly Data)**  
  Stored in: `data/raw/4252569.csv`  
  Source: https://www.ncei.noaa.gov/access/search/data-search/global-hourly  

Both datasets are in CSV format and come from U.S. government sources, ensuring reliability and compliance with open data policies.

---

### 2. Data Profiling and Initial Exploration

We explored both datasets to understand their structure and identify key variables.

**Flight dataset observations:**
- Contains columns such as `FL_DATE`, `ORIGIN`, `DEST`, `DEP_DELAY`, and `WEATHER_DELAY`
- Includes large volumes of data across multiple airports and dates
- Some delay values are missing or contain extreme values

**Weather dataset observations:**
- Contains hourly weather observations including `TMP`, `WND`, `VIS`, and `AA1`
- Uses station identifiers rather than airport codes
- Contains multiple observations per day

This exploration helped us identify how the datasets can be integrated and what cleaning steps are required.

---

### 3. Data Cleaning (In Progress)

We have begun initial data cleaning steps:

**Flight dataset:**
- Converted `FL_DATE` to a standard datetime format
- Identified missing values in delay-related columns
- Planned filtering of cancelled flights and extreme outliers

**Weather dataset:**
- Identified relevant variables (temperature, wind, visibility, precipitation)
- Began parsing timestamps into consistent date formats
- Noted the need to aggregate hourly data into daily summaries

Further cleaning will be completed in the next phase of the project.

---

### 4. Data Integration (Planned)

We have not yet completed the full integration, but we have defined a clear approach.

The datasets will be merged using:

- Airport location (origin airport)
- Date (daily aggregation)

Since the weather dataset uses station IDs instead of airport codes, we plan to create a mapping between weather stations and airport locations.

We will likely aggregate weather data to a daily level to match the flight dataset.

---

### 5. Repository Organization

We have organized our repository to support reproducibility:


We plan to add scripts for cleaning, integration, and analysis in the `scripts/` directory.

---

## Team Contributions

### Dashank Joshi
- Led dataset acquisition and verification of sources
- Organized repository structure and documentation
- Conducted initial exploration of the flight dataset
- Contributed to writing and revising this status report

---


