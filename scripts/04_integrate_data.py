import os
import pandas as pd

FLIGHTS_PATH = "data/processed/flights_cleaned.csv"
WEATHER_PATH = "data/processed/weather_cleaned.csv"
OUTPUT_PATH = "data/processed/integrated_flights_weather.csv"
SUMMARY_PATH = "results/tables/integration_summary.csv"

os.makedirs("data/processed", exist_ok=True)
os.makedirs("results/tables", exist_ok=True)


def main():
    print("Loading cleaned datasets...")

    if not os.path.exists(FLIGHTS_PATH):
        raise FileNotFoundError("flights_cleaned.csv not found. Run 02_clean_flights.py first.")

    if not os.path.exists(WEATHER_PATH):
        raise FileNotFoundError("weather_cleaned.csv not found. Run 03_clean_weather.py first.")

    flights = pd.read_csv(FLIGHTS_PATH, low_memory=False)
    weather = pd.read_csv(WEATHER_PATH, low_memory=False)

    print(f"Cleaned flight rows: {len(flights)}")
    print(f"Cleaned weather rows: {len(weather)}")

    # Convert date columns to datetime for merging
    flights["flight_date"] = pd.to_datetime(flights["flight_date"], errors="coerce")
    weather["weather_date"] = pd.to_datetime(weather["weather_date"], errors="coerce")

    # Map NOAA weather station to airport code.
    # This NOAA dataset is for Chicago O'Hare International Airport.
    airport_station_map = {
        "ORD": "72530094846"
    }

    station_map_df = pd.DataFrame([
        {"origin": airport, "STATION": station}
        for airport, station in airport_station_map.items()
    ])

    weather["STATION"] = weather["STATION"].astype(str)
    station_map_df["STATION"] = station_map_df["STATION"].astype(str)

    # Add airport code to weather data
    weather = weather.merge(station_map_df, on="STATION", how="left")

    # Keep only weather observations that map to an airport
    weather = weather.dropna(subset=["origin"])

    # Since the available weather data is for ORD, only ORD flights can be matched
    flights_for_merge = flights[flights["origin"].isin(airport_station_map.keys())].copy()

    print(f"Flight rows eligible for weather merge: {len(flights_for_merge)}")

    # Merge flights and daily weather by origin airport and date
    merged = flights_for_merge.merge(
        weather,
        left_on=["origin", "flight_date"],
        right_on=["origin", "weather_date"],
        how="inner"
    )

    print(f"Integrated rows: {len(merged)}")

    # Save integrated dataset
    merged.to_csv(OUTPUT_PATH, index=False)

    # Create integration summary table
    summary = pd.DataFrame({
        "metric": [
            "cleaned_flight_rows",
            "cleaned_weather_rows",
            "flight_rows_eligible_for_merge",
            "integrated_rows",
            "airports_integrated"
        ],
        "value": [
            len(flights),
            len(weather),
            len(flights_for_merge),
            len(merged),
            ", ".join(sorted(merged["origin"].dropna().unique()))
        ]
    })

    summary.to_csv(SUMMARY_PATH, index=False)

    print(f"Saved integrated dataset to: {OUTPUT_PATH}")
    print(f"Saved integration summary to: {SUMMARY_PATH}")


if __name__ == "__main__":
    main()