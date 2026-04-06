# Status Report

## Project Overview

Our project aims to analyze how weather conditions affect flight delays at major airports in the United States. We are integrating flight performance data from the U.S. Bureau of Transportation Statistics (BTS) with weather data from the National Oceanic and Atmospheric Administration (NOAA). The goal is to identify relationships between weather variables such as precipitation, wind speed, temperature, and visibility and flight delays.

Since submitting our project plan, we have made progress in data acquisition, initial data exploration, and early data cleaning steps. We have also refined aspects of our project plan based on feedback and a better understanding of the datasets.

---

## Progress on Planned Tasks

### 1. Data Acquisition

We successfully downloaded both datasets described in our project plan:

- **Flight Dataset (BTS)**  
  Stored in: `data/raw/flights.csv`  
  Source: https://transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ&QO_fu146_anzr=b0-gvzr  

- **Weather Dataset (NOAA Global Hourly Data)**  
  Stored in: `data/raw/weather.csv`  
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
### 5. Repository Organization

We have organized our repository to support reproducibility:

To ensure reproducibility, we will develop a structured workflow that automates the process from data acquisition to analysis. This workflow will include scripts for loading data, cleaning datasets, integrating the data, and generating results.

We plan to organize our scripts as follows:
- `clean_data.py` for preprocessing both datasets
- `merge_data.py` for integrating flight and weather data
- `analysis.py` for generating summary statistics and visualizations

All steps will be documented so that another user can reproduce the results by following the same sequence of operations. Additionally, we will clearly specify file paths, dependencies, and execution steps within our repository.

This approach ensures transparency and aligns with the reproducibility requirements outlined in the project guidelines.

We plan to add scripts for cleaning, integration, and analysis in the `scripts/` directory.

---

## Updated Timeline

| Task | Status | Updated Plan |
|------|--------|-------------|
| Dataset acquisition | Completed | No changes |
| Data profiling | Completed | No changes |
| Data cleaning | In progress | Complete within next week |
| Data integration | Not started | Begin after cleaning |
| Exploratory analysis | Not started | Start after integration |
| Visualization | Not started | Final phase |
| Documentation | In progress | Ongoing |

---

## Changes to Project Plan

Based on our progress and feedback from Milestone 2, we have made the following updates:

1. **Added specific dataset URLs**  
   We now explicitly include dataset links to improve reproducibility and clarity.

2. **Clarified licensing and data format**  
   We identified that both datasets are publicly available government data in CSV format, ensuring compliance with project requirements.

3. **Refined integration strategy**  
   We recognized that weather station IDs must be mapped to airport codes, which was not fully addressed in the original plan.

4. **Decided to aggregate weather data**  
   Instead of using raw hourly observations, we plan to aggregate weather variables to a daily level to match the flight dataset.

These changes improve the clarity and feasibility of our project.

---

## Challenges and Solutions

### Challenge 1: Dataset Size
The flight dataset is very large, which can slow down processing.

**Solution:**  
We plan to filter the dataset to a subset of major airports (e.g., ORD, ATL, JFK) to make processing more efficient.

---

### Challenge 2: Different Identifiers
The weather dataset uses station IDs, while the flight dataset uses airport codes.

**Solution:**  
We will create a mapping between weather stations and airport codes using publicly available station metadata or manual mapping for selected airports.

---

### Challenge 3: Time Alignment
The weather dataset is hourly, while the flight dataset is daily.

**Solution:**  
We will aggregate weather data to daily averages or summaries to align with flight dates.

---

### Challenge 4: Missing Values
Both datasets contain missing or inconsistent values.

**Solution:**  
We will apply cleaning techniques such as:
- removing rows with missing key fields
- imputing values where appropriate
- filtering out extreme outliers

---

## Team Contributions

### Dashank Joshi
- Led dataset acquisition and verification of sources
- Organized repository structure and documentation
- Conducted initial exploration of the flight dataset
- Contributed to writing and revising this status report

### Farwah Husain
- Led data cleaning and preprocessing efforts
- Explored the structure of the weather dataset
- Developed initial plan for dataset integration
- Contributed to writing and revising this status report

## Next Steps

In the next phase of the project, we will:

- Complete data cleaning for both datasets
- Create mapping between airport codes and weather stations
- Merge the datasets using shared attributes
- Perform exploratory analysis and generate visualizations
- Begin documenting the workflow for reproducibility

These steps will prepare us for the final stages of the project, including analysis, visualization, and reporting.

