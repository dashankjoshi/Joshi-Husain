import os
import pandas as pd

RAW_PATH = "data/raw/flights_2019.csv"
OUTPUT_PATH = "data/processed/flights_cleaned.csv"

os.makedirs("data/processed", exist_ok=True)


def main():
    print("Loading flight data...")

    if not os.path.exists(RAW_PATH):
        raise FileNotFoundError(
            f"{RAW_PATH} not found. Download flights_2019.csv and place it in data/raw/"
        )

    columns_needed = [
        "YEAR",
        "MONTH",
        "DAY_OF_MONTH",
        "FL_DATE",
        "OP_UNIQUE_CARRIER",
        "OP_CARRIER_FL_NUM",
        "ORIGIN",
        "ORIGIN_CITY_NAME",
        "ORIGIN_STATE_NM",
        "DEST",
        "DEST_CITY_NAME",
        "DEST_STATE_NM",
        "DEP_DELAY",
        "ARR_DELAY",
        "DISTANCE",
        "CARRIER_DELAY",
        "WEATHER_DELAY",
        "NAS_DELAY",
        "LATE_AIRCRAFT_DELAY"
    ]

    df = pd.read_csv(RAW_PATH, usecols=columns_needed, low_memory=False)

    print(f"Original rows: {len(df)}")

    # Standardize date
    df["FL_DATE"] = pd.to_datetime(df["FL_DATE"], errors="coerce")

    # Remove rows missing the main fields needed for analysis
    df = df.dropna(subset=["FL_DATE", "ORIGIN", "DEST", "DEP_DELAY", "ARR_DELAY"])

    # Convert delay columns to numeric
    delay_cols = [
        "DEP_DELAY",
        "ARR_DELAY",
        "CARRIER_DELAY",
        "WEATHER_DELAY",
        "NAS_DELAY",
        "LATE_AIRCRAFT_DELAY"
    ]

    for col in delay_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Cause-specific delay columns are often missing when there is no reportable delay
    cause_delay_cols = [
        "CARRIER_DELAY",
        "WEATHER_DELAY",
        "NAS_DELAY",
        "LATE_AIRCRAFT_DELAY"
    ]

    for col in cause_delay_cols:
        df[col] = df[col].fillna(0)

    # Focus on major airports for a manageable and meaningful analysis
    major_airports = ["ATL", "ORD", "JFK", "LAX", "DFW"]
    df = df[df["ORIGIN"].isin(major_airports)]

    # Remove extreme outliers so rare disruptions do not dominate the analysis
    df = df[df["DEP_DELAY"] <= 600]
    df = df[df["ARR_DELAY"] <= 600]

    # Create useful analysis variables
    df["flight_date"] = df["FL_DATE"].dt.date
    df["month"] = df["FL_DATE"].dt.month
    df["is_departure_delayed"] = df["DEP_DELAY"] > 15
    df["is_weather_delay_reported"] = df["WEATHER_DELAY"] > 0

    # Rename columns for readability
    df = df.rename(columns={
        "YEAR": "year",
        "MONTH": "month_original",
        "DAY_OF_MONTH": "day_of_month",
        "FL_DATE": "flight_datetime",
        "OP_UNIQUE_CARRIER": "carrier",
        "OP_CARRIER_FL_NUM": "flight_number",
        "ORIGIN": "origin",
        "ORIGIN_CITY_NAME": "origin_city",
        "ORIGIN_STATE_NM": "origin_state",
        "DEST": "destination",
        "DEST_CITY_NAME": "destination_city",
        "DEST_STATE_NM": "destination_state",
        "DEP_DELAY": "departure_delay",
        "ARR_DELAY": "arrival_delay",
        "DISTANCE": "distance",
        "CARRIER_DELAY": "carrier_delay",
        "WEATHER_DELAY": "reported_weather_delay",
        "NAS_DELAY": "nas_delay",
        "LATE_AIRCRAFT_DELAY": "late_aircraft_delay"
    })

    df.to_csv(OUTPUT_PATH, index=False)

    print(f"Cleaned rows: {len(df)}")
    print(f"Saved cleaned flight data to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()