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
        "FL_DATE",
        "OP_CARRIER",
        "OP_CARRIER_FL_NUM",
        "ORIGIN",
        "DEST",
        "DEP_TIME",
        "DEP_DELAY",
        "ARR_DELAY",
        "CANCELLED",
        "DIVERTED",
        "AIR_TIME",
        "DISTANCE",
        "WEATHER_DELAY"
    ]

    df = pd.read_csv(RAW_PATH, usecols=columns_needed, low_memory=False)

    print(f"Original rows: {len(df)}")

    # Standardize date
    df["FL_DATE"] = pd.to_datetime(df["FL_DATE"], errors="coerce")

    # Remove cancelled/diverted flights because they do not have normal delay outcomes
    df = df[df["CANCELLED"] == 0]
    df = df[df["DIVERTED"] == 0]

    # Remove rows missing key values
    df = df.dropna(subset=["FL_DATE", "ORIGIN", "DEST", "DEP_DELAY", "ARR_DELAY"])

    # Convert delay columns to numeric
    delay_cols = ["DEP_DELAY", "ARR_DELAY", "WEATHER_DELAY"]
    for col in delay_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # In BTS data, WEATHER_DELAY is usually missing unless a reportable delay occurred
    df["WEATHER_DELAY"] = df["WEATHER_DELAY"].fillna(0)

    # Focus on major airports for a manageable and meaningful analysis
    major_airports = ["ATL", "ORD", "JFK", "LAX", "DFW"]
    df = df[df["ORIGIN"].isin(major_airports)]

    # Remove extreme outliers so rare operational disruptions do not dominate analysis
    df = df[df["DEP_DELAY"] <= 600]
    df = df[df["ARR_DELAY"] <= 600]

    # Create useful analysis variables
    df["flight_date"] = df["FL_DATE"].dt.date
    df["month"] = df["FL_DATE"].dt.month
    df["is_departure_delayed"] = df["DEP_DELAY"] > 15

    # Rename columns for readability
    df = df.rename(columns={
        "FL_DATE": "flight_datetime",
        "OP_CARRIER": "carrier",
        "OP_CARRIER_FL_NUM": "flight_number",
        "ORIGIN": "origin",
        "DEST": "destination",
        "DEP_TIME": "departure_time",
        "DEP_DELAY": "departure_delay",
        "ARR_DELAY": "arrival_delay",
        "AIR_TIME": "air_time",
        "DISTANCE": "distance",
        "WEATHER_DELAY": "reported_weather_delay"
    })

    df.to_csv(OUTPUT_PATH, index=False)

    print(f"Cleaned rows: {len(df)}")
    print(f"Saved cleaned flight data to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
