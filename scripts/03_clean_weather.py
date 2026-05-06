import os
import pandas as pd
import numpy as np

RAW_PATH = "data/raw/weather_2019.csv"
OUTPUT_PATH = "data/processed/weather_cleaned.csv"

os.makedirs("data/processed", exist_ok=True)


def parse_tmp(value):
    """
    NOAA TMP format is often like '+0039,1'.
    First part is temperature in tenths of degrees Celsius.
    """
    if pd.isna(value):
        return np.nan

    try:
        temp_part = str(value).split(",")[0]
        temp = int(temp_part) / 10

        # NOAA missing temperature often appears as 999.9
        if temp == 999.9:
            return np.nan

        return temp
    except:
        return np.nan


def parse_vis(value):
    """
    NOAA VIS format is often like '016000,1,9,9'.
    First part is visibility in meters.
    """
    if pd.isna(value):
        return np.nan

    try:
        vis_part = str(value).split(",")[0]
        visibility = int(vis_part)

        # NOAA missing visibility often appears as 999999
        if visibility == 999999:
            return np.nan

        return visibility
    except:
        return np.nan


def parse_wnd(value):
    """
    NOAA WND format is often like '270,1,N,0057,1'.
    Fourth part is wind speed in tenths of meters per second.
    """
    if pd.isna(value):
        return np.nan

    try:
        parts = str(value).split(",")
        wind_speed = int(parts[3]) / 10

        # NOAA missing wind speed often appears as 999.9
        if wind_speed == 999.9:
            return np.nan

        return wind_speed
    except:
        return np.nan


def parse_precip(value):
    """
    NOAA AA1 format is often like '01,0000,9,1'.
    Second part is precipitation depth in tenths of millimeters.
    """
    if pd.isna(value):
        return 0

    try:
        parts = str(value).split(",")
        precip = int(parts[1]) / 10

        # NOAA missing precipitation often appears as 9999.9
        if precip == 9999.9:
            return np.nan

        return precip
    except:
        return 0


def main():
    print("Loading weather data...")

    if not os.path.exists(RAW_PATH):
        raise FileNotFoundError(
            f"{RAW_PATH} not found. Make sure weather_2019.csv is in data/raw/"
        )

    df = pd.read_csv(RAW_PATH, low_memory=False)

    print(f"Original rows: {len(df)}")

    # Keep only useful columns that exist in the file
    needed_cols = ["STATION", "NAME", "DATE", "TMP", "VIS", "WND", "AA1"]
    existing_cols = [col for col in needed_cols if col in df.columns]
    df = df[existing_cols].copy()

    # Standardize timestamp/date
    df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce")
    df["weather_date"] = df["DATE"].dt.date

    # Parse NOAA encoded weather fields
    if "TMP" in df.columns:
        df["temperature_c"] = df["TMP"].apply(parse_tmp)

    if "VIS" in df.columns:
        df["visibility_m"] = df["VIS"].apply(parse_vis)

    if "WND" in df.columns:
        df["wind_speed_mps"] = df["WND"].apply(parse_wnd)

    if "AA1" in df.columns:
        df["precipitation_mm"] = df["AA1"].apply(parse_precip)
    else:
        df["precipitation_mm"] = 0

    # Drop rows without station/date because they cannot be integrated
    df = df.dropna(subset=["STATION", "weather_date"])

    # Aggregate hourly observations to daily weather summaries
    daily_weather = (
        df.groupby(["STATION", "NAME", "weather_date"], as_index=False)
        .agg({
            "temperature_c": "mean",
            "visibility_m": "mean",
            "wind_speed_mps": "mean",
            "precipitation_mm": "sum"
        })
    )

    # Create simplified weather indicators
    daily_weather["low_visibility_day"] = daily_weather["visibility_m"] < 5000
    daily_weather["precipitation_day"] = daily_weather["precipitation_mm"] > 0
    daily_weather["high_wind_day"] = daily_weather["wind_speed_mps"] > 10

    daily_weather.to_csv(OUTPUT_PATH, index=False)

    print(f"Cleaned daily weather rows: {len(daily_weather)}")
    print(f"Saved cleaned weather data to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()